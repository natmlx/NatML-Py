# 
#   NatML
#   Copyright (c) 2022 Yusuf Olokoba.
#

from numpy import array
from PIL import Image
from pytest import mark

from natml.features import MLArrayFeature, MLImageFeature, MLTextFeature

def test_serialize_array ():
    dtype = "float32"
    x = array([
        [10., 34.],
        [2.2, -4.9]
    ], dtype=dtype)
    feature = MLArrayFeature(x)
    hub_feature = feature.serialize()
    assert hub_feature["type"] == dtype.upper()

@mark.parametrize("image_path", [
    "test/media/1.jpg",
    "test/media/2.jpg",
])
def test_serialize_image (image_path): # INCOMPLETE
    image = Image.open(image_path)
    feature = MLImageFeature(image)
    hub_feature = feature.serialize()
    assert hub_feature["type"] == "IMAGE"

def test_serialize_text ():
    text = "Hello from NatML!"
    feature = MLTextFeature(text)
    hub_feature = feature.serialize()
    assert hub_feature["data"] == text and hub_feature["type"] == "STRING"