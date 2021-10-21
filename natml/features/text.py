# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from ..feature import MLFeature
from ..internal.hub_feature import MLHubFeature
from ..types import MLTextType

class MLTextFeature (MLFeature, MLHubFeature):
    """
    ML text feature.
    """

    def __init__ (self, text: str):
        super().__init__(None) # INCOMPLETE
        self.__text = text

    @property
    def text (self) -> str:
        return self.__text

    def serialize (self) -> dict: # INCOMPLETE
        pass