#!/usr/bin/env python3

import utility as util
import helper

def create_mask(bit):
    return 255+bit

def encode_pgm(msg, infile, outfile):
    '''LSB encodes a message
    Args:
        msg (bytes): bytes object to encode
        infile (str): name of the raw PGM file on disk to use as the cover
        outfile (str): name of the new PGM file to write
    Returns:
        None
    '''
    fconts = helper.binary_read_pgm(infile)
    fconts_list = fconts[0]
    fconts_string = fconts[1]
    raster_idx = util.raster_index(fconts_string)
    header = fconts_string[0:raster_idx]
    cover = fconts_string[raster_idx::]
    message = bin(int.from_bytes(msg,byteorder='big'))
    print("Type of message is {} of {}\n".format(type(message),type(message[0])))
    masked_message = list(map(create_mask,list(int(message))))
    try:
        fobj = open(outfile,'w')
        fobj.write(header)
        for i in range(raster_idx,len(fconts_list)):
            fobj.write(fconts_list[i]&masked_message[i])
        fobj.close()
    except OSError as e:
        print(e)

def decode_pgm(infile):
    '''LSB decodes a message
    Args:
        infile (str): name of the PGM file to read/decode
    Returns:
        bytes: message that was decoded from the PGM file
    '''
    pass

if __name__ == '__main__':
    pass
