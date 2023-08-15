#!/usr/bin/python3
''' Module of class review.py '''

from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Inherits from BaseModel, public class attributes:
    * place_id: empty string
    * user_id: empty string
    * text: empty string
    '''

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        ''' Initialization of inherit super class '''
        super().__init__(*args, **kwargs)
