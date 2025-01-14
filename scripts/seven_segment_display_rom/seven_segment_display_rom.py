# -*- coding: utf-8 -*-

import numpy as np

def main():
    lines = build_number_to_lines()
    
    data = np.zeros(2048, dtype=np.uint8)
        
    # setting 00 - regular character output
    offset = 0
    for i in range(0,256):
        idx3 = 16 # blank character
        idx2 = i // 100
        idx1 = (i - idx2 * 100) // 10
        idx0 = i - idx2 * 100 - idx1 * 10
        
        # uncomment the line below for debugging
        #print(i, idx3, idx2, idx1, idx0)
        
        data[offset + 3 * 256 + i] = lines[idx3]
        data[offset + 2 * 256 + i] = lines[idx2]
        data[offset + 1 * 256 + i] = lines[idx1]
        data[offset + 0 * 256 + i] = lines[idx0]
    
    # setting 01 - HEX output
    offset = 1
    offset = 1024
    for i in range(0,256):
        idx3 = 16 # blank character
        idx2 = 16 # blank character
        idx1 = (i >> 4) & 0x0F
        idx0 = i & 0x0F
        
        # uncomment the line below for debugging
        #print(i, idx3, idx2, idx1, idx0)
        
        data[offset + 3 * 256 + i] = lines[idx3]
        data[offset + 2 * 256 + i] = lines[idx2]
        data[offset + 1 * 256 + i] = lines[idx1]
        data[offset + 0 * 256 + i] = lines[idx0]
        
    print('Storing seven segment display ROM')
    f = open('seven_segment_display.bin', 'wb')
    f.write(data)
    f.close()

def build_number_to_lines():
    """
    Construct an array of unsigned integers wherein each element
    in the array correspond to which lines need to be lit to
    display the corresponding character in the seven-segment
    display
    """
    #
    # bitfield for the hex characters
    #
    #  ABCDEFGP
    segments = [
     0b11111100, # 0
     0b01100000, # 1
     0b11011010, # 2
     0b11110010, # 3
     0b01100110, # 4
     0b10110110, # 5
     0b00111110, # 6
     0b11100000, # 7
     0b11111110, # 8
     0b11100110, # 9
     0b11101110, # A
     0b00111110, # b
     0b10011100, # C
     0b01111010, # d
     0b10011110, # e
     0b10001110, # F
     0b00000000, # blank
    ]

    # wiring
    wires = [3,7,6,0,1,2,4,5]

    lines = []
    for s in segments:
        l = np.uint8(0)
        for j in range(0,8):
            if s & (1 << j):
                l |= (1 << wires[j])
        lines.append(l)
    
    return lines

if __name__ == '__main__':
    main()