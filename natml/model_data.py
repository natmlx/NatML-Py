# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from __future__ import annotations

from .model import MLModel

class MLModelData:

    def __init__ (self):
        pass

    def deserialize (self) -> MLModel:
        """
        Deserialize the model data to create an ML model that can be used for prediction.

        Returns:
            MLModel: ML model.
        """
        pass

    @staticmethod
    def from_hub (tag: str, access_key: str) -> MLModelData:
        """
        Fetch ML model data from NatML Hub.

        Parameters:
            tag (str): Model tag.
            access_key (str): Hub access key.
        
        Returns:
            MLModelData: ML model data.
        """
        pass

