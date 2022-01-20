# 
#   NatML
#   Copyright (c) 2022 Yusuf Olokoba.
#

from .predictor import MLModelData

class MLSession:
    """
    Hub prediction session.
    """

    def __init__ (self):
        pass

    @property
    def model_path (self) -> str:
        """
        Path to ML model graph on the file system.
        """
        return ""

    @property
    def model_data (self) -> MLModelData:
        """
        Model data for this session.
        """
        return None