import psutil, os
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
from library_db.models import Book
from django.db import close_old_connections


def task():
    close_old_connections()
    try:
        return run_query()
    finally:
        close_old_connections()


def run_query():
    return Book.objects.filter(page_count__gt=200).count()


def run_parallel(num_threads, num_queries):
    start=perf_counter()
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        list(executor.map(lambda _:task(),range(num_queries)))
    return perf_counter()-start

process = psutil.Process(os.getpid())

def resources():
    return {
        "ram": process.memory_info().rss / 1024 / 1024
    }

def get_res():
    THREADS=[1,2,4,8,16,32]
    q=100
    results = []
    for t in THREADS:
        time_sec=run_parallel(t, q)
        after=resources()
        results.append({
            "threads": t,
            "time_sec": round(time_sec, 3),
            "ram_mb": round(after["ram"], 1)
        })
    return results