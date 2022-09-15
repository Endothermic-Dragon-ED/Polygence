import os
import matplotlib.pyplot as plt
import numpy as np

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def renderBiasGraph():
    data = np.array([
        [0.796, 2.2],
        [1.304, 3.4],
        [3.07, 8.6],
        [5.65, 9.9],
        [6.76, 8.2],
        [6.93, 8.6],
        [7.38, 6.9],
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

def renderVarianceGraph():
    data = np.array([
        [1.04, 3.42],
        [3.71, 3.68],
        [5.15, 2.65],
        [7.42, 3.16],
        [9.63, 5.14],
        [12.17, 4.69],
        [14.24, 6.55],
        [16.3, 7.61],
        [18.27, 7.02]
    ])

    quadraticFit = [0.0144182, -0.00572898, 3.11042]
    eighthFit = [0.00000400708, -0.000305728, 0.00961241, -0.160818, 1.54259, -8.51759, 25.7954, -37.964, 22.9627]

    inputs = np.arange(0, 20, 0.1)

    quadraticOutputs = np.sum([quadraticFit[i]*inputs**(2-i) for i in range(len(quadraticFit))], 0)
    eighthOutputs = np.sum([eighthFit[i]*inputs**(8-i) for i in range(len(eighthFit))], 0)

    plt.plot(*data.T, "kx")
    plt.plot(inputs, quadraticOutputs, "b")
    plt.plot(inputs, eighthOutputs, "r")
    plt.axis([0, 20, 0, 15])
    plt.axis('off')
    plt.savefig("output/variance.png", bbox_inches='tight')
    plt.show()

# Render via running the appropriate function