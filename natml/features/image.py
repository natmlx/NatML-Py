# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from numpy import ndarray
from PIL import Image
from typing import Union

from ..feature import MLFeature
from ..internal.hub_feature import MLHubFeature

class MLImageFeature (MLFeature, MLHubFeature):

    def __init__ (self, image: Union[ndarray, Image.Image]):
        super().__init__(None) # INCOMPLETE
        pass