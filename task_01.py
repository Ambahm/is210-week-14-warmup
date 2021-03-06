#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pet

class Dog(pet.Pet):  # super class, child class
    """Subclass for the Pet class from inported module."""

    def __init__(self, has_shots=False, **kwargs):
        """Subclass constructor

        Args:
            has_shots(bool, optional): Defaults to False, whether or not
            dog has been given shot
            kwargs: an arbitrary arg to pass dictionary for pet info

        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)









                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
# if __name__ == '__main__':
