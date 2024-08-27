#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel

base = BaseModel()
base1 = BaseModel()
base2 = BaseModel()


print("----------Base Model ----------")

print(base)
print(base1)
print(base2)

print("------- end ------------")
print("------- Start Save ------------")

base.save()
base1.save()
base2.save()
print("------- end Save ------------")

print(storage.all())


print(base.to_dict())
