# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from base64 import b64encode
from io import BytesIO
from PIL import Image

from ..feature import MLFeature
from ..internal.hub_feature import MLHubFeature
from ..types import MLImageType

class MLImageFeature (MLFeature, MLHubFeature):
    """
    ML image feature.

    Parameters:
        image (PIL.Image): Input image.
    """

    def __init__ (self, image: Image.Image): # INCOMPLETE # Type
        super().__init__(None) 
        self.__image = image

    @property
    def image (self) -> Image.Image:
        return self.__image

    def serialize (self) -> dict:
        image_buffer = BytesIO()
        self.__image.save(image_buffer, format="JPEG")
        encoded_data = image_buffer.getvalue()
        return {
            "data": b64encode(encoded_data).decode("ascii"),
            "type": "IMAGE"
        }