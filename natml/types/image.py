# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from ..type import MLFeatureType

class MLImageType (MLFeatureType): # INCOMPLETE
    """
    ML image feature type.
    """

    def __init__ (self): # INCOMPLETE
        super().__init__("", "")

    @property
    def width (self):
        pass

    @property
    def height (self):
        pass

    @property
    def channels (self):
        pass