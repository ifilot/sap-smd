# -*- coding: utf-8 -*-

from assembler import Assembler

asm = Assembler()

data = bytearray()

data += asm.assemble('fibonacci.asm')
data += asm.assemble('knightrider.asm')
data += asm.assemble('doubling.asm')

with open('programs.bin', 'wb') as f:
    f.write(data)