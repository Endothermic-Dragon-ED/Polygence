import os
from glob import glob
import shutil

os.chdir(os.path.dirname(os.path.realpath(__file__)))

shutil.rmtree("build")

inputs = [y for x in os.walk("src") for y in glob(os.path.join(x[0], '*.txt'))]
SVGoutputs = [f"build{i[3:-3]}svg" for i in inputs]
PNGoutputs = [f"build{i[3:-3]}png" for i in inputs]

for i in range(len(inputs)):
    os.makedirs("/".join(SVGoutputs[i].split("\\")[:-1]), exist_ok=True)
    open(SVGoutputs[i],'a+').close()

    open(SVGoutputs[i],'a+').close()
    os.system(f"node render.js \"{inputs[i]}\" \"{SVGoutputs[i]}\"")
    os.system(f"inkscape \"{SVGoutputs[i]}\" -o \"{PNGoutputs[i]}\" -b #FFFFFF")
    os.remove(SVGoutputs[i])