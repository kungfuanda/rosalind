    #!/usr/bin/env python
"""Utility functions for manipulating DNA sequences."""
from collections import Counter


def freq(seq, chunk_size=1):
    """
    Counter object representing the frequencies of each chunk
    in `chunk_size`, contained in `seq`.
    """
    seq_limit = range(len(seq) + 1 - chunk_size)
    return Counter([seq[i:i + chunk_size] for i in seq_limit])