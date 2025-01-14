# -*- coding: utf-8 -*-

import numpy as np

# instructions
NOP  = np.uint8(0x00) #  0
JP   = np.uint8(0x01) #  1
LDA  = np.uint8(0x02) #  2
LDB  = np.uint8(0x03) #  3
ADD  = np.uint8(0x04) #  4
TAB  = np.uint8(0x05) #  5
TBA  = np.uint8(0x06) #  6
TAO  = np.uint8(0x07) #  7
STA  = np.uint8(0x08) #  8
LRA  = np.uint8(0x09) #  9
STB  = np.uint8(0x0A) # 10
LRB  = np.uint8(0x0B) # 11
JPZ  = np.uint8(0x0C) # 12
JPNZ = np.uint8(0x0D) # 13
HLT  = np.uint8(0x0E) # 14

# build simple test program
data = np.zeros(256, dtype=np.uint8)

instructions = []
instructions.append(LDA)
instructions.append(0x01)
instructions.append(LDB)
instructions.append(0x01)
instructions.append(ADD)
instructions.append(HLT)
instructions.append(HLT)


data[0:len(instructions)] = instructions

print(' '.join('0x%02X' % d for d in instructions))

print('Storing program to: program.bin')
f = open('program.bin', 'wb')
f.write(data)
f.close()
