.. _instruction_decoder:
.. index:: Instruction Decoder

Instruction decoder
===================

The instruction decoder is reponsible for mapping a machine instruction together
with the t-state counter to the control lines, effectively tying a set of
microinstructions to a given machine instruction. The instruction decoder in the
SAM-SMD uses two :code:`SST39SF010` EEPROMS for this mapping. One of the EEPROMS
directs 8 parallel control lines, which are lines that can be pulled high or low
in any particular combination. The second EEPROM is tied to four :code:`74HC238`
which control 2 x 15 orthogonal control lines. Orthogonal control lines are such
that only one of the 15 lines can be activated at one time. This limitation
comes with the benefit that a single chip can control far more control lines,
here 30 instead of 8. Note that the 2 x 15 orthogonal control lines form two
sets, i.e. any control line in one set **can** be activated together with any
other control line in the other set. The only limitation is thus that **within**
a set, no two control lines can be activated simultaneously.

Mapping
-------

.. note::
   In the tables below, we use the following abbreviations:
   * ALU: Arithmetic and Logic Unit
   * IR: Instrucion Register
   * MAR: Memory Address Register
   * PC: Program Counter

.. list-table:: Parallel Control Lines
   :widths: 20, 20, 60
   :header-rows: 1

   * - Control line
     - Micro-instruction
     - Description
   * - :code:`PCL0`
     - :code:`CE`
     - PC count enable
   * - :code:`PCL1`
     - :code:`FI`
     - ALU flag register in
   * - :code:`PCL2`
     - :code:`SU`
     - ALU subtract operation
   * - :code:`PCL3`
     - :code:`X`
     - Unused
   * - :code:`PCL4`
     - :code:`X`
     - Unused
   * - :code:`PCL5`
     - :code:`X`
     - Unused
   * - :code:`PCL6`
     - :code:`HLT`
     - Halts the clock line
   * - :code:`PCL7`
     - :code:`/MR`
     - Used internally to reset T-state counter

.. list-table:: Orthogonal Control Lines A
   :widths: 20, 20, 60
   :header-rows: 1

   * - Control line
     - Micro-instruction
     - Description
   * - :code:`OCA1`
     - :code:`MI`
     - MAR in: Retrieves memory address from data bus
   * - :code:`OCA2`
     - :code:`II`
     - IR in: Retrieves instruction from data bus
   * - :code:`OCA3`
     - :code:`J`
     - PC jump: Retrieves address from data bus
   * - :code:`OCA4`
     - :code:`AI`
     - A-register in: Stores value from data bus
   * - :code:`OCA5`
     - :code:`BI`
     - B-register in: Stores value from data bus
   * - :code:`OCA6`
     - :code:`OI`
     - Output register in: Retrieves value from data bus
   * - :code:`OCA7`
     - :code:`RI`
     - RAM in: Stores value from data bus in memory
   * - :code:`OCA8`
     - :code:`TI`
     - T-register in: Stores value from data bus
   * - :code:`OCA9`
     - :code:`X`
     - Unused
   * - :code:`OCA10`
     - :code:`X`
     - Unused
   * - :code:`OCA11`
     - :code:`X`
     - Unused
   * - :code:`OCA12`
     - :code:`X`
     - Unused
   * - :code:`OCA13`
     - :code:`X`
     - Unused
   * - :code:`OCA14`
     - :code:`X`
     - Unused
   * - :code:`OCA15`
     - :code:`X`
     - Unused

.. list-table:: Orthogonal Control Lines B
   :widths: 20, 20, 60
   :header-rows: 1

   * - Control line
     - Micro-instruction
     - Description
   * - :code:`OCB1`
     - :code:`CO`
     - PC counter out: Asserts current PC value on data bus
   * - :code:`OCB2`
     - :code:`RRO`
     - ROM out: Asserts ROM value onto data bus
   * - :code:`OCB3`
     - :code:`AO`
     - A-register out: Asserts register value onto data bus
   * - :code:`OCB4`
     - :code:`BO`
     - B-register out: Asserts register value onto data bus
   * - :code:`OCB5`
     - :code:`EO`
     - ALU sum out: Asserts result of summation onto data bus
   * - :code:`OCB6`
     - :code:`RO`
     - RAM out: Asserts RAM value onto data bus
   * - :code:`OCB7`
     - :code:`TO`
     - T-register: Asserts register value onto data bus
   * - :code:`OCB8`
     - :code:`X`
     - Unused
   * - :code:`OCB9`
     - :code:`X`
     - Unused
   * - :code:`OCB10`
     - :code:`X`
     - Unused
   * - :code:`OCB11`
     - :code:`X`
     - Unused
   * - :code:`OCB12`
     - :code:`X`
     - Unused
   * - :code:`OCB13`
     - :code:`X`
     - Unused
   * - :code:`OCB14`
     - :code:`X`
     - Unused
   * - :code:`OCB15`
     - :code:`X`
     - Unused

Machine instructions
--------------------

Upon receiving a new machine instruction, a t-state counter is executed that
loops over a number of microinstructions. Below, a table is provided showing
the sequence of microinstructions that are executed per machine instruction
and per t-state. A secondary table provides an explanation what each machine
code instruction (opt code) does.

.. note::
  Despite that the t-state counter allows for up to 20 microinstructions, 
  typically far fewer such microinstructions are needed.

.. list-table:: Microinstructions per t-state and per machine instruction
   :header-rows: 1

   * - Instruction
     - State 0
     - State 1
     - State 2
     - State 3
     - State 4
     - State 5
     - State 6
   * - :code:`NOP`
     - :code:`CO | MI`
     - :code:`RRO | II | CE`
     - :code:`RT`
     - 
     - 
     - 
     - 
   * - :code:`JP`
     - :code:`CO | MI`
     - :code:`RRO | II | CE`
     - :code:`CO | MI`
     - :code:`RRO | J`
     - :code:`RT`
     - 
     - 
   * - :code:`LDA`
     - :code:`CO | MI`
     - :code:`RRO | II | CE`
     - :code:`CO | MI`
     - :code:`RRO | AI | CE`
     - :code:`RT`
     - 
     - 
   * - :code:`LDB`
     - :code:`CO | MI`
     - :code:`RRO | II | CE`
     - :code:`CO | MI`
     - :code:`RRO | BI | CE`
     - :code:`RT`
     - 
     - 
   * - :code:`ADD`
     - :code:`CO | MI`
     - :code:`RRO | II | CE`
     - :code:`0`
     - :code:`EO | TI | FI`
     - :code:`TO | AI`
     - :code:`RT`
     - 
   * - :code:`TAB`
     - :code:`CO | MI`
     - :code:`RRO | II | CE`
     - :code:`AO | BI`
     - :code:`RT`
     - 
     - 
     - 
   * - :code:`TBA`
     - :code:`CO | MI`
     - :code:`RRO | II | CE`
     - :code:`BO | AI`
     - :code:`RT`
     - 
     - 
     - 
   * - :code:`TAO`
     - :code:`CO | MI`
     - :code:`RRO | II | CE`
     - :code:`AO | OI`
     - :code:`RT`
     - 
     - 
     - 
   * - :code:`STA`
     - :code:`CO | MI`
     - :code:`RRO | II | CE`
     - :code:`CO | MI`
     - :code:`RRO | TI`
     - :code:`TO | MI`
     - :code:`RI | AO | CE`
     - :code:`RT`
   * - :code:`LRA`
     - :code:`CO | MI`
     - :code:`RRO | II | CE`
     - :code:`CO | MI`
     - :code:`RRO | TI`
     - :code:`TO | MI`
     - :code:`RO | AI | CE`
     - :code:`RT`
   * - :code:`STB`
     - :code:`CO | MI`
     - :code:`RRO | II | CE`
     - :code:`CO | MI`
     - :code:`RRO | TI`
     - :code:`TO | MI`
     - :code:`RI | BO | CE`
     - :code:`RT`
   * - :code:`LRB`
     - :code:`CO | MI`
     - :code:`RRO | II | CE`
     - :code:`CO | MI`
     - :code:`RRO | TI`
     - :code:`TO | MI`
     - :code:`RO | BI | CE`
     - :code:`RT`

.. list-table:: Explanation of every opt code
   :header-rows: 1

   * - Instruction
     - Bytes
     - Description
   * - :code:`NOP`
     - 1
     - Do nothing
   * - :code:`JP <ADDR>`
     - 2
     - Jump to memory address
   * - :code:`LDA <VAL>`
     - 2
     - Immediate load into register A
   * - :code:`LDB <VAL>`
     - 2
     - Immediate load into register B
   * - :code:`ADD`
     - 1
     - Add A+B and store in A (will overwrite)
   * - :code:`TAB`
     - 1
     - Transfer contents of A to B
   * - :code:`TBA`
     - 1
     - Transfer contents of B to A
   * - :code:`TAO`
     - 1
     - Transfer contents of A to Output
   * - :code:`STA <ADDR>`
     - 2
     - Store A in RAM at address
   * - :code:`LRA <ADDR>`
     - 2
     - Load A from RAM
   * - :code:`STB <ADDR>`
     - 2
     - Store B in RAM at address
   * - :code:`LRB <ADDR>`
     - 2
     - Load B from RAM