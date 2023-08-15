#!/usr/bin/python3
''' Module of class State '''

from models.base_model import BaseModel


class State(BaseModel):
    '''
    Inherits from BaseModel, public attributes:
    * name: empty string
    '''

    name = ""

    def __init__(self, *args, **kwargs):
        ''' Initialization call to super class BaseModel '''
        super().__init__(*args, **kwargs)
