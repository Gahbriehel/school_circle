#!/usr/bin/python3

"""
Console for school circle app
"""


import cmd
import sys
import uuid
from models.base_model import BaseModel
from models import storage
from models.admin import Admin
from models.classes import Class
from models.parents import Parents
from models.schedule import Schedule
from models.students import Student
from models.subject import Subject
from models.teachers import Teacher
import os


class SchoolCircle(cmd.Cmd):
    """
    Contains the functionality for the School circle console
    """

    prompt = "(schoolCircle) " if sys.__stdin__.isatty() else ""

    classes = {
        "BaseModel": BaseModel,
        "Admin": Admin,
        "Class": Class,
        "Parents": Parents,
        "Schedule": Schedule,
        "Student": Student,
        "Subject": Subject,
        "Teacher": Teacher,
    }
    dot_cmds = ["all", "count", "show", "destroy", "update"]
    types_to_convert = {"day_of_the_week": int}
    types_not_to_convert = [
        "id",
        "created_at",
        "updated_at",
        "start_time",
        "end_time",
        "dob",
        "password",
        "gender",
    ]

    def preloop(self):
        """
        Prints if isatty is false
        """
        if not sys.__stdin__.isatty():
            print("(schoolCircle)")

    def precmd(self, line):
        """
        Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        """
        _cmd = _cls = _id = _args = ""

        if not ("." in line and "()" in line and ")" in line):
            return line

        try:
            pline = line[:]

            _cls = pline[: pline.find(".")]

            _cmd = pline[pline.find(".") : pline.find("(")]
            if _cmd not in SchoolCircle.dot_cmds:
                raise Exception

            pline = pline[pline.find("(") + 1 : pline.find(")")]
            if pline:

                pline = pline.partition(", ")

                _id = pline[0].replace('"', "")
                if not _id:
                    raise Exception

                pline = pline[2].strip()
                if pline:

                    if (
                        pline[0] == "{"
                        and pline[-1] == "}"
                        and type(eval(pline)) == dict
                    ):
                        _args = pline
                    else:
                        _args = pline.replace(",", "")
            line = " ".join([_cmd, _cls, _id, _args])
        except Exception as error:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """
        Prints if isatty is false
        """
        if not sys.__stdin__.isatty():
            print("(schoolCircle)", end="")

        return stop

    def do_quit(self, command):
        """
        Method to exit the School Circle Console
        """
        exit()

    def help_quit(self):
        """
        Prints the help documentation for quit
        """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """
        Handles EOF to exit program
        """
        print()
        exit()

    def help_EOF(self):
        """
        Prints the help documentation for EOF
        """
        print("Exits the program without formatting\n")

    def emptyline(self):
        pass

    def do_create(self, args):
        """
        Create an object of any class
        """

        if not args:
            print("** class name missing **")
            return

        args_split = args.split(" ")

        if args_split[0] not in SchoolCircle.classes:
            print("** class doesn't exists **")
            return

        new_instance = SchoolCircle.classes[args_split[0]]
        print(new_instance)

        new_attr = {}
        for param in args_split[1:]:
            p_property, p_value = param.split("=")

            if p_value[0] == '"':
                p_value = p_value[1:-1]

                p_value = p_value.replace("_", " ")
                p_value = p_value.replace('"', '\\"')

            elif "." in p_value:
                try:
                    p_value = float(p_value)
                except:
                    print("Float could not be converted")
            else:
                try:
                    p_value = int(p_value)
                except:
                    print("Int could not be converted")
            new_attr[p_property] = p_value

        class_int = new_instance(**new_attr)
        print(class_int.id)
        class_int.save()

    def help_create(self):
        """
        Help information for the create method
        """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n [<param 1> <param 2> <param 3> ...]")

    def do_show(self, args):
        """
        Method to show an individual object
        """

        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        if c_id and " " in c_id:
            c_id = c_id.partition(" ")[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in SchoolCircle.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        # TODO: Modify here to diff query from file
        #       And from DB
        try:
            print("in here")
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found")

    def help_show(self):
        """
        Help information for the show command
        """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """
        Destroys a specified object
        """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        if c_id and " " in c_id:
            c_id = c_id.partition(" ")[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in SchoolCircle.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        # TODO: Modify here to diff query from file
        #       And from DB
        try:
            del storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found")

    def help_destroy(self):
        """
        Help information for the destroy command
        """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """
        Shows all objects, or all objects of a class
        """
        print_list = []

        if args:
            args = args.split(" ")[0]
            if args not in SchoolCircle.classes:
                print("** class doesn't exist **")
                return

            result = storage.all(args)

            for k, v in result.items():
                print_list.append(str(v))
        else:

            result = storage.all()

            for k, v in result.items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """
        Help information for the all command
        """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """
        Count current number of class instances
        """
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split(".")[0]:
                count += 1

        print(count)

    def help_count(self):
        """ """
        print("Usages: count <class_name>")

    def do_update(self, args):
        """
        Updates a certain object with new info
        """
        c_name = c_id = att_name = att_val = kwargs = ""

        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:
            print("** class name missing **")
            return

        if c_name not in SchoolCircle.classes:
            print("** class doesn't exist")
            return

        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        if key not in storage.all():
            print("** no instance found")
            return

        if "{" in args[2] and "}" in args[2] and type(eval(args[2])) == dict:
            kwargs = eval(args[2])
            args = []
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:
            args = args[2]
            if args and args[0] == '"':
                second_quote = args.find('"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1 :]

            args = args.partition(" ")

            if not att_name and args[0] != " ":
                att_name = args[0]

            if args[2] and args[2][0] == '"':
                att_val = args[2][1 : args[2].find('"', 1)]

            if not att_val and args[2]:
                att_val = args[2].partition(" ")[0]

            args = [att_name, att_val]

        new_dict = storage.all()[key]

        for i, att_name in enumerate(args):

            if i % 2 == 0:
                att_val = args[i + 1]
                if not att_name:
                    print("** attribute name missing **")
                    return
                if not att_val:
                    print("** value missing **")
                    return
                if att_name in SchoolCircle.types_to_convert:
                    att_val = SchoolCircle.types_to_convert[att_name](att_val)

                if att_name in SchoolCircle.types_not_to_convert:
                    continue

                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()

    def help_update(self):
        """Help information for the update class"""
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    SchoolCircle().cmdloop()
