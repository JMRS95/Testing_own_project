# Import key classes/functions to make them available at package level
from .rectangle import Rectangle
from .circle import Circle

# Optional: define what gets imported with 'from shapes import *'
__all__ = ['Rectangle', 'Circle']