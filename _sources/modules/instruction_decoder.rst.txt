.. _instruction_decoder:
.. index:: Instruction Decoder

Instruction decoder
===================

The instruction decoder is reponsible for mapping a machine instruction together
with the t-state counter to the control lines. The instruction decoder in the
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
     - CODE008
     - Description for control line 8.
   * - :code:`OCB9`
     - CODE009
     - Description for control line 9.
   * - :code:`OCB10`
     - CODE010
     - Description for control line 10.
   * - :code:`OCB11`
     - CODE011
     - Description for control line 11.
   * - :code:`OCB12`
     - CODE012
     - Description for control line 12.
   * - :code:`OCB13`
     - CODE013
     - Description for control line 13.
   * - :code:`OCB14`
     - CODE014
     - Description for control line 14.
   * - :code:`OCB15`
     - CODE015
     - Description for control line 15.
