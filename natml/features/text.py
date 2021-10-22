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

    Parameters:
        text (str): Input text.
    """

    def __init__ (self, text: str): # INCOMPLETE # Type
        super().__init__(None)
        self.__text = text

    @property
    def text (self) -> str:
        return self.__text

    def serialize (self) -> dict:
        return { "data": self.__text, "type": "STRING" }