#code for stupid stuff

#step 1:
#class binary - to binary (for numbers)

#class Rformat
class Rformat:
    def __init__(self,inctruc):
    self.opcode = instruction.digits(31,21)
    self.rm =instruction.digits(20,16)
    self.shmnt = instruction.digits(15,10)
    self.rn = instruction.digits(9,5)
    self.rd = instruction.digits(4,0)

#class Iformat
class Iformat:
    def __init__(self,instruc):
    self.opcode = instruction.digits(31,22)
    self.immediate = instruction.digits(21,10)
    self.rn = instruction.digits(9,5)
    self.rd = instruction.digits(4,0)

#class Dformat
class Dformat:
    def __init__(self,instruc):
    self.opcode = instruction.digits(31,21)
    self.address = instruction.digits(20,12)
    self.op2 = instruction.digits(11,10)
    self.rn = instruction.digits(9,5)
    self.rt = instruction.digits(4,0)

#class CBformat
class CBformat:
    def __init__(self,instruc)
    self.opcode = instruction.digits(31,24)
    self.address = instruction.digits(23,5)
    self.rt = instruction.digits(4,0)

#class MUX

#class ALU

#step 2: 
PC = 0
#instruction decode

#if statement for each option, add, sub, addi
#ib (instriction bit)

if self.opcode == 1112:
    self.instruction = ("ADD")
    self.alucontrol = 0010
    #add
    pass
elif self.opcode == 1624:
    #for SUB
    pass
elif self.opcode == 580:
    #addi
    pass
elif self.opcode == 836:
    #subi
    pass
elif self.opcode == 1986:
    #ldur
elif self.opcode == 1984:
    #stur
    pass
elif self.opcode == 1104:
    #and
    pass
elif self.opcode == 1360:
    #orr
    pass
elif self.opcode > 1439 && self.opcode < 1448:
    #cbz
    pass
elif self.opcode > 159 && self.opcode < 192:
    #b
    pass
else:
    pass

#register fetch

#step 3:
#execute
#address calculation

#step 4:
#memory access

#step 5:
#write back
