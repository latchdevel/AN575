# Microchip PIC microcontrollers
Peripheral Interface Controller (PIC) micro chips are designed with a Harvard architecture with RISC (Reduced Instruction Set Computer) support by Microchip Technology in 1993, and are offered in various device families. The baseline and mid-range families use 8-bit wide data memory, and the high-end families use 16-bit data memory.

Instruction word sizes are 12 bits (PIC10 and PIC12), **14 bits (PIC16, PIC17 and PIC18)** and 24 bits (PIC24 and dsPIC). The binary representations of the machine instructions vary by family.

These devices feature a 14-bit wide code memory, and an improved 8 level deep call stack. The instruction set differs very little from the baseline devices, but the 2 additional opcode bits allow 128 registers and 2048 words of code to be directly addressed. There are a few additional miscellaneous instructions, and two additional 8-bit literal instructions, add and subtract. The mid-range core is available in the majority of devices labeled PIC16, PIC17 and PIC18.

Enhanced mid-range core devices introduce a deeper hardware stack, additional reset methods, 14 additional instructions and C programming language optimizations. In particular. there are two INDF registers (INDF0 and INDF1), and two corresponding FSR register pairs (FSRnL and FSRnH). Special instructions use FSRn registers like address registers, with a variety of addressing modes.

## PIC16
The first 32 bytes of the register space are allocated to special-purpose registers; the remaining 96 bytes are used for general-purpose RAM. If banked RAM is used, the high 16 registers (0x70–0x7F) are global, as are a few of the most important special-purpose registers, including the STATUS register, which holds the RAM bank select bits. (The other global registers are FSR and INDF, the low 8 bits of the program counter PCL, the PC high preload register PCLATH, and the master interrupt control register INTCON.)

The PCLATH register supplies high-order instruction address bits when the 8 bits supplied by a write to the PCL register, or the 11 bits supplied by a GOTO or CALL instruction, are not sufficient to address the available ROM space.

## PIC17
The PIC17 series never became popular and has been superseded by the PIC18 architecture (however, see clones below). The PIC17 series is not recommended for new designs, and availability may be limited to users.

Improvements over earlier cores are 16-bit wide opcodes (allowing many new instructions), and a 16-level deep call stack. PIC17 devices were produced in packages from 40 to 68 pins.

The PIC17 series introduced a number of important new features:

- a memory mapped accumulator
- read access to code memory (table reads)
- direct register-to-register moves (prior cores needed to move registers through the accumulator)
- an external program memory interface to expand the code space
- an 8-bit × 8-bit hardware multiplier
- a second indirect register pair
- auto-increment/auto-decrement addressing controlled by control bits in a status register (ALUSTA)

A significant limitation was that RAM space was limited to 256 bytes (26 bytes of special function registers, and 232 bytes of general-purpose RAM), with awkward bank-switching in the models that supported more.

## PIC18
The PIC18 series inherits most of the features and instructions of the PIC17 series, while adding a number of important new features:

- call stack is 21 bits wide and much deeper (31 levels deep)
- the call stack may be read and written (TOSU:TOSH:TOSL registers)
- conditional branch instructions
- indexed addressing mode (PLUSW)
- the FSR registers are extended to 12 bits, allowing them to linearly address the entire data address space
- the addition of another FSR register (bringing the number up to 3)

The RAM space is 12 bits, addressed using a 4-bit bank select register (BSR) and an 8-bit offset in each instruction. An additional "access" bit in each instruction selects between bank 0 (a=0) and the bank selected by the BSR (a=1).

A 1-level stack is also available for the STATUS, WREG and BSR registers. They are saved on every interrupt, and may be restored on return. If interrupts are disabled, they may also be used on subroutine call/return by setting the s bit (appending ", FAST" to the instruction).

The auto increment/decrement feature was improved by removing the control bits and adding four new indirect registers per FSR. Depending on which indirect file register is being accessed, it is possible to postdecrement, postincrement, or preincrement FSR; or form the effective address by adding W to FSR.

In more advanced PIC18 devices, an "extended mode" is available which makes the addressing even more favorable to compiled code:

a new offset addressing mode; some addresses which were relative to the access bank are now interpreted relative to the FSR2 register
the addition of several new instructions, notably for manipulating the FSR registers.
PIC18 devices are still developed (2023) and fitted with CIP (Core Independent Peripherals)
