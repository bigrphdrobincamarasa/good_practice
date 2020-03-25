"""
**Author** : Antonio Garcia Uceda

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : a.garciauceda@erasmusmc.nl

**Date** : 2020-03-25

**Project** : good_practice

**Class to compute any callbacks during training the networks**

"""


class Callback(object):
    """Abstract class : with virtual functions to be overloaded"""

    def __call__(self, *args, **kwargs):
        return NotImplemented
