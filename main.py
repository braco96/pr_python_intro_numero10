# -*- coding: utf-8 -*-
import re
class Punto:
    __slots__ = ("x","y")
    def __init__(self,x=0,y=0):
        self.x = float(x); self.y = float(y)
    def norma(self):
        return (self.x**2 + self.y**2) ** 0.5

