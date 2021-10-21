# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from abc import ABC, abstractmethod

class MLHubFeature (ABC):

    def __init__ (self):
        super().__init__()

    @abstractmethod
    def serialize (self) -> dict:
        pass