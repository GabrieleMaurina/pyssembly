# pyssembly
A python assembly emulator.

### Install
`python -m pip install pyssembly`

### Usage
`python -m pyssembly <code.pys>`

### Instruction set

##### Comments
To comment a line write ';' at the beginning. For example:

`;this is a comment`

##### Labels
To label a line, to use it as destination in a jmp statement, simply write a single word in the line. For example:

`this-is-a-label`

##### Instructions
* `in a b`: print b to stdout, then read string from stdin and store it into a
* `out a b`: print a and b to stdout
* `mov a b`: store b into a
* `jmp a b`: if a, jump to b
* `bool a b`:
* `int a b`:
* `flt a b`:
* `str a b`:
* `add a b`:
* `sub a b`:
* `mul a b`:
* `div a b`:
* `pow a b`:
* `log a b`:
* `root a b`:
* `idiv a b`:
* `mod a b`:
* `eq a b`:
* `neq a b`:
* `les a b`:
* `leq a b`:
* `grt a b`:
* `vgeq a b`:
* `not a b`:
* `and a b`:
* `or a b`:
* `xor a b`:
* `nand a b`:
* `nor a b`:
* `nxor a b`:

### Future work

* Add arrays
* Add some string manipulation support
