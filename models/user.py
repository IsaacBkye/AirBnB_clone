#!/usr/bin/python3
''' Module of class user.py '''

from models.base_model import BaseModel


class User(BaseModel):
    '''
    Inherits from BaseModel, public class attributes:
    * email: empty string
    * password: empty string
    * first_name: empty string
    * last_name: empty string
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

