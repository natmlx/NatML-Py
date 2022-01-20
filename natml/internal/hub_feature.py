# 
#   NatML
#   Copyright (c) 2022 Yusuf Olokoba.
#

from enum import Enum
from io import BytesIO
from typing import TypedDict

class MLHubDataType (Enum):
    pass

class MLHubFeature (TypedDict):
    data: BytesIO
    type: MLHubDataType
    shape: list