#code for stupid stuff

#step 1:

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
    def __init__(self,instruction):
        self.opcode = instruction.digits(31,24)
        self.address = instruction.digits(23,5)
        self.rt = instruction.digits(4,0)

#class MUX

#class ALU
PC = 0
#step 1: instrcution fetch
PC = PC + 4
#instrcution memory


#step 2: 

#instruction decode

#if statement for each option, add, sub, addi
#ib (instriction bit)

if self.opcode == 1112:
    self.format = "R"
    self.type = "ADD"
    self.alucontrol = 0010
    self.aluop = 10
    #add
    pass
elif self.opcode == 1624:
    self.type = "R"
    self.type = "SUB"
    self.alucontrol = 0110
    self.aluop = 10
    #for SUB
    pass
elif self.opcode == 580:
    self.format = "I"
    self.type = "ADDI"
    #addi
    pass
elif self.opcode == 836:
    self.format = "I"
    self.type = "SUBI"
    #subi
    pass
elif self.opcode == 1986:
    self.format = "D"
    self.type = "LDUR"
    self.alucontrol = 0010
    self.aluop = 00
    #ldur
elif self.opcode == 1984:
    self.format = "D"
    self.type = "STUR"
    self.alucontrol = 0010
    self.aluop = 00
    #stur
    pass
elif self.opcode == 1104:
    self.format = "R"
    self.type = "AND"
    self.alucontrol = 0000
    self.aluop = 10
    #and
    pass
elif self.opcode == 1360:
    self.format = "R"
    self.type = "ORR"
    self.alucontrol = 0001
    self.aluop = 10
    #orr
    pass
elif self.opcode > 1439 && self.opcode < 1448:
   self.format = "CB"
    self.type = "CBZ"
    self.alucontrol = 0111
    self.aluop = 10
    #cbz
    pass
elif self.opcode > 159 && self.opcode < 192:
    self.format = "CB"
    self.type = "B"
    #b
    pass
else:
    pass

#register fetch
if self.format == "R":
    reg1 = #get value
    reg2 = 
    
    if self.type == "ADD":
        writeReg = reg1 + reg2
        pass
    elif self.type == "SUB":
        writeReg = reg1 - reg2
        pass
    elif self.type == "AND":
        pass
    else:
        #ORR
        pass
    
    pass
elif self.format == "I":
    imm = int(self.immediate, 2)
    reg1 = #get value

    if self.type == "ADDI":
        writeReg = reg1 + imm
        pass
    else:
        #SUBI
        writeReg = reg1 - imm
        pass
    pass
else self.format == "CB":
    pass
#step 3:

#execute
#address calculation

#step 4:
#memory access

#step 5:
#write back
