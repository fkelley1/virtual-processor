#creates register file
RegFile = [0] * 32
#creates data memory
dataMemory = [0] * 100
#stores 10 into data memory at 0
dataMemory[0]=10
#stores 13 into data memory at 1
dataMemory[1]=13
dataMemory[2]=11
globals()
PC = 0
instructionList = []
file = open('input.txt', 'r')

#template for all R instructions
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

#template for all I instructions
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

#template for all D instructions
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
        self.type = "CBZ"

#class b format
class Bformat:
    def __init__(self, adr):
        self.address = adr
        self.form = "B"
        self.opcode = 5
        self.type = "B"

#step 1: instrcution fetch
#each is acting as PC
for each in file:
    if not each.strip():#Skips any line that is empty
        placeholder = 1
    else:
        instructionType = each.split(' ')[0]#Takes first variable
        each = each.replace(',','')#Removes all ,
        each = each.replace('X','')#Removes all X
        each = each.replace('[','')
        each = each.replace(']','')
        each = each.replace('#','')
        each = each.replace('ZR','0')
        # each conditional sets the appropriate values for each field
        if instructionType == 'ADD':
            instructionType, RD, RN, RM = each.split()#Sets the 4 parts to invdividual variables
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            Opcode = 1112
            # creates R instruction object
            r = Rformat(RM, RN, RD, Opcode, instructionType)
            # adds new object to list
            instructionList.append(r)
        # Same concept is used for all instructions
        elif instructionType == 'ADDI':
            # splits the registers/numbers into perspective feilds per each instruction format
            instructionType, RD, RN, IMM = each.split()
            RN = int(RN)
            RD = int(RD)
            IMM = int(IMM)
            Opcode = 580
            # creates I instruction object
            Im = Iformat(Opcode, IMM, RN, RD, instructionType)
            # adds new object to list
            instructionList.append(Im)
        elif instructionType == 'SUB':
            # splits the registers/numbers into perspective fields per each instruction format
            instructionType, RD, RN, RM = each.split()
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            Opcode = 1624
            # creates R instruction object
            r = Rformat(RM,RN,RD,Opcode, instructionType)
            # adds new object to list
            instructionList.append(r)
        elif instructionType == 'SUBI':
            # splits the registers/numbers into perspective feilds per each instruction format
            instructionType, RD, RN, IMM = each.split()
            RN = int(RN)
            RD = int(RD)
            IMM = int(IMM)
            Opcode = 836
            # creates I instruction object
            Im = Iformat(Opcode, IMM, RN, RD, instructionType)
            # adds new object to list
            instructionList.append(Im)
        elif instructionType == 'ORR':
            # splits the registers/numbers into perspective feilds per each instruction format
            instructionType, RM, RN, RD = each.split()
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            Opcode = 1360
            # creates R instruction object
            r = Rformat(RM, RN, RD, Opcode, instructionType)
            # adds new object to list
            instructionList.append(r)
        elif instructionType == 'AND':
            # splits the registers/numbers into perspective feilds per each instruction format
            instructionType, RM, RN, RD = each.split()
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            Opcode = 1104
            # creates R instruction object
            r = Rformat(RM, RN, RD, Opcode, instructionType)
            # adds new object to list
            instructionList.append(r)
        elif instructionType == 'LDUR':
            # splits the registers/numbers into perspective feilds per each instruction format
            instructionType, RT, RN, ADD = each.split()
            RT = int(RT)
            RN = int(RN)
            ADD = int(ADD)
            Opcode = 1986
            # creates D instruction object
            d = Dformat(Opcode, ADD, RN, RT, instructionType)
            # adds new object to list
            instructionList.append(d)
        elif instructionType == 'STUR':
            # splits the registers/numbers into perspective feilds per each instruction format
            instructionType, RT, RN, ADD = each.split()
            RT = int(RT)
            RN = int(RN)
            ADD = int(ADD)
            Opcode = 1984
            # creates D instruction object
            d = Dformat(Opcode, ADD, RN, RT, instructionType)
            # adds new object to list
            instructionList.append(d)
        elif instructionType == 'CBZ':
            # splits the registers/numbers into perspective feilds per each instruction format
            instructionType, RT, ADD = each.split()
            RT = int(RT)
            ADD = int(ADD)
            opcode = 180
            # creates CB instruction object
            c = CBformat(opcode, ADD, RT)
            # adds new object to list
            instructionList.append(c)
        elif instructionType == 'B':
            # splits the registers/numbers into perspective fields per each instruction format
            instructionType, ADD = each.split()
            ADD = int(ADD)
            # creates B instruction object
            b = Bformat(ADD)
            # adds new object to list
            instructionList.append(b)
        else:
            print('no instruction match')
    #start at PC = 0
    PC = 0
    while PC in range((len(instructionList))):
        # print(PC)
        #outer if checks for format and inner if checks specific type
        if instructionList[PC].form == "R":
            if instructionList[PC].type == "ADD":
                # print("ADD")
                # saves the addition of the 2 values(stored in RegFile) in the registers into the result register
                RegFile[instructionList[PC].rd] = RegFile[instructionList[PC].rn] + RegFile[instructionList[PC].rm]
            # sub
            elif instructionList[PC].type == "SUB":
                # print("sub: ")
                # print(RegFile)
                # saves the subtraction f the 2 values(stored in RegFile) in the registers into the result register
                RegFile[instructionList[PC].rd] = RegFile[instructionList[PC].rn] - RegFile[instructionList[PC].rm]
            # and
            elif instructionList[PC].type == "AND":
                RegFile[instructionList[PC].rd] = RegFile[instructionList[PC].rn] and RegFile[instructionList[PC].rm]
            # orr
            elif instructionList[PC].type == "ORR":
                RegFile[instructionList[PC].rd] = RegFile[instructionList[PC].rn] or RegFile[instructionList[PC].rm]
        elif instructionList[PC].form == "I":
            # addi
            if instructionList[PC].type == "ADDI":
                # print("addi")
                # print(RegFile)
                # saves the addition of the register stored value(in RegFile) and  the immediate into the result register
                RegFile[instructionList[PC].rd] = RegFile[instructionList[PC].rn] + instructionList[PC].immediate
                # print(RegFile)
            # subi
            elif instructionList[PC].type == "SUBI":
                # print("subi")
                # saves the subtraction of the register stored value(in RegFile) and  the immediate into the result register
                RegFile[instructionList[PC].rd] = RegFile[instructionList[PC].rn] - instructionList[PC].immediate
                # print(RegFile[instructionList[PC].rd])
        elif instructionList[PC].form == "D":
            # ldur
            if instructionList[PC].type == "LDUR":
                # print("LDUR")
                #memoryaddress is the base + the offset that will be used in the dataMemory to get the value at that index
                memoryaddress = RegFile[instructionList[PC].rn] + instructionList[PC].address
                #loads the rt register with the value from data memory
                RegFile[instructionList[PC].rt] = dataMemory[memoryaddress]
                # print(RegFile)
            # stur
            elif instructionList[PC].type == "STUR":
                # print("STUR")
                #reg to load into data memory
                memoryaddress = RegFile[instructionList[PC].rn] + instructionList[PC].address
                #print(dataMemory[memoryadd])
                dataMemory[memoryaddress] = RegFile[instructionList[PC].rt]
                # print(RegFile)
        # cbz
        elif instructionList[PC].form == "CBZ":
            # print("CBZ")
            # print(RegFile)
            # print(instructionList[PC].rt)
            # print(RegFile[instructionList[PC].rt])
            # print(instructionList[PC].address)
            if RegFile[instructionList[PC].rt] == 0:
                print("CBZ says exit loop now")
                break
                break
        # b
        elif instructionList[PC].form == "B":
            #gets the address to branch to
            PC = PC + instructionList[PC].address - 1
        else:
            #if none of the formats
            print("Invalid Format")
        print("At instruction: ")
        print(instructionList[PC].type)
        print("regFile:")
        print(RegFile)
        print("Data memory:")
        print(dataMemory)
        #increment PC for next instruction
        PC = PC + 1
