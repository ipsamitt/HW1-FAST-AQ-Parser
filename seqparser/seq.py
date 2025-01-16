# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    print(seq)
    trans_seq = ""
    if seq == "":
        return ""
    for char in seq:
        trans_seq = trans_seq + (TRANSCRIPTION_MAPPING[char])
    return trans_seq

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    trans_seq = transcribe(seq)
    rev_trans_seq = trans_seq[::-1]
    return rev_trans_seq