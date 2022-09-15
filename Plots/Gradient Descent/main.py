import os
import matplotlib.pyplot as plt
import numpy as np

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def renderMinimaGraph():
    ax = plt.axes(projection='3d')

    def f(x, y):
        return (x**4+5*x**3+6*x**2-0.7)+y**2*2

    x = np.linspace(-2.8, 0.5, 50)
    y = np.linspace(-0.5, 1, 50)

    X, Y = np.meshgrid(x, y)

    Z = f(X, Y)

    ax.scatter([-2.593], [0], [-2.323], c="k")
    ax.scatter([0], [0], [-0.7], c="r")
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none', zorder=10, alpha=0.7)
    ax.view_init(elev=46, azim=-129)
    ax.set_xlabel("x", labelpad=-12.5)
    ax.set_ylabel("y", labelpad=-12.5)
    ax.set_zlabel("z", labelpad=-12.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
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

def renderSaddlePoint():
    ax = plt.axes(projection='3d')

    def f(x, y):
        return x**2 - y**2

    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)

    X, Y = np.meshgrid(x, y)

    Z = f(X, Y)

    ax.scatter([0], [0], [0], c="k")
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none', zorder=10, alpha=0.7)
    ax.view_init(elev=33, azim=-125)
    ax.set_xlabel("x", labelpad=-12.5)
    ax.set_ylabel("y", labelpad=-12.5)
    ax.set_zlabel("z", labelpad=-12.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    plt.savefig("output/saddle.png", bbox_inches='tight', dpi=130)
    plt.show()

def renderCusp():
    inputs = np.linspace(-3, 3, 1000)

    outputs = np.abs(inputs)

    plt.figure(figsize=(6.4*2/3, 4.8*2/3))
    plt.plot(inputs, outputs, "k", linewidth=7.5, solid_capstyle='round', zorder=1)
    plt.scatter([0], [0], s=1000, facecolors='none', edgecolors='r', zorder=2, linewidths=4)
    plt.axis([-3.1, 3.1, -0.5, 3.1])
    plt.axis('off')
    plt.savefig("output/cusp.png", bbox_inches='tight')
    plt.show()

def renderQuadratic():
    inputs = np.linspace(-5, 5, 1000)

    outputs = inputs**2

    tangentLine = inputs*6 - 9

    plt.figure(figsize=(6.4*2/3, 4.8*2/3))
    plt.plot(inputs, outputs, "k")
    plt.plot(inputs, tangentLine, "r")
    plt.axis([-5, 5, -0.1, 20])
    plt.axis('off')
    plt.savefig("output/positive-slope.png", bbox_inches='tight')
    plt.show()

def renderHyperplane2D():
    inputs = np.linspace(-2.5, 0.5, 1000)

    outputs = inputs**3 + 3*inputs**2 + inputs + 1

    tangentLine = -2*inputs

    plt.figure(figsize=(6.4*2/3, 4.8*2/3))
    plt.plot(inputs, outputs, "k")
    plt.plot(inputs, tangentLine, "r")
    plt.axis([-2.5, 0.5, 0, 4])
    plt.axis('off')
    plt.savefig("output/hyperplane-2D.png", bbox_inches='tight')
    plt.show()

def renderHyperplane3D():
    plt.figure(figsize=(6.4*2/3, 4.8*2/3))
    ax = plt.axes(projection='3d')

    def f(x, y):
        return -x**2 - y**2

    x = np.linspace(-4, 4, 50)
    y = np.linspace(-4, 4, 50)

    X, Y = np.meshgrid(x, y)

    Z = f(X, Y)

    Z_plane = -6*X+9

    ax.scatter([3], [0], [-9], c="k")
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none', zorder=10, alpha=0.7)
    ax.plot_surface(X, Y, Z_plane, edgecolor='none', color="r", zorder=10, alpha=0.5)
    ax.view_init(elev=31, azim=-115)
    ax.set_xlabel("x", labelpad=-12.5)
    ax.set_ylabel("y", labelpad=-12.5)
    ax.set_zlabel("z", labelpad=-12.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    plt.savefig("output/hyperplane-3D.png", bbox_inches='tight', dpi=130)
    plt.show()

# Render via running the appropriate function