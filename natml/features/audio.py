# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from numpy import ndarray

from ..feature import MLFeature
from ..internal.hub_feature import MLHubFeature
from ..types import MLAudioType

class MLAudioFeature (MLFeature, MLHubFeature):
    """
    ML audio feature.

    The audio feature is stored as an array with shape (S,C)
    in range [-1., 1.] where `S` is the sample count and `C` is the channel count.

    Parameters:
        sample_buffer (ndarray): Interleaved linear PCM sample buffer with shape (S,C) in range [-1., 1.].
        sample_rate (int): Sample rate in Hz.
    """

    def __init__ (self, sample_buffer: ndarray, sample_rate: int): # INCOMPLETE # Type
        super().__init__(None)
        self.__sample_buffer = sample_buffer

    @property
    def sample_buffer (self) -> ndarray:
        return self.__sample_buffer

    def serialize (self) -> dict: # INCOMPLETE
        pass