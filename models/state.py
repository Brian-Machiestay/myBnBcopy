#!/usr/bin/python3
"""this model defines a state"""

from models.base_model import BaseModel


class State(BaseModel):
    """the state class defines a state and inherits from
    the base class
    """
    name = ""

    def __init__(self, *arg, **kwargs):
        """the constructor for the state class"""
        super().__init__(*arg, **kwargs)
