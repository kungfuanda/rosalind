import sys

from rosalind.seq import freq

def most_frequent(seq, chunk_size):
    """
    Return a list of the most frequent items in `seq`,
    broken up by `chunk_size`.
    """
    frequent = freq(seq, chunk_size)
    most_frequent = max(frequent.values())
    return [seq for (seq, frequency) in frequent.items() if frequency == most_frequent]


if __name__ == '__main__':
    print sys.argv
    in_file, out_file = sys.argv[1:3]
    with open(in_file, 'r') as r:
        seq, chunk_size = r.readlines()
        with open(out_file, 'w') as w:
            w.write(' '.join(most_frequent(seq, int(chunk_size))))