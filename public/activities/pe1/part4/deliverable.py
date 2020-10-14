#!/usr/bin/env python3

def read_pgm(filename):
    '''Reads a PGM file
    Args:
        filename (str): the file name of a PGM file on disk to read from
    Returns:
        tuple:
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    '''
    pass

def write_pgm(filename,content):
    '''Writes a PGM file
    Args:
        filename (str): the file name to be used for the written file
        content (tuple):
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    Returns:
        None
    '''
    pass

def invert(content):
    '''Modifies the pixel intensities of the given content to be inverted
    Args:
        content (tuple):
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    Returns:
        None
    '''
    pass

if __name__ == '__main__':
    pass
