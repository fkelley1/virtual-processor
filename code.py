#code for stupid stuff
storedValues = [0] * 32
globals()
PC = 0
instructionList = []
file = open('input.txt', 'r')
#class Rformat
class Rformat:
    opcode = 0
    rm = 0
    rn = 0
    rd = 0
    def __init__(self, bRM, bRN, bRD, bOpcode):
        self.opcode  = bOpcode
        self.rm = bRM
        self.shmnt = format(0, '#02b')
        self.rn = bRN
        self.rd = bRD
        self.writebackValue = 0

#class Iformat
class Iformat:
    opcode = 0
    immediate = 0
    rn = 0
    rd = 0
    def __init__(self, op, im, brn, brd):
        self.opcode = op
        self.immediate = im
        self.rn = brn
        self.rd = brd
        self.writebackValue = 0

#class Dformat
class Dformat:
    opcode = 0
    address = 0
    rn = 0
    rt = 0
    def __init__(self, bOpcode, dAddress, bRN, bRT):
        self.opcode = bOpcode
        self.address = dAddress
        self.op2 = format(0, '#02b')
        self.rn = bRN
        self.rt = bRT
        self.writebackValue = 0

#class CBformat
class CBformat:
    opcode = 0
    address = 0
    rt = 0
    def __init__(self, o, ad, r):
        self.opcode = o
        self.address = ad
        self.rt = r

#class b format
class Bformat:
    opcode = format(5, '#07b')
    add = 0
    def __init__(self, o, adr):
        self.address = adr
#step 1: instrcution fetch
#Could all be put into a function but i wasn't feeling it
for each in file:
    PC = PC + 4
    if not each.strip():#Skips any line that is empty
        placeholder = 1
    else:
        PC = PC +4
        instructionType = each.split(' ')[0]#Takes first variable
        each = each.replace(',','')#Removes all ,
        each = each.replace('X','')#Removes all X
        each = each.replace('[','')
        each = each.replace(']','')
        each = each.replace('#','')
        each = each.replace('ZR','0')
        if instructionType == 'ADD':
            instructionType, RM, RN, RD = each.split()#Sets the 4 parts to invdividual variables
            RN = int(RN)
            RD = int(RD)# Type is Str and can't be set straight to Binary so have to do int first
            RM = int(RM)
            # bSA = format(shiftAmt,'#08b')
            Opcode = 1112
            print(RN + RD + RM)
            r = Rformat(RM, RN, RD, Opcode)
            instructionList.append(r)
        #Same concept is used for all instructions
        elif instructionType == 'ADDI':
            instructionType, IMM, RN, RD = each.split()
            RN = int(RN)
            RD = int(RD)
            IMM = int(IMM)
            Opcode = 580
            print(RN + RD + IMM)
            Im = Iformat(Opcode, IMM, RN, RD)
            instructionList.append(Im)
        elif instructionType == 'SUB':
            instructionType, RM, RN, RD = each.split()
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            # bSA = format(shiftAmt,'#08b')
            Opcode = 1624
            print(RN + RD + RM)
            r = Rformat(RM,RN,RD,Opcode)
            instructionList.append(r)
        elif instructionType == 'SUBI':
            instructionType, IMM, RN, RD = each.split()
            RN = int(RN)
            RD = int(RD)
            IMM = int(IMM)
            Opcode = 836
            print(RN + RD + IMM)
            Im = Iformat(Opcode, IMM, RN, RD)
            instructionList.append(Im)
        elif instructionType == 'ORR':
            instructionType, RM, RN, RD = each.split()
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            Opcode = 1360
        elif instructionType == 'AND':
            instructionType, RM, RN, RD = each.split()
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            Opcode = 1104
        elif instructionType == 'LDUR':
            instructionType, ADD, RN, RT = each.split()
            RT = int(RT)
            RN = int(RN)
            ADD = int(ADD)
            # bOP = format(OP2, '#04b')
            bOpcode = 1986
            print(RT + RN + ADD)
            d = Dformat(Opcode, ADD, RN, RT)
            instructionList.append(d)
        elif instructionType == 'STUR':
            instructionType, ADD, RN, RT = each.split()
            RT = int(RT)
            RN = int(RN)
            ADD = int(ADD)
             # bOP = format(OP2, '#04b')
            Opcode = 1984
            print(RT + RD + ADD)
            d = Dformat(Opcode, ADD, RN, RT)
            instructionList.append(d)
        elif instructionType == 'CBZ':
            instructionType, ADD, RT = each.split()
            RT = int(RT)
            ADD = int(ADD)
            opcode = 180
            print(RT + ADD)
            c = CBformat(opcode, ADD, RT)
            instructionList.append(c)
        elif instructionType == 'B':
            instructionType, ADD = each.split()
            ADD = int(ADD)
            Opcode = 5
            print(ADD)
            b = Bformat(Opcode, ADD)
            instructionList.append(b)
        else:
            print('no instruction match')

#step 2:
#instruction decode
class instrcutiondecode:
    def __init__(self):
        #add
        if self.opcode == 1112:
            writebackValue = storedValues[self.rn] + storedValues[self.rm]
        #sub
        elif self.opcode == 1624:
            writebackValue = storedValues[self.rn] - storedValues[self.rm]
        #addi
        elif self.opcode == 580:
            writebackValue = storedValues[self.rn] + storedValues[self.immediate]
        #subi
        elif self.opcode == 836:
            writebackValue = storedValues[self.rn] - storedValues[self.immediate]
        #ldur
        elif self.opcode == 1986:

            self.alucontrol = 0b0010
            self.aluop = 0
        #stur
        elif self.opcode == 1984:
            self.alucontrol = 0b0010
            self.aluop = 00
        #and
        elif self.opcode == 1104:
            writebackValue = storedValues[self.rn] and storedValues[self.rm]
        #orr
        elif self.opcode == 1360:
            writebackValue = storedValues[self.rn] or storedValues[self.rm]
        #cbz
        elif self.opcode == 180:

            self.type = "CBZ"
        #b
        else:
            newPC = self.address


# step 4:
# memory access
# if branch new PC
#address calc for loads/stores
class memoryaccess:
    def __init__(self, PC):
        if self.opcode == 5:
            PC = PC - 4 + self.address

# step 5:
# write back
# only loads and R format


for i in range(len(instructionList)):
    print(instructionList[i].opcode)




