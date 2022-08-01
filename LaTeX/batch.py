import os
from glob import glob
import shutil
import re

os.chdir(os.path.dirname(os.path.realpath(__file__)))

sourceSubDir = "Gradient Descent"

try:
    shutil.rmtree("build" + (f"/{sourceSubDir}" if sourceSubDir else ""))
except Exception:
    print("Folder not found, continuing...")

inputs = [y for x in os.walk("src" + (f"/{sourceSubDir}" if sourceSubDir else "")) for y in glob(os.path.join(x[0], '*.tex'))]
SVGoutputs = [f"build{i[3:-3]}svg" for i in inputs]
PNGoutputs = [f"build{i[3:-3]}png" for i in inputs]

for i in range(len(inputs)):
    os.makedirs("/".join(re.split(r"[\\/]", SVGoutputs[i])[:-1]), exist_ok=True)
    open(SVGoutputs[i],'a+').close()

    open(SVGoutputs[i],'a+').close()
    os.system(f"node render.js \"{inputs[i]}\" \"{SVGoutputs[i]}\"")
    os.system(f"inkscape \"{SVGoutputs[i]}\" -o \"{PNGoutputs[i]}\" -b #FFFFFF")
    os.remove(SVGoutputs[i])