# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from numpy import array, ndarray
from PIL import Image
from typing import Union

from ..feature import MLFeature
from ..internal.hub_feature import MLHubFeature
from ..types import MLImageType

class MLImageFeature (MLFeature, MLHubFeature):
    """
    ML image feature.

    The image feature is stored as an array with shape (H,W,C).
    """

    def __init__ (self, image: Union[Image.Image, ndarray]):
        """
        Create an image feature.

        Parameters:
            image (PIL.Image | ndarray): RGB image in range [0, 255].
        """
        super().__init__(None) # INCOMPLETE
        self.__image = array(image) if isinstance(image, Image.Image) else image

    @property
    def image (self) -> ndarray:
        return self.__image

    def serialize (self) -> dict: # INCOMPLETE
        pass