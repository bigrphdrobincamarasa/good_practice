"""
**Author** : Antonio Garcia Uceda

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : a.garciauceda@erasmusmc.nl

**Date** : 2020-03-25

**Project** : good_practice

**Class to read file formats (e.g. Dicom, Nifti)**

"""


class FileReader(object):
    """Abstract class : with virtual functions to be overloaded"""

    @classmethod
    def get_image_array(cls, filename):
        return NotImplemented

    @classmethod
    def write_image_array(cls, filename, img_array, **kwargs):
        return NotImplemented


class NIFTIreader(FileReader):

    @classmethod
    def get_image_array(cls, filename):
        """Implement : read and return image array"""
        pass

    @classmethod
    def write_image_array(cls, filename, img_array, **kwargs):
        """Implement : write nifti image from image array"""
        pass


class DICOMreader(FileReader):

    @classmethod
    def get_image_array(cls, filename):
        """Implement : read and return image array"""
        pass

    @classmethod
    def write_image_array(cls, filename, img_array, **kwargs):
        """Implement : write dicom image from image array"""
        pass
