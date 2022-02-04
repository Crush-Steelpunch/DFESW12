import lrfunctions

def test_reverseaword():
    assert lrfunctions.reverseaword("cat") == "tac"

def test_reverseanotherword():
    assert lrfunctions.reverseaword("racecar") == "racecar"