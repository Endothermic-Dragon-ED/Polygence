import os
import matplotlib.pyplot as plt
import numpy as np

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def renderMinimaGraph():
    ax = plt.axes(projection='3d')

    def f(x, y):
        return (x**4+5*x**3+6*x**2-0.7)+y**2*2

    x = np.linspace(-2.8, 0.5, 25)
    y = np.linspace(-0.5, 1, 25)

    X, Y = np.meshgrid(x, y)

    Z = f(X, Y)

    ax.scatter([-2.593], [0], [-2.323], c="k")
    ax.scatter([-0], [0], [-0.7], c="r")
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none', zorder=10, alpha=0.7)
    ax.axis('off')
    ax.view_init(elev=46, azim=-129)
    plt.savefig("output/minima.png", bbox_inches='tight', dpi=130)
    plt.show()

def renderDeltaGraph():
    data = np.array([
        [2, 7],
        [3, 2]
    ])

    quadratic = [-8, 35, -31]

    inputs = np.linspace(1, 3.5, 1000)

    quadraticOutputs = quadratic[0]*inputs**2 + quadratic[1]*inputs + quadratic[2]

    plt.vlines(data.T[0], 0, data.T[1], "r", linestyle="dashed")
    plt.hlines(data.T[1], 0, data.T[0], "r", linestyle="dashed")
    plt.plot(inputs, quadraticOutputs, "k")
    plt.plot(*data.T, "ro")
    plt.axis([1, 3.5, 1, 8])
    plt.savefig("output/delta.png", bbox_inches='tight')
    plt.show()

def renderTangentGraph():
    linear = [-2, 8]
    quadratic = [-1, 4, -1]

    inputs = np.linspace(0, 4.5, 1000)

    linearOutputs = linear[0]*inputs + linear[1]
    quadraticOutputs = quadratic[0]*inputs**2 + quadratic[1]*inputs + quadratic[2]

    plt.plot(inputs, quadraticOutputs, "k")
    plt.plot(inputs, linearOutputs, "r")
    plt.axis([0, 4.5, -1, 4])
    plt.axis('off')
    plt.savefig("output/tangent.png", bbox_inches='tight')
    plt.show()
renderTangentGraph()