#code for stupid stuff
storedValues = []
for x in 32:
    storedValues[x] = 0
instructionList = []
file = open('input.txt', 'r')
#Could all be put into a function but i wasn't feeling it
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
        if instructionType == 'ADD':
            instructionType, RM, RN, RD = each.split()#Sets the 4 parts to invdividual variables
            tempRN = int(RN)
            tempRD = int(RD)# Type is Str and can't be set straight to Binary so have to do int first
            tempRM = int(RM)
            bRN = format(tempRN,'#07b')
            bRD = format(tempRD, '#07b')# Convert To Binary
            bRM = format(tempRM, '#07b')
            bOpcode = format(1112, '#013b')
            print(bRN + bRD + bRM)
        #Same concept is used for all instructions
        elif instructionType == 'ADDI':
            instructionType, IMM, RN, RD = each.split()
            tempRN = int(RN)
            tempRD = int(RD)
            tempIMM = int(IMM)
            bRN = format(tempRN,'#07b')
            bRD = format(tempRD, '#07b')
            bIMM = format(tempIMM, '#014b')
            bOpcode = format(580, '#012b')
            print(bRN + bRD + bIMM)
        elif instructionType == 'SUB':
            instructionType, RM, RN, RD = each.split()
            tempRN = int(RN)
            tempRD = int(RD)
            tempRM = int(RM)
            bRN = format(tempRN,'#07b')
            bRD = format(tempRD, '#07b')
            bRM = format(tempRM, '#07b')
            bOpcode = format(1624, '#013b')
            print(bRN + bRD + bRM)
        elif instructionType == 'SUBI':
            instructionType, IMM, RN, RD = each.split()
            tempRN = int(RN)
            tempRD = int(RD)
            tempIMM = int(IMM)
            bRN = format(tempRN,'#07b')
            bRD = format(tempRD, '#07b')
            bIMM = format(tempIMM, '#014b')
            bOpcode = format(836, '#012b')
            print(bRN + bRD + bIMM)
        elif instructionType == 'ORR':
            instructionType, RM, RN, RD = each.split()
            tempRN = int(RN)
            tempRD = int(RD)
            tempRM = int(RM)
            bRN = format(tempRN, '#07b')
            bRD = format(tempRD, '#07b')
            bRM = format(tempRM, '#07b')
            bOpcode = format(1360, '#013b')
        elif instructionType == 'AND':
            instructionType, RM, RN, RD = each.split()
            tempRN = int(RN)
            tempRD = int(RD)
            tempRM = int(RM)
            bRN = format(tempRN, '#07b')
            bRD = format(tempRD, '#07b')
            bRM = format(tempRM, '#07b')
            bOpcode = format(1104, '#013b')
        elif instructionType == 'LDUR':
            instructionType, ADD, RN, RT = each.split()
            tempRT = int(RT)
            tempRN = int(RN)
            tempADD = int(ADD)
            bRT = format(tempRT,'#07b')
            bRN = format(tempRN,'#07b')
            bADD = format(tempADD, '#011b')
            bOpcode = format(1986, '#013b')
            print(bRT + bRN + bADD)
        elif instructionType == 'STUR':
            instructionType, ADD, RN, RT = each.split()
            tempRT = int(RT)
            tempRN = int(RN)
            tempADD = int(ADD)
            bRT = format(tempRT,'#07b')
            bRN = format(tempRN,'#07b')
            bADD = format(tempADD, '#011b')
            bOpcode = format(1984, '#013b')
            print(bRT + bRD + bADD)
        elif instructionType == 'CBZ':
            instructionType, ADD, RT = each.split()
            tempRT = int(RT)
            tempADD = int(ADD)
            bRT = format(tempRT,'#07b')
            bADD = format(tempADD,'#021b')
            bOpcode = format(180, '#010b')
            print(bRT + bADD)
        elif instructionType == 'B':
            instructionType, ADD = each.split()
            tempADD = int(ADD)
            bOpcode = format(5, '#08b')
            bADD = format(tempADD,'#028b')
            print(bADD)
        else:
            print('no instruction match')

#step 1:

#class Rformat
class Rformat:
    def __init__(self, bRM, bRN, bRD, bOpcode):
        self.opcode  = bOpcode
        self.rm = bRM
        self.shmnt = format(0, '#04b')
        self.rn = bRN
        self.rd = bRD

#class Iformat
class Iformat:
    def __init__(self, op, im, brn, brd):
        self.opcode = op
        self.immediate = im
        self.rn = brn
        self.rd = brd

#class Dformat
class Dformat:
    def __init__(self, o, ad, brn, brt):
        self.opcode = o
        self.op2 = format(0, '#02b')
        self.rn = brn
        self.rt = brt

#class CBformat
class CBformat:
    def __init__(self, o, ad, r):
        self.opcode = o
        self.address = ad
        self.rt = r

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
class instrcutiondecode:
    def __init__(self):
        if self.opcode == 1112:
            storedValues[self.rd] = storedValues[self.rn] + storedValues[self.rm]
        #add
        elif self.opcode == 1624:
            storedValues[self.rd] = storedValues[self.rn] - storedValues[self.rm]
        #for SUB
        elif self.opcode == 580:
            writeValue = storedValues[self.rn] + storedValues[self.immediate]
        #addi
        elif self.opcode == 836:
            writeValue = storedValues[self.rn] - storedValues[self.immediate]
        #subi
        elif self.opcode == 1986:

            self.alucontrol = 0b0010
            self.aluop = 00
         #ldur
        elif self.opcode == 1984:

            self.alucontrol = 0b0010
            self.aluop = 00
        #stur
        elif self.opcode == 1104:
            writeValue = storedValues[self.rn] and storedValues[self.rm]
        #and
        elif self.opcode == 1360:
            writeValue = storedValues[self.rn] or storedValues[self.rm]
        #orr
        elif self.opcode > 1439 and self.opcode < 1448:
            self.format = "CB"
            self.type = "CBZ"
            self.alucontrol = 0b0111
            self.aluop = 10
        #cbz
        elif self.opcode > 159 and self.opcode < 192:
            self.format = "CB"
            self.type = "B"
        #b
        #everything else

        #register fetch

#step 3:

#execute
#address calculation

#step 4:
#memory access

#step 5:
#write back

