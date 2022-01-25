# 
#   NatML
#   Copyright (c) 2022 Yusuf Olokoba.
#

from abc import ABC, abstractmethod
from .predictor import MLModelData

class MLSession (ABC):
    """
    Hub prediction session.
    """

    @property
    @abstractmethod
    def model_path (self) -> str:
        """
        Path to ML model graph on the file system.
        """
        return ""

    @property
    @abstractmethod
    def model_data (self) -> MLModelData:
        """
        Model data for this session.
        """
        return None