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
            instructionType, RD, RN, RM = each.split()#Sets the 4 parts to invdividual variables
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            Opcode = 1112
            print(RM)
            #creates R instrcution object
            r = Rformat(RM, RN, RD, Opcode, instructionType)
            # adds new object to list
            instructionList.append(r)
        #Same concept is used for all instructions
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
            # splits the registers/numbers into perspective feilds per each instruction format
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
            #splits the registers/numbers into perspective feilds per each instruction format
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
            bOpcode = 1986
            # creates D instruction object
            d = Dformat(Opcode, ADD, RN, RT, instructionType)
            #adds new object to list
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
            # splits the registers/numbers into perspective feilds per each instruction format
            instructionType, ADD = each.split()
            ADD = int(ADD)
            Opcode = 5
            # creates B instruction object
            b = Bformat(Opcode, ADD)
            # adds new object to list
            instructionList.append(b)
        else:
            print('no instruction match')

print("start")
for i in range(len(instructionList)+1):
    print(i)
    #print(instructionList[i].opcode)
    if instructionList[i].form == "R":
        if instructionList[i].type == "ADD":
            print("ADD")
            # saves the addition of the 2 values(stored in RegFile) in the registers into the result register
            RegFile[instructionList[i].rd] = RegFile[instructionList[i].rn] + RegFile[instructionList[i].rm]
        # sub
        elif instructionList[i].type == "SUB":
            print("sub: ")
            # saves the subtraction f the 2 values(stored in RegFile) in the registers into the result register
            RegFile[instructionList[i].rd] = RegFile[instructionList[i].rn] - RegFile[instructionList[i].rm]
        # and
        elif instructionList[i].type == "AND":
            RegFile[instructionList[i].rd] = RegFile[instructionList[i].rn] and RegFile[instructionList[i].rm]
        # orr
        elif instructionList[i].type == "ORR":
            RegFile[instructionList[i].rd] = RegFile[instructionList[i].rn] or RegFile[instructionList[i].rm]
    elif instructionList[i].form == "I":
        # addi
        if instructionList[i].type == "ADDI":
            print("addi")
            # saves the addition of the register stored value(in RegFile) and  the immediate into the result register
            RegFile[instructionList[i].rd] = RegFile[instructionList[i].rn] + instructionList[i].immediate
        # subi
        elif instructionList[i].type == "SUBI":
            # saves the subtraction of the register stored value(in RegFile) and  the immediate into the result register
            RegFile[instructionList[i].rd] = RegFile[instructionList[i].rn] - instructionList[i].immediate
            print(RegFile[instructionList[i].rd])
    elif instructionList[i].form == "D":
        # ldur
        if instructionList[i].type == "LDUR":
            print("LDUR")
            #memoryaddress is the base + the offset that will be used in the dataMemory to get the value at that index
            memoryaddress = RegFile[instructionList[i].rn] + instructionList[i].address
            #loads the rt register with the value from data memory
            RegFile[instructionList[i].rt] = dataMemory[memoryaddress]
        # stur
        elif instructionList[i].type == "STUR":
            print("STUR")
            # memoryaddress is the base + the offset that will be used in the dataMemory to store the value at that index
            memoryadd = RegFile[instructionList[i].rn] + instructionList[i].address
            #stores the value into the data memory
#            print("LDUR")
            #reg to be loaded from -> instuctionList[i].rt
            memoryadd = RegFile[instructionList[i].rn] + instructionList[i].address
            RegFile[instructionList[i].rt] = dataMemory[memoryadd]
            print(RegFile[instructionList[i].rt])
            # need to do
        # stur
        elif instructionList[i].type == "STUR":
            print("STUR")
            #reg to load into data memory
            memoryadd = RegFile[instructionList[i].rn] + instructionList[i].address
            #print(dataMemory[memoryadd])
            dataMemory[memoryadd] = RegFile[instructionList[i].rt]
    # cbz
    elif instructionList[i].form == "CBZ":
         print("CBZ")
#        print(i)
         if RegFile[instructionList[i].rt] > instructionList[i].address:
            print("exit loop")
        # b
    elif instructionList[i].form == "B":
        print("B")
#        print(i)
        print(instructionList[i].address)
        #gets the address to branch back to
        i = i + instructionList[i].address
        print(i)
        print(instructionList[i].address)
    else:
        #if none of the formats
        print("Invalid Format")


