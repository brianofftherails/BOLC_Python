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

if __name__ == '__main__':
    pass
