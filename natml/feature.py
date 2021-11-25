# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from __future__ import annotations
from abc import ABC
from numpy import ndarray
from PIL import Image

from .type import MLFeatureType

class MLFeature (ABC):

    def __init__ (self, type: MLFeatureType):
        super().__init__()
        self.__type = type

    @property
    def type (self) -> MLFeatureType:
        """
        Feature type.
        """
        return self.__type

    @staticmethod
    def from_numpy (array: ndarray) -> MLFeature: # INCOMPLETE
        """
        """
        pass

    @staticmethod
    def from_image (image: Image.Image) -> MLFeature: # INCOMPLETE
        """
        """
        pass

    @staticmethod
    def from_string (text: str) -> MLFeature: # INCOMPLETE
        """
        """
        pass

    @staticmethod
    def __hub_type (dtype: str) -> str:
        pass