# 
#   NatML
#   Copyright (c) 2021 Yusuf Olokoba.
#

from abc import ABC

class MLModel (ABC):

    def __init__ (self, session: str):
        super().__init__()
        self.__session = session