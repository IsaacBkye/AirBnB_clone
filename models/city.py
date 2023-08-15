#!/usr/bin/python3
''' Module class city.py '''

from models.base_model import BaseModel


class City(BaseModel):
    '''
    Inherits from BaseModel, public class attributes:
    * state_id: empty string
    * name: empty string
    '''

    state_id = ""
    name = ""

