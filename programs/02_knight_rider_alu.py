# -*- coding: utf-8 -*-

import numpy as np

# instructions
NOP  = np.uint8(0x00)
JP   = np.uint8(0x01)
LDA  = np.uint8(0x02)
LDB  = np.uint8(0x03)
ADD  = np.uint8(0x04)
TAB  = np.uint8(0x05)
TBA  = np.uint8(0x06)
TAO  = np.uint8(0x07)
JPZ  = np.uint8(0x08)
JPNZ = np.uint8(0x09)

# build simple test program
data = np.zeros(256, dtype=np.uint8)

instructions = []
instructions.append(NOP)
instructions.append(LDA)
instructions.append(0x01)
instructions.append(TAB)
lbl0 = len(instructions)
instructions.append(ADD)
instructions.append(TAO)
instructions.append(TAB)
instructions.append(JPNZ)
instructions.append(lbl0)
instructions.append(JP)
instructions.append(0x00)

data[0:len(instructions)] = instructions

print(' '.join('0x%02X' % d for d in instructions))

print('Storing program to: program.bin')
f = open('program.bin', 'wb')
f.write(data)
f.close()
