import numpy as np

class Assembler:
    def __init__(self):
        self.machinecodes = {
            "NOP": np.uint8(0x00),  #  0: do nothing
            "JMP": np.uint8(0x01),  #  1: jump to address
            "LDA": np.uint8(0x02),  #  2: load from ROM address
            "LDB": np.uint8(0x03),  #  3: load from RAM address
            "ADD": np.uint8(0x04),  #  4: perform addition
            "TAB": np.uint8(0x05),  #  5: transfer A to B
            "TBA": np.uint8(0x06),  #  6: transfer B to A
            "TAO": np.uint8(0x07),  #  7: transfer A to O
            "STA": np.uint8(0x08),  #  8: store B in RAM
            "LRA": np.uint8(0x09),  #  9: load A from RAM
            "STB": np.uint8(0x0A),  # 10: store A in RAM
            "LRB": np.uint8(0x0B),  # 11: load B from RAM
            "JPZ": np.uint8(0x0C),  # 12: jump when zero set
            "JNZ": np.uint8(0x0D),  # 13: jump when not zero
            "HLT": np.uint8(0x0E)   # 14: halt (stop)
        }
        
        self.optcode_args = {
            "NOP": 0,
            "JMP": 1,
            "LDA": 1,
            "LDB": 1,
            "ADD": 0,
            "TAB": 0,
            "TBA": 0,
            "TAO": 0,
            "STA": 1,
            "LRA": 1,
            "STB": 1,
            "LRB": 1,
            "JPZ": 1,
            "JNZ": 1,
            "HLT": 0
        }
    
    def assemble(self, infile:str):
        with open(infile, 'r') as f:
            lines = f.readlines()
        
        data = []
        
        for line in lines:
            line.strip()
            inst = line.split(';')[0].strip()
            args = inst.split(' ')
            data.append(self.machinecodes[args[0]])
            for i in range(0,self.optcode_args[args[0]]):
                if args[i+1].startswith('$'):
                    data.append(int(args[i+1].replace('$', '0x'), 16))
        
        out = np.zeros(256, dtype=np.uint8)
        out[0:len(data)] = data
        
        return bytearray(out)
            