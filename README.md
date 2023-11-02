# CHUNGUS2 Disassembler

Disassembler for the [CHUNGUS 2 Minecraft CPU](https://www.youtube.com/watch?v=FDiapbD0Xfg&t=27s).

![](res/chungus2.jpg)

The assembler can be found in the original repository [sammyuri/chungus-2-assembler](https://github.com/sammyuri/chungus-2-assembler).

Usage:
```
$ python3 disassembler.py <SCHEM file>
```

By default it will produce the disassembly into `stdout` with comments enabled. To disable comments just add `-nc` or `--no-comments`.
To get the disassembly with line numbers add `-ln` or `--line-numbers`.

# Notes

Special thanks to the organizers of BoitaTech CTF that created a challenge that involved disassembling CHUNGUS2; otherwise this would probably never be written :P

# Contribute

This code is very experimental and may have lots of bugs. Feel free to contribute with a [pull request](https://github.com/Macmod/chungus-2-disassembler/pulls) =)

# License

MIT License

Copyright (c) 2023 Artur Henrique Marzano Gonzaga

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
