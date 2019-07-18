//code to implement the processor
//

//read in all of the intrsuctions

int PC = 0;
int state = 1;

//fetch from the instruction && increment PC state ==1
switch (state)
{
    case 1:
        //fetch instruction
        PC = PC + 4;
        state = 2;
        break;
    case 2: 
        //instruction decode
        //register fetch
        //compute brancg address
        break;
    case 3:
        //load-store instruction
        //ALU execturion
        //branch completion
        break;
    case 4:
        
    default:
        break;
}(state)
1.    
PC = PC + 4;
    state = 2;
    

//contain a register file (read/write reg values)

//decode instruction, parse
//opcode[32:24/23]



//contain a data memory (loads/stores)

//output the instruction memory, value sin reg files, and data memory defore each smulation

//output the values in the register file and data memory after each simulation