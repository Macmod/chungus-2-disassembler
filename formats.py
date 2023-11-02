SCREEN = {
    64: 'Load x1',
    65: 'Load y1',
    66: 'Load x2',
    67: 'Load y2',
    68: 'Clear screen',
    69: 'Buffer screen',
    70: 'Clear char display',
    71: 'Load pixel',
    72: 'Write character 1',
    73: 'Write character 2',
    74: 'Toggle integer display 1',
    75: 'Toggle integer display 2',
    76: 'Display signed integer 1',
    77: 'Display signed integer 2',
    78: 'Display unsigned integer 1',
    79: 'Display unsigned integer 2',
    80: 'Draw pixel',
    81: 'Draw rectangle',
    82: 'Draw pixel + load x1',
    83: 'Draw pixel + load y1',
    84: 'Draw rectangle + load x1',
    85: 'Draw rectangle + load y1',
    86: 'Draw rectangle + load x2',
    87: 'Draw rectangle + load y2',
    88: 'Erase pixel',
    89: 'Erase rectangle',
    90: 'Erase pixel + load x1',
    91: 'Erase pixel + load y1',
    92: 'Erase rectangle + load x1',
    93: 'Erase rectangle + load y1',
    94: 'Erase rectangle + load x2',
    95: 'Erase rectangle + load y2',
    96: 'Load byte 1',
    104: 'Load byte 2',
    112: 'Draw sprite'
}

FORMATS = {
    "NOP": ("00000", "00000000000"),
    "HLT": ("00001", "00000000000"),
    "STS": ("00010", "BITS", "IMM_8"),
    "CLI": ("00011", "REG", "OPERAND", "IMM_5"),
    "JMP": ("00100", "IMM_11"),
    "CAL": ("00101", "IMM_11"),
    "RET": ("00110", "00000000000"),
    "BRH": ("00111", "OPERAND", "BITS", "IMM_6"),
    "SST": ("01000", "00", "BITS", "00000", "REG"),
    "SLD": ("01001", "REG", "00000", "OPERAND"),
    "PST": ("01010", "REG", "IMM_8"),
    "PLD": ("01011", "REG", "IMM_8"),
    "PSH": ("01100", "REG", "BITS", "IMM_6"),
    "POP": ("01101", "REG", "BITS", "IMM_6"),
    "MST": ("01110", "REG", "IMM_8"),
    "MLD": ("01111", "REG", "IMM_8"),
    "LIM": ("10000", "REG", "IMM_8"),
    "AIM": ("10001", "REG", "IMM_8"),
    "CMP": ("10010", "REG", "IMM_8"),
    "CMA": ("10011", "REG", "IMM_8"),
    "MOV": ("10100", "REG", "REG", "00000"),
    "ADD": ("10101", "REG", "REG", "BITS", "REG"),
    "SUB": ("10110", "REG", "REG", "BITS", "REG"),
    "ADI": ("10111", "REG", "REG", "IMM_5"),
    "BIT": ("11000", "REG", "REG", "BITS", "REG"),
    "BNT": ("11001", "REG", "REG", "BITS", "REG"),
    "SHF": ("11010", "REG", "REG", "BITS", "REG"),
    "SFI": ("11011", "REG", "REG", "BITS", "IMM_3"),
    "MUL": ("11100", "REG", "REG", "BITS", "REG"),
    # unused opcode,
    # unused opcode,
    "BCT": ("11111", "REG", "REG", "BITS", "REG"),
}

OPERANDS = {
    # branch conditions
    "TRUE": "000",   "ALWAYS": "000",
    "EVEN": "001",
    "HIGHER": "010", "GRTR": "010",      "GREATER": "010",
    "LESS": "011",   "LOWER": "011",     "NCARRY": "011",
    "ZERO": "100",   "EQUAL": "100",
    "NZERO": "101",  "NEQUAL": "101",
    "GRTREQ": "110", "HIGHEREQ": "110",  "CARRY": "110",
    "LESSEQ": "111", "LOWEREQ": "111",
    # special registers
    "BRANCH": "001",
    "PCUPPER": "010",
    "PCLOWER": "011",
    "FLAGS": "100",
    "SP": "101",
    "POI": "110",    "POINTER": "110",   "MAR": "110",
    "LOOP": "111",   "LPOI": "111",
}

# if not in alias, assume same opcode
ALIAS = {
    "ABC": "STS",  "FNU": "STS",  "LOOPCNT": "STS", "LOOPSRC": "STS",
    "SSP": "STS",
    "BRN": "BRH",  "BRT": "BRH",
    "POI": "SST",  "EPOI": "SST",
    "PSHU": "PSH", "DSP": "PSH",
    "POPU": "POP", "ISP": "POP",
    "ADDC": "ADD", "ADDV": "ADD", "ADDVC": "ADD",
    "SUBC": "SUB", "SUBC": "SUB", "SUBVC": "SUB",
    "IMP": "BIT",  "XOR": "BIT",  "AND": "BIT",     "OR": "BIT",
    "NIMP": "BNT", "XNOR": "BNT", "NAND": "BNT",    "NOR": "BNT",
    "BSL": "SHF",  "BSR": "SHF",  "ROT": "SHF",     "SXTSR": "SHF",
    "BSLI": "SFI", "BSRI": "SFI", "ROTI": "SFI",    "SXTSRI": "SFI",
    "MULU": "MUL", "DIV": "MUL",  "MOD": "MUL",
    "SQRT": "BCT", "LZR": "BCT",  "TZR": "BCT",
}

BITS = {
    # settings
    "ABC": "000", "FNU": "001", "LOOPCNT": "010", "LOOPSRC": "011",
    "SSP": "100",
    "POI": "0",   "EPOI": "1",
    # branch aliases
    "BRH": "00",  "BRN": "00",  "BRT": "10",
    # stack
    "PSH": "00",  "PSHU": "10", "DSP": "01",
    "POP": "00",  "POPU": "10", "ISP": "01",
    # alu ops
    "ADD": "00",  "ADDC": "01", "ADDV": "10",     "ADDVC": "11",
    "SUB": "00",  "SUBC": "01", "SUBV": "10",     "SUBVC": "11",
    "IMP": "00",  "XOR": "01",  "AND": "10",      "OR": "11",
    "NIMP": "00", "XNOR": "01", "NAND": "10",     "NOR": "11",
    "BSL": "00",  "BSR": "01",  "ROT": "10",      "SXTSR": "11",
    "BSLI": "00", "BSRI": "01", "ROTI": "10",     "SXTSRI": "11",
    "MUL": "00",  "MULU": "01", "DIV": "10",      "MOD": "11",
    "SQRT": "00", "BCT": "11",  "LZR": "01",      "TZR": "10",
}

STS_FLAGS = [
    'Use alternate branch conditions',
    'Force flags to not update',
    'Set loop counter',
    'Set loop source',
    'Set stack pointer to immediate',
    'unused',
    'unused',
    'unused',
]

COMP_FLAGS = [
    '== True',
    '== Even',
    '>=', # might be wrong?
    '<=', # might be wrong?
    '== 0 (Equal)',
    '!= 0 (Not Equal)',
    '>', # might be wrong?
    '<' # might be wrong?
]

def R(x): return 'R' + str(int(x, 2))

def B(x, k=8): return '0b' + x.zfill(k) 

def I(x): return str(int(x, 2))

def format_instruction(mnemonic, operands, comments=True):
    rawops = ''.join(operands).zfill(11)

    if mnemonic in ALIAS:
        mnemonic = mnemonic[ALIAS]

    text = f'{mnemonic}'
    if mnemonic in ('NOP', 'HLT', 'RET'):
        pass
    elif mnemonic in ('MST','MLD','LIM','AIM','CMP','CMA'):
        text += f' {R(rawops[:3])}, {I(rawops[3:])}'
    elif mnemonic in ('ADD','SUB','BIT','BNT','SHF','MUL','UDH'):
        text += f' {R(rawops[:3])}, {R(rawops[3:6])}, {B(rawops[6:8],2)}, {R(rawops[8:])}'
    elif mnemonic in ('SFI', 'BCT'):
        text += f' {R(rawops[:3])}, {R(rawops[3:6])}, {B(rawops[6:8],2)}, {I(rawops[8:])}'
    elif mnemonic in ('PSH', 'POP'):
        text += f' {R(rawops[:3])}, {B(rawops[4], 1)}, {B(rawops[5], 1)}, {B(rawops[6:], 6)}'
    elif mnemonic in ('CAL', 'JMP'):
        text += f' {I(rawops)}'
    elif mnemonic == 'MOV':
        text += f' {R(rawops[:3])}, {R(rawops[3:6])}'
    elif mnemonic == 'PST':
        key = int(rawops[3:], 2)
        if comments and key in SCREEN:
            text += f' {R(rawops[:3])} {I(rawops[3:])} ; {SCREEN[key]}'
        else:
            text += f' {R(rawops[:3])} {I(rawops[3:])}'
    elif mnemonic == 'ADI':
        text += f' {R(rawops[:3])}, {R(rawops[3:6])}, {I(rawops[6:])}'
    elif mnemonic == 'PLD':
        text += f' {R(rawops[:3])}, {I(rawops[3:8])}'
    elif mnemonic == 'SST':
        text += f' {rawops[2]}, {R(rawops[8:])}'
    elif mnemonic == 'CLI':
        text += f' {R(rawops[:3])}, {B(rawops[3:6])}, {I(rawops[6:])}'
    elif mnemonic == 'BRH':
        if comments:
            text += f' {B(rawops[:3],3)}, {B(rawops[4],1)}, {I(rawops[5:])} ; {COMP_FLAGS[int(rawops[:3],2)]}'
        else:
            text += f' {B(rawops[:3],3)}, {B(rawops[4],1)}, {I(rawops[5:])}'
    elif mnemonic == 'SLD':
        text += f' {R(rawops[:3])}, {B(rawops[8:])}'
    else:
        text = f' {mnemonic} {", ".join(operands)}'

    return text
