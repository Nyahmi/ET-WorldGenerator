import noise as n
import png
import sys
import random as r
import math

def execute():
    #Arguments!
    #arg1 = Image Size
    #arg2 = Cell Scale
    #arg3 = Cell Perturb
    #arg4 = Save Loc
    #arg5 = Save Name
    #arg6 = Bit Depth

    args = sys.argv
    DATA = []
    f = open(args[4] + args[5], 'wb')
    if (int(args[6]) == 16):
        for x in range(0, int(args[1])):
            ROW_DATA = []
            for z in range(0, int(args[1])):
                ROW_DATA.append(round(getCellData(x, z, float(args[2])) * 65535))
            DATA.append(ROW_DATA)
    w = png.Writer(int(args[1]), int(args[1]), greyscale=True, bitdepth=16)
    w.write(f, DATA)
    f.close()

def getCellData(x,z, cell_scale):
    return -(math.sqrt(((math.sin(x * cell_scale)) + (math.sin(z * cell_scale))) + 2) / 2) + 1

execute()