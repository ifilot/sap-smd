# -*- coding: utf-8 -*-

import numpy as np

### Hard ware details
#
# The address pins of the instruction decoder rom are
# wired as follows:
#    - A0-A3: T-state counter
#    - A4:    ZF (zero flag)
#    - A5:    CF (carry flag)
#    - A6-A13 Instruction (8 bits)
#
# Parallel counter line 7 resets the T-state counter
# and is used to proceed to the next opt code
#

### Define lines
#
# The instruction decoder allows for 8 parallel
# lines on the lower 8bit block and 2x16 orthogonal
# lines on the upper 8 bit block
#

# parallel lines
CE  = np.uint8(1 << 0)           # counter enable
FI  = np.uint8(1 << 1)           # flag in enable
SU  = np.uint8(1 << 2)           # subtract enable
HLT = np.uint8(1 << 6)           # halt instruction
RT  = np.uint8(1 << 7)           # reset T-state counter

# orthogonal lines (block 1A)
# shifted by 8 for orthogonal block 1A
MI = 1 << 8
II = 2 << 8
J  = 3 << 8
AI = 4 << 8
BI = 5 << 8
OI = 6 << 8
RI = 7 << 8
TI = 8 << 8

# orthogonal lines (block 2B)
# shifted by 12 for orthogonal block 2A
CO  = 1 << 12
RRO = 2 << 12 # rom out
AO  = 3 << 12
BO  = 4 << 12
EO  = 5 << 12
RO =  6 << 12 # ram out
TO =  7 << 12 # temp out

### define opcodes
#
# only needs five micro-instructions, on the sixth clock
# tick the ring is reset
#
NOP = [CO | MI, RRO | II | CE, RT]
JP  = [CO | MI, RRO | II | CE, CO | MI, RRO | J, RT]
LDA = [CO | MI, RRO | II | CE, CO | MI, RRO | AI | CE, RT]
LDB = [CO | MI, RRO | II | CE, CO | MI, RRO | BI | CE, RT]
ADD = [CO | MI, RRO | II | CE, 0, EO | TI | FI, TO | AI, RT]
TAB = [CO | MI, RRO | II | CE, AO | BI, RT]
TBA = [CO | MI, RRO | II | CE, BO | AI, RT]
TAO = [CO | MI, RRO | II | CE, AO | OI, RT]
STA = [CO | MI, RRO | II | CE, CO | MI, RRO | TI, TO | MI, RI | AO | CE, RT]
LRA = [CO | MI, RRO | II | CE, CO | MI, RRO | TI, TO | MI, RO | AI | CE, RT]
STB = [CO | MI, RRO | II | CE, CO | MI, RRO | TI, TO | MI, RI | BO | CE, RT]
LRB = [CO | MI, RRO | II | CE, CO | MI, RRO | TI, TO | MI, RO | BI | CE, RT]
optcodes = [NOP, JP, LDA, LDB, ADD, TAB, TBA, TAO, STA, LRA, STB, LRB]

# expand instructions to CF/ZF
microinstructions = []
for inst in optcodes:
    microinstructions.append([inst for i in range(0,4)])
    
# add specialized instructions for JPZ
JPZ1 = [CO | MI, RRO | II | CE, CE, RT]               # FLAGS: 00
JPZ2 = [CO | MI, RRO | II | CE, CO | MI, RRO | J, RT] # FLAGS: 01
microinstructions.append([JPZ1,JPZ2,JPZ1,JPZ2])

# add specialized instructions for JPNZ (opposite of JP)
microinstructions.append([JPZ2,JPZ1,JPZ2,JPZ1])

# add halt instruction at the end
HALT = [CO | MI, RRO | II | CE, HLT,HLT,HLT,HLT,HLT,HLT,HLT,HLT,HLT,HLT,HLT,HLT,HLT,HLT]
microinstructions.append([HALT,HALT,HALT,HALT])

### construct instruction set
idlower = np.zeros(2**14, dtype=np.uint8)
idupper = np.zeros(2**14, dtype=np.uint8)
ibsz = 2**6 # instruction block size
csz = 2**4  # flag blok size
for i,inst in enumerate(microinstructions):
    for j in range(0,4): # loop over all CF/ZF configurations
        for k in range(0, len(inst[j])):
            addr = i*ibsz+j*csz+k
            idlower[addr] = np.uint8(inst[j][k] & 0xFF)
            idupper[addr] = np.uint8((inst[j][k] >> 8) & 0xFF)
        

instid = 0x0
tst = 4
start = instid * ibsz
print('Instruction set:')
print('ROM 1:')
for i in range(tst*4,(tst+1)*4):
    print(' '.join('0x%02X' % d for d in idlower[start+i*16:start+(i+1)*16]))
print('ROM 2:')
for i in range(tst*4,(tst+1)*4):
    print(' '.join('0x%02X' % d for d in idupper[start+i*16:start+(i+1)*16]))
print()

print('Storing to file: instructionset_lower.bin')
f = open('instructionset_lower.bin', 'wb')
f.write(idlower)
f.close()

print('Storing to file: instructionset_upper.bin')
f = open('instructionset_upper.bin', 'wb')
f.write(idupper)
f.close()