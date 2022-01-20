# 
#   NatML
#   Copyright (c) 2022 Yusuf Olokoba.
#

from io import BytesIO
from numpy import ndarray
from PIL import Image
from urllib.parse import quote
from .hub_feature import MLHubFeature
from ..model import MLModel

class MLHubModel (MLModel):

    def __init__ (self, session: str):
        super().__init__(session)

    def predict (self, *inputs: MLHubFeature):
        """
        Make a Hub prediction.

        Parameters:
            inputs (list): Prediction inputs. Supported types are `PIL.Image`, `numpy.ndarray`
        """
        pass

    def __serialize (self, input) -> MLHubFeature:
        # Shortcut
        if isinstance(input, MLHubFeature):
            return input
        # PIL image
        if isinstance(input, Image.Image):
            buffer = BytesIO()
            input.save(buffer, format="JPEG")
            return {
                "data": buffer,
                "type": "IMAGE"
            }
        # Numpy
        if (isinstance(input, ndarray)):
            return {
                "data": BytesIO(input.tobytes()),
                "type": input.dtype.name.upper(),
                "shape": list(input.shape)
            }
        # String
        if isinstance(input, str):
            return {
                "data": f"data:,{quote(input)}",
                "type": "STRING"
            }