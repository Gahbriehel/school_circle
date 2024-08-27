#!/usr/bin/python3

from models.base_model import BaseModel


base = BaseModel()

print(base)

base.save()
print(base)
print(base.to_dict())