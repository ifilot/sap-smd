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

.. list-table:: Parallel Control Lines
   :widths: 20, 20, 60
   :header-rows: 1

   * - Control line
     - Code
     - Description
   * - :code:`PCL0`
     - CODE000
     - Description for control line 0.
   * - :code:`PCL1`
     - CODE001
     - Description for control line 1.
   * - :code:`PCL2`
     - CODE002
     - Description for control line 2.
   * - :code:`PCL3`
     - CODE003
     - Description for control line 3.
   * - :code:`PCL4`
     - CODE004
     - Description for control line 4.
   * - :code:`PCL5`
     - CODE005
     - Description for control line 5.
   * - :code:`PCL6`
     - CODE006
     - Description for control line 6.
   * - :code:`PCL7`
     - CODE007
     - Description for control line 7.

.. list-table:: Orthogonal Control Lines A
   :widths: 20, 20, 60
   :header-rows: 1

   * - Control line
     - Code
     - Description
   * - :code:`OCA1`
     - CODE001
     - Description for control line 1.
   * - :code:`OCA2`
     - CODE002
     - Description for control line 2.
   * - :code:`OCA3`
     - CODE003
     - Description for control line 3.
   * - :code:`OCA4`
     - CODE004
     - Description for control line 4.
   * - :code:`OCA5`
     - CODE005
     - Description for control line 5.
   * - :code:`OCA6`
     - CODE006
     - Description for control line 6.
   * - :code:`OCA7`
     - CODE007
     - Description for control line 7.
   * - :code:`OCA8`
     - CODE008
     - Description for control line 8.
   * - :code:`OCA9`
     - CODE009
     - Description for control line 9.
   * - :code:`OCA10`
     - CODE010
     - Description for control line 10.
   * - :code:`OCA11`
     - CODE011
     - Description for control line 11.
   * - :code:`OCA12`
     - CODE012
     - Description for control line 12.
   * - :code:`OCA13`
     - CODE013
     - Description for control line 13.
   * - :code:`OCA14`
     - CODE014
     - Description for control line 14.
   * - :code:`OCA15`
     - CODE015
     - Description for control line 15.

.. list-table:: Orthogonal Control Lines B
   :widths: 20, 20, 60
   :header-rows: 1

   * - Control line
     - Code
     - Description
   * - :code:`OCB1`
     - CODE001
     - Description for control line 1.
   * - :code:`OCB2`
     - CODE002
     - Description for control line 2.
   * - :code:`OCB3`
     - CODE003
     - Description for control line 3.
   * - :code:`OCB4`
     - CODE004
     - Description for control line 4.
   * - :code:`OCB5`
     - CODE005
     - Description for control line 5.
   * - :code:`OCB6`
     - CODE006
     - Description for control line 6.
   * - :code:`OCB7`
     - CODE007
     - Description for control line 7.
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
