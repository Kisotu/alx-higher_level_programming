#!/usr/bin/python3
'''Task 11 - Student to disk and reload'''


class Student:
    '''Student class'''

    def __init__(self, first_name, last_name, age):
        '''Initialize a new Student.
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): The age of the student.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves dictionary representation of the Student.

        Args:
            attrs (list): (Optional) The attributes to represent.
        '''
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        '''Replace all attributes of the Student instance

        Args:
            json (dict): The key/value pairs to replace attributes with.
        '''
        for k, v in json.items():
            setattr(self, k, v)
