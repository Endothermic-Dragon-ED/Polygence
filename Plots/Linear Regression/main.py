import os
import matplotlib.pyplot as plt
import numpy as np

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()

plt.rcParams.update({"text.usetex": True})

fig, ax = plt.subplots(1,1)
data=[[360000,1235,3],
      [1195000,3407,5],
      [529990,2017,3],
      [599900,2943,5],
      [2865000,4497,5],
      [r"$\vdots$",r"$\vdots$",r"$\vdots$"]]
column_labels=["Price (\\$)", "Square Footage", "Bedrooms"]
ax.axis('tight')
ax.axis('off')
ax.table(cellText=data,colLabels=column_labels,loc="center")

plt.show()