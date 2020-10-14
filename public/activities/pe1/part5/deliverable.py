#!/usr/bin/env python3

import helper as utils

def sentinel():
    return chr(128)

def encode_pgm(msg,coverfilename,outputfilename):
    '''Encodes a message in a PGM file
    Args:
        msg (str): the message to encode
        coverfilename (str): the name of the PGM file on disk to use as the cover
        outputfilename (str): the name of the new PGM file to write
    Returns:
        None
    '''
    try:
        fobj = open(coverfilename,'r')
        #fobj.seek(2,0)
        #file_length = fobj.tell()
        #msglist = list(msg)
        #assert (file_length+1) >= (len(msglist)*4)
        #fobj.seek(0,11) #seek to after header
        fobj.seek(0,0)
        cover = fobj.readlines()
        header = cover[0:4]
        del cover[0:4]
        utils.steg_encode(msg,cover)
        fobj.close()
    except OSError as e:
        print(e)
    try:
        fobj = open(outputfilename,'w')
        for line in header:
            fobj.write("{}\n".format(line))
        for line in cover:
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
        fobj = open(filename,'r')
        decodeme = list()
        fobj.seek(0,11)
        for line in fobj.readlines():
            decodeme.append(line)
        decoded_list = utils.steg_decode(decodeme)
        
    except OSError as e:
        print(e)

if __name__ == '__main__':
    pass
