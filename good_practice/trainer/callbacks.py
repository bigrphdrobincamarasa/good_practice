# Class to compute any callbacks during training the networks


class Callback(object):
    "Abstract class : with virtual functions to be overloaded"
    
    def __call__(self, *args, **kwargs):
        return NotImplemented