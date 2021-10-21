# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from ..type import MLFeatureType

class MLAudioType (MLFeatureType): # INCOMPLETE
    """
    ML audio feature type.

    Audio type always represents floating-point linear PCM data.
    """

    def __init__ (self): # INCOMPLETE
        super().__init__("", "")

    @property
    def sample_rate (self):
        pass

    @property
    def channel_count (self):
        pass