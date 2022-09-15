import os
import matplotlib.pyplot as plt
import numpy as np

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def logLoss():
    fig, (ax1, ax2) = plt.subplots(ncols=2)

    inputs = np.linspace(0, 1, 1000)
    outputs = -np.log(1-inputs)

    ax1.plot(inputs, outputs, "k")
    ax1.axis([-0.1, 1.1, 0, 6])
    ax1.set_title(r"$-\log(1-x)$")
    
    inputs = np.linspace(0, 1, 1000)
    outputs = -np.log(inputs)

    ax2.plot(inputs, outputs, "k")
    ax2.axis([-0.1, 1.1, 0, 6])
    ax2.set_title(r"$-\log(x)$")

    plt.savefig("output/log-loss.png", bbox_inches='tight')
    plt.show()

def sigmoid():
    inputs = np.linspace(-7.5, 7.5, 1000)
    outputs = 1/(1+np.e**(-inputs))

    plt.figure(figsize=(6, 3.5))
    plt.plot(inputs, outputs, "k")
    plt.axis([-7.5, 7.5, 0, 1])
    plt.vlines(0, 0, 0.5, "r", linestyle="dashed")
    plt.hlines(0.5, -7.5, 0, "r", linestyle="dashed")
    plt.plot(0, 0.5, "ro")
    plt.savefig("output/sigmoid.png", bbox_inches='tight')
    plt.show()

# Render via running the appropriate function