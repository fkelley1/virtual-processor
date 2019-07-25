#code for stupid stuff
RegFile = [0] * 32
dataMemory = []
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
    def __init__(self, bRM, bRN, bRD, bOpcode, itype):
        self.opcode  = bOpcode
        self.rm = bRM
        self.shmnt = format(0, '#02b')
        self.rn = bRN
        self.rd = bRD
        self.type = itype
        self.form = "R"
        self.writebackValue = 0

#class Iformat
class Iformat:
    opcode = 0
    immediate = 0
    rn = 0
    rd = 0
    def __init__(self, op, im, brn, brd, itype):
        self.opcode = op
        self.immediate = im
        self.rn = brn
        self.rd = brd
        self.type = itype
        self.form = "I"
        self.writebackValue = 0

#class Dformat
class Dformat:
    opcode = 0
    address = 0
    rn = 0
    rt = 0
    def __init__(self, bOpcode, dAddress, bRN, bRT, itype):
        self.opcode = bOpcode
        self.address = dAddress
        self.op2 = format(0, '#02b')
        self.rn = bRN
        self.rt = bRT
        self.type = itype
        self.form = "D"
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
        self.form = "CBZ"

#class b format
class Bformat:
    opcode = format(5, '#07b')
    add = 0
    def __init__(self, o, adr):
        self.address = adr
        self.form = "B"

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
            print(RN)
            print(RD)
            print(IMM)
            r = Rformat(RM, RN, RD, Opcode, instructionType)
            instructionList.append(r)
        #Same concept is used for all instructions
        elif instructionType == 'ADDI':
            instructionType, IMM, RN, RD = each.split()
            RN = int(RN)
            RD = int(RD)
            IMM = int(IMM)
            Opcode = 580
            print(RN)
            print(RD)
            print(IMM)
            Im = Iformat(Opcode, IMM, RN, RD, instructionType)
            instructionList.append(Im)
        elif instructionType == 'SUB':
            instructionType, RM, RN, RD = each.split()
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            Opcode = 1624
            print(RN + RD + RM)
            r = Rformat(RM,RN,RD,Opcode, instructionType)
            instructionList.append(r)
        elif instructionType == 'SUBI':
            instructionType, IMM, RN, RD = each.split()
            RN = int(RN)
            RD = int(RD)
            IMM = int(IMM)
            Opcode = 836
            print(RN + RD + IMM)
            Im = Iformat(Opcode, IMM, RN, RD, instructionType)
            instructionList.append(Im)
        elif instructionType == 'ORR':
            instructionType, RM, RN, RD = each.split()
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            Opcode = 1360
            r = Rformat(RM, RN, RD, Opcode, instructionType)
        elif instructionType == 'AND':
            instructionType, RM, RN, RD = each.split()
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            Opcode = 1104
            r = Rformat(RM, RN, RD, Opcode, instructionType)
        elif instructionType == 'LDUR':
            instructionType, ADD, RN, RT = each.split()
            RT = int(RT)
            RN = int(RN)
            ADD = int(ADD)
            bOpcode = 1986
            print(RT + RN + ADD)
            d = Dformat(Opcode, ADD, RN, RT, instructionType)
            instructionList.append(d)
        elif instructionType == 'STUR':
            instructionType, ADD, RN, RT = each.split()
            RT = int(RT)
            RN = int(RN)
            ADD = int(ADD)
            Opcode = 1984
            print(RT + RD + ADD)
            d = Dformat(Opcode, ADD, RN, RT, instructionType)
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
        if self.type == "ADD":
            writebackValue = storedValues[self.rn] + storedValues[self.rm]
        #sub
        elif self.type == "SUB":
            writebackValue = storedValues[self.rn] - storedValues[self.rm]
        #addi
        elif self.type == "ADDI":
            writebackValue = storedValues[self.rn] + self.immediate
        #subi
        elif self.type == "SUBI":
            writebackValue = storedValues[self.rn] - self.immediate
        #ldur
        elif self.type == "LDUR":
        #need to do
            self.alucontrol = 0b0010
            self.aluop = 0
        #stur
        elif self.type == "STUR":
            #NEED TO DO
            self.alucontrol = 0b0010
            self.aluop = 00
        #and
        elif self.type == "AND":
            writebackValue = storedValues[self.rn] and storedValues[self.rm]
        #orr
        elif self.type == "ORR":
            writebackValue = storedValues[self.rn] or storedValues[self.rm]
        #cbz
        elif self.type == "CBZ":
            #NEED TO DO

            self.type = "CBZ"
        #b
        else:
            newPC = self.address


#data memmory
#stored values - reg file
#another array for memory - holds where in the memory array to get the value from
#load - get address - stored value of rn - has index for memory array
#4 levels of complexity memarray[regfile[instruction]] -> rt

# step 4:
# memory access
# if branch new PC
#address calc for loads/stores
class memoryaccess:
    def __init__(self, PC):
        if self.type == "B":
            PC = PC - 4 + self.address
        #TO DO FOR LOADS/STORES

# step 5:
# write back
# only loads and R format

for i in range(len(instructionList)):
    print(instructionList[i].opcode)
    if instructionList[i].form == "R":
        if instructionList[i].type == "ADD":
            RegFile[instructionList[i].rd] = RegFile[instructionList[i].rn] + RegFile[instructionList[i].rm]
            print("ADD")
            print(RegFile[instructionList[i].rd])
        # sub
        elif instructionList[i].type == "SUB":
            RegFile[instructionList[i].rd] = RegFile[instructionList[i].rn] - RegFile[instructionList[i].rm]
            print("testing sub: ")
            print(RegFile[instructionList[i].rd])
        # and
        elif instructionList[i].type == "AND":
            RegFile[instructionList[i].rd] = RegFile[instructionList[i].rn] and RegFile[
                instructionList[i].rm]
        # orr
        elif instructionList[i].type == "ORR":
            RegFile[instructionList[i].rd] = RegFile[instructionList[i].rn] or RegFile[
                instructionList[i].rm]
    elif instructionList[i].form == "I":
        # addi
        if instructionList[i].type == "ADDI":
            print("addi")
            print(instructionList[i].immediate)
            print(RegFile[instructionList[i].rd])
            RegFile[instructionList[i].rd] = RegFile[instructionList[i].rn] + instructionList[i].immediate
            print(RegFile[instructionList[i].rd])
        # subi
        elif instructionList[i].type == "SUBI":
            RegFile[instructionList[i].rd] = RegFile[instructionList[i].rn] - instructionList[i].immediate
            print(RegFile[instructionList[i].rd])
    elif instructionList[i].form == "D":
        # ldur
        if instructionList[i].type == "LDUR":
            print("LDUR")
            # need to do
        # stur
        elif instructionList[i].type == "STUR":
            # NEED TO DO
            print("STUR")
        # cbz
    elif instructionList[i].form == "CBZ":
        # NEED TO DO
        print("CBZ")
        instructionList[i].type = "CBZ"
        # b
    else:
        print("B")
        newPC = instructionList[i].address
