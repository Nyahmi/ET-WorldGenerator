import noise as n
import png
import sys

def execute():
    #Arguments!
    #arg1 = Image Size
    #arg2 = Noise Scale
    #arg3 = Noise Oct
    #arg4 = Noise Persist
    #arg5 = Noise Lacunarity
    #arg6 = Save Loc
    #arg7 = Save Name

    args = sys.argv
    DATA = []
    for x in range(0, int(args[1])):
        ROW_DATA = []
        ROW_DATA.extend(range(0,int(args[1])))
        for z in range(0, int(args[1])):
            ROW_DATA[z] = (n.snoise2(x * float(args[2]), z * float(args[2]),
                                     int(args[3]), float(args[4]), float(args[5]), int(args[1]), int(args[1]), 0) * 128) + 127
        DATA.append(ROW_DATA)
    png.from_array(DATA, 'L').save(args[6] + args[7])

execute()