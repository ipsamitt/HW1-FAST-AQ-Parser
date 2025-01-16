# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    assert transcribe("ACTGAACCC") == "UGACUUGGG"
    assert transcribe("") == ""
    assert transcribe("ACTGGACCC") != "UGACUUGGG"


def test_reverse_transcribe():
    assert reverse_transcribe("") == ""
    assert reverse_transcribe("ACTGAACCC") == "GGGUUCAGU"


