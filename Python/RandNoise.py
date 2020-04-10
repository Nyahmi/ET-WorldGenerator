import noise as n
import png
import sys
import random as r

def execute():
    #Arguments!
    #arg1 = Image Size
    #arg2 = Save Loc
    #arg3 = Save Name
    #arg4 = Bit Depth

    args = sys.argv
    DATA = []
    f = open(args[2] + args[3], 'wb')
    if (int(args[4]) == 16):
        for x in range(0, int(args[1])):
            ROW_DATA = []
            for z in range(0, int(args[1])):
                ROW_DATA.append(round(r.randrange(0, 65536)))
            DATA.append(ROW_DATA)
    w = png.Writer(int(args[1]), int(args[1]), greyscale=True, bitdepth=16)
    w.write(f, DATA)
    f.close()
execute()