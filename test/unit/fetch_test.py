# 
#   NatML
#   Copyright (c) 2022 Yusuf Olokoba.
#

from pytest import mark

from natml import MLModelData

MODEL_TAGS = [
    "@natsuite/mobilenet-v2"
]

@mark.parametrize("tag", MODEL_TAGS)
def test_fetch_hub (tag: str):
    model_data = MLModelData.from_hub(tag, access_key="")
    model = model_data.deserialize()