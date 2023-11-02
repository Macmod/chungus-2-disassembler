from nbt import nbt
from formats import *
from utils import *
import argparse
import sys

def get_coords(bit, instruction):
    x = 4 * (instruction // 16)
    if bit > 7 and instruction % 32 < 16:
        x += 2
    if bit < 8 and instruction % 32 > 15:
        x += 2
    y = 15 - ((2 * bit) % 16 + (1 if instruction % 2 == 0 else 0))
    z = 30 - (2 * (instruction % 16))

    return (x, y, z)

def get_block_pos(x, y, z):
    return x + 63 * z + 31 * 63 * y

def blocks_to_machine_code(basedata, blockentities):
    assembly = ['0000000000000000']*1024
    ss_from_barrels = {
        tuple(entity["Pos"].value): (i, len(entity["Items"].tags))
        for i, entity in enumerate(blockentities.tags)
    }

    def get_ss_from_barrel(pos):
        if tuple(pos) in ss_from_barrels:
            count = ss_from_barrels[tuple(pos)][1]
            if count == 27:
                return 14
            else:
                return (count*14) // 27 + 1 if count != 0 else 0

        return 0

    for instruction in range(256):
        for bit in range(16):
            x, y, z = get_coords(bit, instruction)           
            absolute = get_block_pos(x, y, z)

            if basedata[absolute] == 2 or basedata[absolute] == 3:
                ss = get_ss_from_barrel([x, y, z])

                inv_ss = bin(15 - ss)[2:].zfill(4)
                for i in range(4):
                    idx = 64 * (instruction // 16) + instruction % 16 + 16 * i
                    assembly[idx] = list(assembly[idx])
                    assembly[idx][bit] = inv_ss[-i-1]
                    assembly[idx] = ''.join(assembly[idx])

    return assembly

def disassemble_line(binary_line, formats_dict):
    """Disassemble a given binary line based on the provided formats dictionary."""
    for mnemonic, format_tuple in formats_dict.items():
        idx = 0
        match = True
        operands = []

        for segment in format_tuple:
            if segment == "OPERAND":
                segment_length = 3
            elif segment.startswith("IMM_"):
                segment_length = int(segment.split("_")[1])
            elif segment == "REG":
                segment_length = 5
            elif segment == "BITS":
                if mnemonic == 'STS':
                    segment_length = 3
                elif mnemonic == 'SST':
                    segment_length = 1
                else:
                    segment_length = 2
            else:
                segment_length = len(segment)

            segment_value = binary_line[idx:idx+segment_length]

            if segment == segment_value:
                idx += segment_length
                continue
            elif segment in ["BITS", "IMM_11", "IMM_8", "IMM_5", "IMM_6", "IMM_3", "REG", "OPERAND"]:
                operands.append(segment_value)
                idx += segment_length
            else:
                match = False
                break

        if match:
            return mnemonic, operands

    # Note: there should maybe be a "best match"
    #       logic here to handle corrupted files

    # If no match is found, return None
    return None, None

def disassemble(binary_lines):
    disassembled_output = [disassemble_line(line, FORMATS) for line in binary_lines]
    return disassembled_output

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('inputfile', help='Input CHUNGUS2 NBT file (.schem)')
    parser.add_argument('-nc','--no-comments', action='store_true', default=False)
    parser.add_argument('-ln','--line-numbers', action='store_true', default=False)
    args = parser.parse_args()

    rom = nbt.NBTFile(args.inputfile, "rb")

    blockentities = rom['BlockEntities']
    basedata = rom['BlockData']

    assembly = blocks_to_machine_code(basedata, blockentities)

    assembly = strip_nops(assembly)

    for idx, code in enumerate(disassemble(assembly)):
        mnemonic, operands = code
        text = format_instruction(mnemonic, operands, comments=not args.no_comments)
        if args.line_numbers:
            print(str(idx)+'\t'+text)
        else:
            print(text)
