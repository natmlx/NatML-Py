# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from base64 import b64encode
from numpy import ndarray

from ..feature import MLFeature
from ..internal.hub_feature import MLHubFeature
from ..types import MLArrayType

class MLArrayFeature (MLFeature, MLHubFeature):
    """
    ML array feature.

    Parameters:
        array (ndarray): Input array.
    """

    def __init__ (self, array: ndarray): # INCOMPLETE # Type
        super().__init__(None)
        self.__data = array

    @property
    def data (self) -> ndarray:
        return self.__data

    def serialize (self) -> dict:
        return {
            "data": b64encode(self.__data).decode("ascii"),
            "type": self.__data.dtype.name.upper(),
            "shape": list(self.__data.shape)
        }
