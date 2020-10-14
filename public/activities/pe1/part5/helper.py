#!/usr/bin/env python3

def steg_encode_char(char, cover):
    # ENCODES SINGLE CHARACTER
    msgbin = format(ord(char), "0>8b")
    #print(msgbin)
    for i in range(0, 8):
        coverbinl = list(format(int(cover[i]), "0>8b"))
        coverbinl[-1] = msgbin[i]
        cover[i] = str(int("".join(coverbinl), 2))
        #print(cover[i])

def steg_decode_char(stego):
    # DECODES SINGLE CHARACTER
    msgbits = []
    for b in stego:
        msgbits.append(bin(int(b))[-1])
    message = chr(int("".join(msgbits), 2))
    return message

def steg_encode(msg, cover):
    # ENCODES WORD
    coverindex = 0
    for char in msg:
        charbin = format(ord(char), "0>8b")
        #print(charbin)
        for index in range(0, 8):
            coverbinl = list(format(int(cover[coverindex]), "0>8b"))
            coverbinl[-1] = charbin[index]
            cover[coverindex] = str(int("".join(coverbinl), 2))
            coverindex += 1

def steg_decode(stego):
    #DECODES WORD
    msgbits = []
    for b in stego:
        msgbits.append(bin(int(b))[-1])
    #print(msgbits)
    all_bytes = [msgbits[i : i + 8] for i in range(0, len(msgbits), 8)]
    #print(all_bytes)
    decoded = ""
    for byte in all_bytes:
        decoded += chr(int("".join(byte), 2))
    return decoded

def read_pgm(filename):
    '''Reads a PGM file
    Args:
        filename (str): the file name of a PGM file on disk to read from
    Returns:
        tuple:
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    '''
    headerlist = list()
    pixelintensity = list()
    try:
        fobj = open(filename,'r+')
        fobj.seek(0,0)
        for line in range(0,4):
            linebuf = fobj.readline()
            headerlist.append(linebuf.rstrip('\n'))
        #whereami = fobj.tell()
        #print("My current position is {}\n".format(whereami))
        #assert(fobj.tell() == 16)
        for line in fobj.readlines():
            pixelintensity.append(line.rstrip('\n'))
    except OSError as e:
        print(e)
    print(headerlist,"\n",pixelintensity)
    return (headerlist,pixelintensity)

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
    try:
        fobj = open(filename,'w')
        headers = content[0]
        intensities = content[1]
        fobj.seek(0,0)
        writeme = list()
        for line in headers:
            writeme.append(line)
        for line in intensities:
            writeme.append(line)
        for line in writeme:
            fobj.write("{}\n".format(line))
    except OSError as e:
        print(e)
    finally:
        fobj.close()

def invert_helper(input_string):
    return str(255-int(input_string))


def invert(content):
    '''Modifies the pixel intensities of the given content to be inverted
    Args:
        content (tuple):
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    Returns:
        None
    '''
    content = (content[0],list(map(invert_helper,content[1])))
    
