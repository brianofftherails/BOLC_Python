#!/usr/bin/env python3

import helper as utils


def sentinel():
    return chr(128)


def encode_pgm(msg, coverfilename, outputfilename):
    '''Encodes a message in a PGM file
    Args:
        msg (str): the message to encode
        coverfilename (str): the name of the PGM file on disk to use as the cover
        outputfilename (str): the name of the new PGM file to write
    Returns:
        None
    '''
    input_tuple = utils.read_pgm(coverfilename)
    header = input_tuple[0]
    cover = input_tuple[1]
    utils.steg_encode(msg,cover) #modifies cover argument
    try:
        fobj = open(outputfilename,'w')
        assert not fobj.tell()
        for line in header+cover:
            fobj.write("{}\n".format(line))
        fobj.close()
    except OSError as e:
        print(e)

def decode_pgm(filename):
    '''Decodes a message hidden in a PGM file
    Args:
        filename (str): the name of the PGM file that contains a hidden message
    Returns:
        str: the message that was encoded in the PGM file
    '''
    try:
        fileconts = utils.read_pgm(filename)
    except OSError as e:
        print(e)
    decoded_message = utils.steg_decode(fileconts[1])
    found_eom = list()
    for char in list(decoded_message):
        if char == sentinel():
            break
        else:
            found_eom.append(char)
    return ''.join(found_eom)

if __name__ == '__main__':
    pass
