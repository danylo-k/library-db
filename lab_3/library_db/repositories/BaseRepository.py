class BaseRepository:
    def __init__(self, model):
        self.model=model
    def get_all(self):
        return self.model.objects.all()
    def get_by_id(self, id):
        return self.model.objects.get(pk=id)
    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)
    def delete(self, id):
        obj=self.get_by_id(id)
        if obj:
            obj.delete()
            return obj
        else:
            return None
    def update(self, id,**kwargs):
        obj=self.get_by_id(id)
        if obj:
            for key,val in kwargs.items():
                setattr(obj,key,val)
            obj.save()
        return obj
