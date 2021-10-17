# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from numpy import array, ndarray
from PIL import Image
from typing import Union

from ..feature import MLFeature
from ..internal.hub_feature import MLHubFeature

class MLTextFeature (MLFeature, MLHubFeature):
    """
    ML text feature.
    """

    def __init__ (self, text: str):
        super().__init__(None) # INCOMPLETE
        self.__text = text

    @property
    def text (self):
        return self.__text