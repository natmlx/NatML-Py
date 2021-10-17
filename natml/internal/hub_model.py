# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from .hub_feature import MLHubFeature
from ..model import MLModel

class MLHubModel (MLModel):

    def __init__ (self, session: str):
        super().__init__(session)

    def predict (self, *inputs: MLHubFeature):
        pass