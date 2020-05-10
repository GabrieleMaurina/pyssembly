# pyssembly
A python assembly emulator.

### Install
`python -m pip install pyssembly`

### Usage
`python -m pyssembly \<code.pys\>`

### Instruction set

* ; comment line
* in a b: print b to stdout, then read string from stdin and store into a
* out a b: print a and b to stdout
* mov a b: store b into a
    'jmp': jmp,
    'bool': my_bool,
    'int': my_int,
    'flt': my_float,
    'str': my_string,
    'add': add,
    'sub': sub,
    'mul': mul,
    'div': div,
    'pow': my_pow,
    'log': my_log,
    'root': root,
    'idiv': idiv,
    'mod': mod,
    'eq': eq,
    'neq': neq,
    'les': les,
    'leq': leq,
    'grt': grt,
    'geq': geq,
    'not': my_not,
    'and': my_and,
    'or': my_or,
    'xor': xor,
    'nand': nand,
    'nor': nor,
    'nxor': nxor
