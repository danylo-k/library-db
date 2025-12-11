import requests

headers = {
    'Content-Type': 'application/json'
}

username = 'dector'
password = 'itsamemario'

response1=requests.request("GET", 'http://127.0.0.1:8003/api/courses/', headers=headers, auth=(username, password))
response1_json=response1.json()
print(f'response 1 json: {type(response1_json)} {response1_json}')

response2=requests.request("GET", 'http://127.0.0.1:8003/api/courses/1', headers=headers, auth=(username, password))
response2_json=response2.json()
print(f'response 2 json: {type(response2_json)} {response2_json}')
data = {
    "course_name": "New course",
    "description": "test",
    "duration": 4,
    "price": '13.5'
}
response3=requests.request("POST", 'http://127.0.0.1:8003/api/courses/', headers=headers, auth=(username, password), json=data)
response3_json=response3.json()
print(f'response 3 json: {type(response3_json)} {response3_json}')
data2 = {
    "course_name": "Newer course"
}
response4=requests.request("PATCH", 'http://127.0.0.1:8003/api/courses/5/',  json=data2, auth=(username, password))
print(response4.status_code)
response5=requests.request("DELETE", 'http://127.0.0.1:8003/api/courses/3/', headers=headers, auth=(username, password))
print(response5.status_code)