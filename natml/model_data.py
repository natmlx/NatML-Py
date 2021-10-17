# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from __future__ import annotations
from collections import namedtuple
from typing import List

from .model import MLModel

class MLModelData:

    Normalization = namedtuple("Normalization", ["mean", "std"])

    AudioFormat = namedtuple("AudioFormat", ["sample_rate", "channel_count"])

    def __init__ (self):
        pass

    @property
    def labels (self) -> List[str]: # INCOMPLETE
        """
        Model classification labels.

        This is `None` if the model does not have any classification labels.
        """
        pass

    @property
    def normalization (self) -> Normalization: # INCOMPLETE
        """
        Expected feature normalization for predictions with this model.
        """
        pass

    @property
    def audio_format (self) -> AudioFormat: # INCOMPLETE
        """
        Expected audio format for predictions with this model.
        """
        pass

    def deserialize (self) -> MLModel: # INCOMPLETE
        """
        Deserialize the model data to create an ML model that can be used for prediction.

        Returns:
            MLModel: ML model.
        """
        pass

    @staticmethod
    def from_hub (tag: str, access_key: str) -> MLModelData: # INCOMPLETE
        """
        Fetch ML model data from NatML Hub.

        Parameters:
            tag (str): Model tag.
            access_key (str): Hub access key.
        
        Returns:
            MLModelData: ML model data.
        """
        pass
