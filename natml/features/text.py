# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

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