#!/usr/bin/env python3
# Credit to Capt. Matthai

def steg_encode(msg, cover):
    coverindex = 0
    for char in msg:
        charbin = format(ord(char), "0>8b")
        #print(charbin)
        for index in range(0, 8):
            coverbinl = list(format(int(cover[coverindex]), "0>8b"))
            coverbinl[-1] = charbin[index]
            cover[coverindex] = str(int("".join(coverbinl), 2))
            coverindex += 1
    #return print(cover)

def steg_decode(stego):
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

if __name__ == '__main__':
    pass

