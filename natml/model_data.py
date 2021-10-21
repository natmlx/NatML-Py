# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from __future__ import annotations
from collections import namedtuple
from typing import List

from .model import MLModel
from .internal.hub_model import MLHubModel

class MLModelData:
    """
    Self-contained archive with ML model and supplemental data needed to make predictions.
    """

    Normalization = namedtuple("Normalization", ["mean", "std"])

    AudioFormat = namedtuple("AudioFormat", ["sample_rate", "channel_count"])

    def __init__ (self, predictor):
        self.__predictor = predictor

    @property
    def labels (self) -> List[str]:
        """
        Model classification labels.

        This is `None` if the model does not have any classification labels.
        """
        return self.__predictor["labels"]

    @property
    def normalization (self) -> Normalization:
        """
        Expected feature normalization for predictions with this model.

        This is `None` if the model does not use normalization.
        """
        normalization = self.__predictor["normalization"]
        return normalization["mean"], normalization["std"]

    @property
    def audio_format (self) -> AudioFormat:
        """
        Expected audio format for predictions with this model.

        This is `None` if the model does not use audio features.
        """
        self.__predictor["audioFormat"]

    def deserialize (self) -> MLModel:
        """
        Deserialize the model data to create an ML model that can be used for prediction.

        Returns:
            MLModel: ML model.
        """
        # Check session
        assert self.__predictor["session"], "Cannot deserialize model data because session is invalid"
        # Check type
        assert self.__predictor["type"] == "HUB", "Edge model deserialization is not yet supported"
        # Create Hub model
        return MLHubModel(self.__predictor["session"])

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
