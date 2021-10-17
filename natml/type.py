# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from abc import ABC

class MLFeatureType (ABC):

    def __init__ (self, name: str, dtype: str):
        super().__init__()
        self.__name = name
        self.__dtype = dtype

    @property
    def name (self) -> str:
        """
        Feature name.
        """
        return self.__name

    @property
    def dtype (self) -> str:
        """
        Feature data type.
        """
        return self.__dtype