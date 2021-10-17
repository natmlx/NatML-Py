# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from numpy import ndarray

from ..feature import MLFeature
from ..internal.hub_feature import MLHubFeature

class MLArrayFeature (MLFeature, MLHubFeature):
    """
    ML array feature.
    """

    def __init__ (self, array: ndarray):
        super().__init__(None) # INCOMPLETE
        self.__data = array

    @property
    def data (self):
        return self.__data