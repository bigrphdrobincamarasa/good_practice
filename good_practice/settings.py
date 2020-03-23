"""
**Author** : Robin Camarasa

**Institution** : Erasmus Medical Center

**Position** : PhD student

**Contact** : r.camarasa@erasmusmc.nl

**Date** : 2020-03-23

**Project** : good_practice

**Contains the global settings of the good_practice project**

"""
import os

# Set project root
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Set text_file.txt root
TEST_ROOT = os.path.join(PROJECT_ROOT, 'test')

# Set ressources root
RESSOURCES_ROOT = os.path.join(PROJECT_ROOT, 'ressources')

# Device on which pytorch codes will be tested
DEVICE = 'cpu'

