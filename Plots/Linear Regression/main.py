import os
import matplotlib.pyplot as plt
import numpy as np

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def renderBiasGraph():
    data = np.array([
        [1.304, 3.4],
        [3.07, 8.6],
        [5.65, 9.9],
        [6.76, 8.2],
        [6.93, 8.6],
        [7.38, 6.9],
        [0.796, 2.2],
        [8.84, 4.1]
    ])

    linearFit = [0.422714, 4.33536]
    quadraticFit = [-0.426608, 4.31644, -1.0898]
    sineFit = [10, np.pi/10]

    inputs = np.arange(0, 10, 0.1)

    linearOutputs = linearFit[0]*inputs + linearFit[1]
    quadraticOutputs = quadraticFit[0]*inputs**2 + quadraticFit[1]*inputs + quadraticFit[2]
    sineOutputs = sineFit[0]*np.sin(sineFit[1]*inputs)

    plt.plot(*data.T, "kx")
    plt.plot(inputs, linearOutputs, "b")
    plt.plot(inputs, quadraticOutputs, "r")
    plt.plot(inputs, sineOutputs, "g")
    plt.axis([0, 10, 0, 11])
    plt.axis('off')
    plt.savefig("output/bias.png", bbox_inches='tight')
    plt.show()

renderBiasGraph()