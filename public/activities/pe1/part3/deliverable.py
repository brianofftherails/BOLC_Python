#!/usr/bin/env python3

def steg_encode_char(char, cover):
    '''LSB encodes a character
    Args:
        char (str): a single character string
        cover (list): list of 8 strings representing integers in the range [0-255]
    Returns:
        None
    '''
    intrep = ord(char)
    bitarray = list()
    for i in range(0,8):
        if intrep > 2**(7-i):
            bitarray.append(1)
            intrep = intrep %(2**(7-i))
        elif intrep == 2**(7-i):
            bitarray.append(1)
            for k in range(i+1,8):
                bitarray.append(0)
            break
        else:
            bitarray.append(0)
    print("Bit array is {} for {}".format(bitarray,char))
    tempbuf = list(map(int,cover))
    print("Adding...\n \t{}\n +\t{}\n".format(tempbuf,bitarray))
    for i in range(len(tempbuf)):
        if (not tempbuf[i]%2 and bitarray[i]):
        # if it's even and bitarray is non-zero, do this:
            cover[i] = str(int(tempbuf[i]) + 1)
            print(f"{cover[i]}\n")
        elif (tempbuf[i]%2 and not bitarray[i]):
        #if it's odd and bitarray is zero do this:
            #tempbuf[i] = str(int(tempbuf[i]-1))
            cover[i] = str(int(tempbuf[i]-1))
            print(f"{cover[i]}\n")
        else:
            print(f"{cover[i]}\n")
    return cover
    #cover = tempbuf[::-1]
    #cover = tempbuf

def steg_decode_char(stego):
    '''LSB decodes a character
    Args:
        stego (list): list of 8 strings representing integers in the range [0-255]
    Returns:
        str: character that was decoded
    '''
    #assert len(stego) == 8
    #msb_pos = len(stego)-1
    msb_pos = 7
    charint = 0
    for i in range(len(stego)):
        if int(stego[i])%2:
            charint += 2**(msb_pos-i)
    print("Detected ASCII char {}.\n".format(chr(charint)))
    return chr(charint)

def steg_encode(msg, cover):
    '''LSB encodes a message
    Args:
        msg (str): a string message to encode
        cover (list): list of strings representing integers in the range [0-255]
    Returns:
        None
    '''
    message_list = list(msg)
    print(f"Received {message_list} to encode\n")
    encoded_message = list()
    #assert (len(message_list) == len(cover))
    for i in range(len(message_list)):
        encoded_message.append(steg_encode_char(message_list[i],cover[i]))
    print(f"Encoded to {encoded_message}\n")


def steg_decode(stego):
    '''LSB decodes a message
    Args:
        stego (list): list of strings representing integers in the range [0-255]
    Returns:
        str: message that was decoded
    '''
    stego_list = list(stego)
    print("Received {} to decode\n".format(stego_list))
    reconstructed = list()
    for char in stego_list:
        reconstructed.append(steg_decode_char(char))
    print("Reconstructed {}\n".format(reconstructed))
    return ''.join(reconstructed)

if __name__ == '__main__':
    pass

