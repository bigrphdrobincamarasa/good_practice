"""
**Author** : Antonio Garcia Uceda

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : a.garciauceda@erasmusmc.nl

**Date** : 2020-03-25

**Project** : good_practice

**Class to apply preprocessing operations to batch images (e.g. Cropping, Sliding-window, Rigid Transformation, Elastic Deformation)**

"""


class ImageGenerator(object):
    """Abstract class : with virtual functions to be overloaded"""

    def __init__(self):
        """Implement : constructor"""
        pass

    def get_image(self, in_array, **kwargs):
        return NotImplemented


class SlidingWindowImages(ImageGenerator):

    def __init__(self):
        """Implement : constructor"""
        super(SlidingWindowImages, self).__init__()
        pass

    def get_image(self, in_array, **kwargs):
        """Implement : apply preprocess operation to 'in_array' and return result"""
        pass


class TransformationRigidImages(ImageGenerator):

    def __init__(self):
        """Implement : constructor"""
        super(TransformationRigidImages, self).__init__()
        pass

    def get_image(self, in_array, **kwargs):
        """Implement : apply preprocess operation to 'in_array' and return result"""
        pass


class TransformationElasticImages(ImageGenerator):

    def __init__(self):
        """Implement : constructor"""
        super(TransformationElasticImages, self).__init__()
        pass

    def get_image(self, in_array, **kwargs):
        """Implement : apply preprocess operation to 'in_array' and return result"""
        pass
