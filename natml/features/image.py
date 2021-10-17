# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from numpy import array, ndarray
from PIL import Image
from typing import Union

from ..feature import MLFeature
from ..internal.hub_feature import MLHubFeature

class MLImageFeature (MLFeature, MLHubFeature):
    """
    ML image feature.

    The image feature is stored as an array with shape (H,W,C).
    """

    def __init__ (self, image: Union[ndarray, Image.Image]):
        """
        Create an image feature.

        Parameters:
            image (ndarray | PIL.Image): RGB image in range [0, 255].
        """
        super().__init__(None) # INCOMPLETE
        self.__image = array(image) if isinstance(image, Image.Image) else image

    @property
    def image (self):
        return self.__image