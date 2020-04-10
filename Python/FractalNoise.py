import noise as n
import png
import sys
import random as r
import math

def execute():
    #Arguments!
    #arg1 = Image Size
    #arg2 = Noise Scale
    #arg3 = Perturb_Level
    #arg4 = Perturb Scale
    #arg5 = Perturb Oct
    #arg6 = Perturb Persist
    #arg7 = Perturb Lac
    #arg8 = Save Loc
    #arg9 = Save Name
    #arg10 = Bit Depth

    args = sys.argv
    DATA = []
    f = open(args[8] + args[9], 'wb')
    if (int(args[10]) == 16):
        for x in range(0, int(args[1])):
            ROW_DATA = []
            for z in range(0, int(args[1])):
                ROW_DATA.append(round(getFractalData(x, z, float(args[2]), int(args[3]), float(args[4]), int(args[5]), float(args[6]), float(args[7])) * 65535))
            DATA.append(ROW_DATA)
    w = png.Writer(int(args[1]), int(args[1]), greyscale=True, bitdepth=16)
    w.write(f, DATA)
    f.close()

def getFractalData(x,z, n_scale, perturb_level, perturb_scale, perturb_octaves, perturb_persist, perturb_lac):
    fractal_basis = n.snoise2(x * (n_scale * perturb_scale), z * (n_scale * perturb_scale), perturb_octaves, perturb_persist, perturb_lac) * perturb_level
    out_noise = (n.snoise2((x + fractal_basis) * n_scale, (z + fractal_basis) * n_scale, 4, 0.5, 2.0) + 1) / 2
    return out_noise

execute()