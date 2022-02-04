import lrfunctions
import random

def test_maxthreenumbers():
    assert lrfunctions.maxthreenumbers(10, 20, 30) == 30

def test_randint():
    var1 = random.randint(1,6)
    assert var1 < 7 and var1 > 0