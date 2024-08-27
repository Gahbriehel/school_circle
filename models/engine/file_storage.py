#!/usr/bin/python3

"""
Defines a class to manage file storage for School Circle
"""

import json


class FileStorage:
    """
    Manages storage of School circle
    """

    __file = "school_circl_db.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dict of models currently in storage
        """

        if cls is None:
            return FileStorage.__objects
        else:
            return {
                key: obj
                for key, obj in FileStorage.__objects.items()
                if isinstance(obj, cls)
            }

    def new(self, obj):
        """
        Adds new object to storage dictionary
        """

        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})


    def save(self):
        """
        Saves storage dictionary to file
        """

        with open(FileStorage.__file, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, indent=4)

    def reload(self):
        """
        Loads storage dictionary from file
        """

        from models.base_model import BaseModel
        from models.admin import Admin
        from models.classes import Class
        from models.parents import Parents
        from models.schedule import Schedule
        from models.subject import Subject
        from models.teachers import Teacher

        classes = {"BaseModel": BaseModel}

        try:
            temp = {}
            with open(FileStorage.__file, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes an obj from __objects if in __objects
        """

        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
