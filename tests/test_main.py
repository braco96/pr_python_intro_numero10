import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


def test_punto_norma():
    p = mod.Punto(3,4)
    assert abs(p.norma() - 5.0) < 1e-9
