# Pyssembly
##### A python assembly emulator.
This tool allows to execute pseudo assembly code and it is meant for teaching purposes.

### Install
`python -m pip install pyssembly`

### Usage
`python -m pyssembly <code.pys>`

### Examples
Examples are available in the examples folder.

Print the result of 137 * 2322:

1) create file `example.pys` containing:
```
mov a 137
mul a 2322
out a "\n"
```
2) run it with: `python -m pyssembly <example.pys>`
3) result: `318114`

### Comments
To comment a line write ';' at the beginning. For example:

`;this is a comment`

### Labels
To label a line, to use it as destination in a jmp statement, simply write a single word in the line. For example:

`this-is-a-label`

### Instruction set

##### General
* `in a b`: print b to stdout, read string from stdin, store it into a
* `out a b`: print a and b to stdout
* `mov a b`: store b into a
* `jmp a b`: if a, jump to b (b can be a label or a line number)

All conversions, math and boolean operations store the result in the first operand (a).

##### Conversions
* `bool a b`: boolean(b)
* `int a b`: integer(b)
* `flt a b`: float(b)
* `str a b`: string(b)

##### Arithmetic
* `add a b`: a + b
* `sub a b`: a - b
* `mul a b`: a * b
* `div a b`: a / b
* `pow a b`: a<sup>b</sup>
* `log a b`: log<sub>b</sub><sup>a</sup>
* `root a b`: a<sup>1/b</sup>
* `idiv a b`: a // b
* `mod a b`: a % b

##### Boolean
* `eq a b`: a == b
* `neq a b`: a != b
* `les a b`: a < b
* `leq a b`: a <= b
* `grt a b`: a > b
* `geq a b`: a >= b
* `not a b`: not b
* `and a b`: a and b
* `or a b`: a or b
* `xor a b`: a xor b
* `nand a b`: a nand b
* `nor a b`: a nor b
* `nxor a b`: a nxor b

### Future work

* Add arrays
* Add string manipulation
