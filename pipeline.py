#creates register file
RegFile = [0] * 32
#creates data memory
dataMemory = [0] * 32
#stores 10 into data memory at 0
dataMemory[0]=10
#stores 13 into data memory at 1
dataMemory[1]=13
dataMemory[2]=11
globals()
PC = 0
instructionList = []
instructionL = []
file = open('input.txt', 'r')

class inst:
    def __init__(self, instruction):
        self.instruction = instruction
        self.cyclenum = 0
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
        self.writebackvalue = 0
        self.cyclenum = 0

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
        self.writebackvalue = 0
        self.cyclenum = 0

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
        self.mem = 0
        self.cyclenum = 0

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
        self.cyclenum = 0

#class b format
class Bformat:
    def __init__(self, adr):
        self.address = adr
        self.form = "B"
        self.opcode = 5
        self.type = "B"
        self.cyclenum = 0


#step 1: instrcution fetch
#each is acting as PC


class instructionfetch:
    def __new__(self, instruction):
        #instructionType = instruction.split(' ')[0]#Takes first variable
        instruction = instruction.replace(',','')#Removes all ,
        instruction = instruction.replace('X','')#Removes all X
        instruction = instruction.replace('[','')
        instruction = instruction.replace(']','')
        instruction = instruction.replace('#','')
        instruction = instruction.replace('ZR','0')
        return instruction

class instructiondecode:
    def __init__(self, instruction, instructionType):
        # instruction conditional sets the appropriate values for instruction field
        if instructionType == 'ADD':
            instructionType, RD, RN, RM = instruction.split()#Sets the 4 parts to invdividual variables
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
            # splits the registers/numbers into perspective feilds per instruction instruction format
            instructionType, RD, RN, IMM = instruction.split()
            RN = int(RN)
            RD = int(RD)
            IMM = int(IMM)
            Opcode = 580
            # creates I instruction object
            Im = Iformat(Opcode, IMM, RN, RD, instructionType)
            # adds new object to list
            instructionList.append(Im)
        elif instructionType == 'SUB':
            # splits the registers/numbers into perspective fields per instruction instruction format
            instructionType, RD, RN, RM = instruction.split()
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            Opcode = 1624
            # creates R instruction object
            r = Rformat(RM,RN,RD,Opcode, instructionType)
            # adds new object to list
            instructionList.append(r)
        elif instructionType == 'SUBI':
            # splits the registers/numbers into perspective feilds per instruction instruction format
            instructionType, RD, RN, IMM = instruction.split()
            RN = int(RN)
            RD = int(RD)
            IMM = int(IMM)
            Opcode = 836
            # creates I instruction object
            Im = Iformat(Opcode, IMM, RN, RD, instructionType)
            # adds new object to list
            instructionList.append(Im)
        elif instructionType == 'ORR':
            # splits the registers/numbers into perspective fields per instruction instruction format
            instructionType, RM, RN, RD = instruction.split()
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            Opcode = 1360
            # creates R instruction object
            r = Rformat(RM, RN, RD, Opcode, instructionType)
            # adds new object to list
            instructionList.append(r)
        elif instructionType == 'AND':
            # splits the registers/numbers into perspective feilds per instruction instruction format
            instructionType, RM, RN, RD = instruction.split()
            RN = int(RN)
            RD = int(RD)
            RM = int(RM)
            Opcode = 1104
            # creates R instruction object
            r = Rformat(RM, RN, RD, Opcode, instructionType)
            # adds new object to list
            instructionList.append(r)
        elif instructionType == 'LDUR':
            # splits the registers/numbers into perspective feilds per instruction instruction format
            instructionType, RT, RN, ADD = instruction.split()
            RT = int(RT)
            RN = int(RN)
            ADD = int(ADD)
            Opcode = 1986
            # creates D instruction object
            d = Dformat(Opcode, ADD, RN, RT, instructionType)
            # adds new object to list
            instructionList.append(d)
        elif instructionType == 'STUR':
            # splits the registers/numbers into perspective feilds per instruction instruction format
            instructionType, RT, RN, ADD = instruction.split()
            RT = int(RT)
            RN = int(RN)
            ADD = int(ADD)
            Opcode = 1984
            # creates D instruction object
            d = Dformat(Opcode, ADD, RN, RT, instructionType)
            # adds new object to list
            instructionList.append(d)
        elif instructionType == 'CBZ':
            # splits the registers/numbers into perspective feilds per instruction instruction format
            instructionType, RT, ADD = instruction.split()
            RT = int(RT)
            ADD = int(ADD)
            opcode = 180
            # creates CB instruction object
            c = CBformat(opcode, ADD, RT)
            # adds new object to list
            instructionList.append(c)
        elif instructionType == 'B':
            # splits the registers/numbers into perspective fields per instruction instruction format
            instructionType, ADD = instruction.split()
            ADD = int(ADD)
            # creates B instruction object
            b = Bformat(ADD)
            # adds new object to list
            instructionList.append(b)
        else:
            print('no instruction match')

    # the loop of code

#start at PC = 0
PC = 0
#while PC in range((len(instructionList))):
        # print(PC)
        #outer if checks for format and inner if checks specific

class execute:
    def __new__(self, instruction, PC):
        print("executing")
        if instructionList[PC].form == "R":
            if instructionList[PC].type == "ADD":
                print(str(instructionList[PC].type) + " X" + str(instructionList[PC].rd) + ", X" + str(
                    instructionList[PC].rn) + ", X" + str(instructionList[PC].rm))
                print(instructionL[PC].instruction)
                # saves the addition of the 2 values(stored in RegFile) in the registers into the result register
                instructionList[PC].writebackvalue = RegFile[instructionList[PC].rn] + RegFile[instructionList[PC].rm]
            # sub
            elif instructionList[PC].type == "SUB":
                print(str(instructionList[PC].type) + " X" + str(instructionList[PC].rd) + ", X" + str(
                    instructionList[PC].rn) + ", X" + str(instructionList[PC].rm))
                instructionList[PC].writebackvalue = RegFile[instructionList[PC].rn] - RegFile[instructionList[PC].rm]
            # and
            elif instructionList[PC].type == "AND":
                print(str(instructionList[PC].type) + " X" + str(instructionList[PC].rd) + ", X" + str(
                    instructionList[PC].rn) + ", X" + str(instructionList[PC].rm))
                instructionList[PC].writebackvalue = RegFile[instructionList[PC].rn] and RegFile[instructionList[PC].rm]
                RegFile[instructionList[PC].rd] = RegFile[instructionList[PC].rn] and RegFile[instructionList[PC].rm]
            # orr
            elif instructionList[PC].type == "ORR":
                print(str(instructionList[PC].type) + " X" + str(instructionList[PC].rd) + ", X" + str(
                    instructionList[PC].rn) + ", X" + str(instructionList[PC].rm))
                RegFile[instructionList[PC].rd] = RegFile[instructionList[PC].rn] or RegFile[instructionList[PC].rm]
        elif instructionList[PC].form == "I":
            # addi
            if instructionList[PC].type == "ADDI":
                print("adding i")
                print(str(instructionList[PC].type) + " X" + str(instructionList[PC].rd) + ", X" + str(
                    instructionList[PC].rn) + ", #" + str(instructionList[PC].immediate))
                instructionList[PC].writebackvalue = RegFile[instructionList[PC].rn] + instructionList[PC].immediate
                print(instructionList[PC].writebackvalue)
            # subi
            elif instructionList[PC].type == "SUBI":
                print(str(instructionList[PC].type) + " X" + str(instructionList[PC].rd) + ", X" + str(
                    instructionList[PC].rn) + ", #" + str(instructionList[PC].immediate))
                instructionList[PC].writebackvalue = RegFile[instructionList[PC].rn] - instructionList[PC].immediate
        elif instructionList[PC].form == "D":
            # ldur
            if instructionList[PC].type == "LDUR":
                print(str(instructionList[PC].type) + " X" + str(instructionList[PC].rt) + ", [X" + str(
                    instructionList[PC].rn) + ", #" + str(instructionList[PC].address) + "]")
                instructionList[PC].mem = RegFile[instructionList[PC].rn] + instructionList[PC].address
            # stur
            elif instructionList[PC].type == "STUR":
                print(str(instructionList[PC].type) + " X" + str(instructionList[PC].rt) + ", [X " + str(
                    instructionList[PC].rn) + ", #" + str(instructionList[PC].address))
                instructionList[PC].mem = RegFile[instructionList[PC].rn] + instructionList[PC].address
        # cbz
        elif instructionList[PC].form == "CBZ":
            print(str(instructionList[PC].type) + " X" + str(instructionList[PC].rt) + ", " + str(instructionList[PC].address))
            # print("CBZ")
            # print(RegFile)
            # print(instructionList[PC].rt)
            # print(RegFile[instructionList[PC].rt])
            # print(instructionList[PC].address)
            if RegFile[instructionList[PC].rt] == 0:
                print("CBZ says exit loop now")
        # b
        elif instructionList[PC].form == "B":
            print(str(instructionList[PC].type) + " " + str(instructionList[PC].address))
            #gets the address to branch to
            PC = PC + instructionList[PC].address - 1
            print(PC)
        else:
            #if none of the formats
            print("Invalid Format")
        return PC
        #print("At instruction: " + str(PC))

class pipelineexe:
    def __init__(self, PC):
        print("pipeline exe stage")
        print(instructionL[PC].instruction)
        if instructionList[PC].form == "R":
            if instructionList[PC-1].form =="D":
                print("regs")
                print(RegFile[instructionList[PC].rn])
                print(RegFile[instructionList[PC].rm])
            if instructionList[PC-1].form == "R" or instructionList[PC-1].form == "I":
                if instructionList[PC].form == "R":
                    print("R")
                    if instructionList[PC-1].rd == instructionList[PC].rn:
                        RegFile[instructionList[PC].rn] = instructionList[PC-1].writebackvalue
                        print(instructionList[PC-1].writebackvalue)
                    if instructionList[PC-1].rd == instructionList[PC].rm:
                        RegFile[instructionList[PC].rm] = instructionList[PC-1].writebackvalue
                        print(instructionList[PC-1].writebackvalue)
                if instructionList[PC].form == "I":
                    print("i")
                    if instructionList[PC-1].rd == instructionList[PC].rn:
                        RegFile[instructionList[PC].rn] = instructionList[PC-1].writebackvalue
            if instructionList[PC-2].form == "R" or instructionList[PC-2].form == "I":
                if instructionList[PC].form == "R":
                    print("R")
                    if instructionList[PC-2].rd == instructionList[PC].rn:
                        RegFile[instructionList[PC].rn] = instructionList[PC-2].writebackvalue
                        print(instructionList[PC-2].writebackvalue)
                    if instructionList[PC-2].rd == instructionList[PC].rm:
                        RegFile[instructionList[PC].rm] = instructionList[PC-2].writebackvalue
                        print(instructionList[PC-2].writebackvalue)
                if instructionList[PC].form == "I":
                    print("i")
                    if instructionList[PC - 2].rd == instructionList[PC].rn:
                        instructionList[PC].rn = instructionList[PC - 2].writebackvalue
            if instructionList[PC-1].form == "D":
                if instructionList[PC-1].rt == instructionList[PC].rn:
                    instructionList[PC].rn = dataMemory[instructionList[PC -1].rt]
                if instructionList[PC - 1].rt == instructionList[PC].rm:
                    instructionList[PC].rm = dataMemory[instructionList[PC - 1].rt]

            else:
                print("else")
                placeholder =1

class pipelinemem:
    def __init__(self, PC):
        print("pipeline")
        if instructionList[PC].form == "D":
            print("D")
            if instructionList[PC-1].form == "R" or instructionList[PC-1].form == "I":
                print("R or i at -1")
                if instructionList[PC-1].rd == instructionList[PC].rn:
                    print("rd")
                    instructionList[PC].rn = instructionList[PC-1].writebackvalue
            if instructionList[PC - 2].form == "R" or instructionList[PC - 2].form == "I":
                if instructionList[PC-2].rd == instructionList[PC].rn:
                    instructionList[PC].rn = instructionList[PC-2].writebackvalue
            print(instructionList[PC].rn)
            instructionList[PC].mem = RegFile[instructionList[PC].rn] + instructionList[PC].address

class memory:
    def __init__(self, memory, value, PC):
        if instructionList[PC].type == "STUR":
            dataMemory[memory] = RegFile[value]
        else:
            RegFile[value] = dataMemory[memory]
            print(dataMemory[memory])

class writeback:
    def __init__(self, register, value):
        RegFile[register] = value
length = 0
for each in file:
    if not each.strip():  # Skips any line that is empty
        placeholder = 1
    else:
        newinst = inst(each)
        instructionL.append(newinst)


PC = 0
cyclecount = 0
instructioncount = 0
while PC in range(len(instructionL)+5):
        #outer if checks for format and inner if checks specific
        #TODO check each intruction to pass correct value to id pipeline register
        #id(instructionList[PC].rm, instructionList[PC].rn)
        print("PC" + str(PC))
        instruction = 0
        if instructionL[PC].cyclenum == 0 and PC < len(instructionL) + 2 :
            print("if")
            print(instructionL[PC].instruction)
            # print(instructionType)
            instructionL[PC].instruction = instructionfetch(instructionL[PC].instruction)
            instructionType = instructionL[PC].instruction.split(' ')[0]  # Takes first variable
            print(instructionType)
            if instructionType == "B":
                print("BBB")
                instructiondecode(instructionL[PC].instruction, instructionType)
                print(instructionList[PC-1].address)
                PC = PC - instructionList[PC-1].address - 4
                print(PC)
                #instructionList[PC-1].cyclenum = 0
                break
            instructionL[PC].cyclenum = instructionL[PC].cyclenum + 1
            #print(instructionL[PC].cyclenum)
            cyclecount = cyclecount +1
        if instructionL[PC-1].cyclenum == 1 and (PC - 1) > -1 and PC < len(instructionL):
            print("id")
            print(instructionL[PC-1].instruction)
            instructionType = instructionL[PC-1].instruction.split(' ')[0]  # Takes first variable
            instructiondecode(instructionL[PC - 1].instruction, instructionType)
            #print(instructionList[PC-1].immediate)
            instructionList[PC-1].type = instructionType
            if instructionList[PC -1].type == "B":
                PC = PC + 1
                instructionL[PC].cyclenum = instructionL[PC].cyclenum + 1
            instructionL[PC-1].cyclenum = instructionL[PC-1].cyclenum + 1
            cyclecount = cyclecount + 1
        if instructionL[PC-2].cyclenum == 2 and (PC - 2) > -1 and PC < len(instructionL):
            print("ex")
            print(instructionL[PC -2].instruction)
            if PC-3 > -1 and instructionList[PC -3].form == "D" and instructionList[PC -2].form == "R":
                print("d before ex")
                instructionList[PC-3].mem = RegFile[instructionList[PC-3].rn] + instructionList[PC-3].address
                #memory(instructionList[PC-3].mem, instructionList[PC-3].rt, (PC-3))
                RegFile[instructionList[PC-2].rm] = dataMemory[instructionList[PC - 3].mem]
                PC = (execute(instructionList[PC - 2], PC - 2)) + 2
            else:
                pipelineexe(PC - 2)
                PC = (execute(instructionList[PC-2], PC-2))+2

            #print(PC)
            #print(instructionList[PC-2].writebackvalue)
            instructionL[PC-2].cyclenum = instructionL[PC-2].cyclenum + 1
            cyclecount = cyclecount + 1
        if (PC - 3) > -1 and instructionL[PC-3].cyclenum == 3  and PC < len(instructionL):
            print("memory")
            print(instructionL[PC - 3].instruction)
            if instructionList[PC-3].form == "D":
                print("Dformat in while loop")
                pipelinemem(PC-3)
                memory(instructionList[PC-3].mem, instructionList[PC-3].rt, (PC-3))

            instructionL[PC-3].cyclenum = instructionL[PC-3].cyclenum + 1
            cyclecount = cyclecount + 1
        if (PC - 4) > -1 and instructionL[PC-4].cyclenum == 4 and  PC < len(instructionL) :
            print("writeback")
            print(instructionL[PC - 4].instruction)
            if instructionList[PC-4].form == "R":
                print("rformat in while loop")
                print(instructionList[PC-4].writebackvalue)
                writeback(instructionList[PC-4].rd, instructionList[PC-4].writebackvalue)
            elif instructionList[PC-4].form == "I":
                print("wb val" + str(instructionList[PC-4].writebackvalue))
                writeback(instructionList[PC-4].rd, instructionList[PC-4].writebackvalue)
            if instructionList[PC-4].form == "CBZ":
                if RegFile[instructionList[PC-4].rt] == 0:
                    print("Exiting loop")
                    print("CPI: " + str(cyclecount/instructioncount))
                    break
            #if instructionList[PC - 4].form == "B":
            instructionL[PC-4].cyclenum = 0
            cyclecount = cyclecount + 1

        print("At instruction: " + str(PC))
        print("regFile:")
        print(RegFile)
        print("Data memory:")
        print(dataMemory)
        print(PC)
        #increment PC for next instruction
        instructioncount = instructioncount + 1
        #print("CPI Stats: " + str(instructioncount) + ":" + str(cyclecount))
        PC = PC + 1

