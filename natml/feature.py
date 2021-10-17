# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from abc import ABC

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
    def __hub_type (dtype: str) -> str:
        pass