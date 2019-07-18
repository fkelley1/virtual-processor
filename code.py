#code for stupid stuff

#step 1:
#class binary

#class Rformat
class Rformat:
    def __init__(self,inctruction):
    self.opcode = instruction.digits(31,21)
    self.rm =instruction.digits(20,16)
    self.shmnt = instruction.digits(15,10)
    self.rn = instruction.digits(9,5)
    self.rd = instruction.digits(4,0)

#class Iformat
class Iformat:
    def __init__(self,instruction):
    self.opcode = instruction.digits(31,22)
    self.immediate = instruction.digits(21,10)
    self.rn = instruction.digits(9,5)
    self.rd = instruction.digits(4,0)

#class Dformat
class Dformat:
    def __init__(self,instruction):
    self.opcode = instruction.digits(31,21)
    self.address = instruction.digits(20,12)
    self.op2 = instruction.digits(11,10)
    self.rn = instruction.digits(9,5)
    self.rt = instruction.digits(4,0)

#class CBformat
class CBformat:
    def __init__(self,instruction)
    self.opcode = instruction.digits(31,24)
    self.address = instruction.digits(23,5)
    self.rt = instruction.digits(4,0)

#class MUX

#class ALU

#step 2: 
#instruction decode

#if statement for each option, add, sub, addi

#register fetch

#step 3:
#execute
#address calculation

#step 4:
#memory access

#step 5:
#write back
