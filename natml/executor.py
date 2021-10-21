# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from abc import ABC, abstractmethod
from typing import List, Union

from .model_data import MLModelData
from .feature import MLFeature

class MLExecutor (ABC):
    """
    Executor which runs ML predictions on the NatML Hub infrastructure.
    """

    def __init__ (self):
        super().__init__()

    @abstractmethod
    def initialize (self, model_data: MLModelData, graph_path: str):
        """
        Initialize the executor.
        
        This method should instantiate an ML inference session using an
        inference framework like ONNX Runtime, PyTorch, or TensorFlow.

        Parameters:
            model_data (MLModelData): Model data.
            graph_path (str): Path to ML graph on the file system.
        """
        pass

    @abstractmethod
    def predict (self, *inputs: List[MLFeature]) -> Union[MLFeature, List[MLFeature]]:
        """
        Make a prediction on one or more input features.

        Parameters:
            inputs (list): Input features.

        Returns:
            MLFeature | list: Output feature(s).
        """
        pass