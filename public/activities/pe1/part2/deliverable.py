#!/usr/bin/env python3
# Credit to Capt. Matthai

def steg_encode_char(char, cover):
    #print(cover)
    msgbin = format(ord(char), "0>8b")
    #print(msgbin)
    for i in range(0, 8):
        coverbinl = list(format(int(cover[i]), "0>8b"))
        coverbinl[-1] = msgbin[i]
        cover[i] = str(int("".join(coverbinl), 2))
        #print(cover[i])

def steg_decode_char(stego):
    msgbits = []
    for b in stego:
        msgbits.append(bin(int(b))[-1])
    message = chr(int("".join(msgbits), 2))
    return message

if __name__ == '__main__':
    char = 'a'
    cover = ['250','251','252','251','250','249','248','249']
    steg_encode_char (char, cover)
    #steg_decode_char (stego)
    steg_decode_char(['250','251','253','250','250','248','248','249'])
