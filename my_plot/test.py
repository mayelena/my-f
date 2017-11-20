import numpy as np

f=open("E:/May/3DGolfPose/Debug/real_cord.txt","r")
lines=f.readlines()
f.close()
n=len(lines)
real_cord=[]
for i,line in enumerate(lines):
    real_cord.append([])
    real_cord[i].append(list(map(float,line.strip().split(" "))))
real_cord=np.array(real_cord).reshape(n,18,3)

origin=np.array([1.38655420e+03,   8.63870422e+02,  -2.22925000e+03])

real_cord-=origin

print(real_cord)

with open("outputx.txt","w") as f:
    f.write(str(real_cord.tolist()))



import numpy as np

import matplotlib.pyplot as plt

def plot_pose(pose):
    """Plot the 3D pose showing the joint connections."""
    import mpl_toolkits.mplot3d.axes3d as p3

    # _CONNECTION = [
    #     [0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [0, 7], [7, 8],
    #     [8, 9], [9, 10], [8, 11], [11, 12], [12, 13], [8, 14], [14, 15],
    #     [15, 16]]

    _CONNECTION = [
        [0,1],[1,14],[2,1],[2,3],[3,4],[5,1],[5,6],[6,7],[14,8],[8,9],[9,10],[14,11],[11,12],[12,13]
    ]

    def joint_color(j):
        """
        TODO: 'j' shadows name 'j' from outer scope
        """

        colors = [(0, 0, 0), (255, 0, 255), (0, 0, 255),
                  (0, 255, 255), (255, 0, 0), (0, 255, 0)]
        _c = 0
        if j in range(2, 5):
            _c = 1
        if j in range(5, 8):
            _c = 2
        if j in range(8, 11):
            _c = 3
        if j in range(11, 14):
            _c = 4
        # if j in range(14, 17):
        #     _c = 5
        return colors[_c]

    assert (pose.ndim == 2)
    assert (pose.shape[0] == 3)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    for c in _CONNECTION:
        col = '#%02x%02x%02x' % joint_color(c[0])
        ax.plot([pose[0, c[0]], pose[0, c[1]]],
                [pose[1, c[0]], pose[1, c[1]]],
                [pose[2, c[0]], pose[2, c[1]]], c=col)
    for j in range(pose.shape[1]):
        col = '#%02x%02x%02x' % joint_color(j)
        ax.scatter(pose[0, j], pose[1, j], pose[2, j],
                   c=col, marker='o', edgecolor=col)
    smallest = pose.min()
    largest = pose.max()
    ax.set_xlim3d(smallest, largest)
    ax.set_ylim3d(smallest, largest)
    ax.set_zlim3d(smallest, largest)

    return fig

p=np.array([[-0.116076, 0.85712, 2.03345], [-0.119417, 0.72904, 2.11552], [-0.350045, 0.433939, 2.15463], [-0.295988, 0.276044, 1.99476], [-0.282735, 0.245716, 1.9392], [0.0395475, 0.613331, 2.12756], [0.0951764, 0.410642, 2.08408], [0.0780926, 0.300569, 1.90763], [-0.208399, 0.237249, 2.09626], [-0.289298, -0.275609, 2.1652], [-0.317303, -0.62768, 2.19608], [-0.0673923, 0.234363, 2.09191], [-0.0426268, -0.25831, 2.19541], [-0.0381535, -0.615049, 2.2843], [-0.13789565, 0.235806, 2.0940849999999998]]

)
x,y,z=list(zip(*p))
y=list(map(lambda x:-x,y))

pose=np.array([x,z,y])
pose-=np.mean(pose,axis=1,keepdims=True)

plot_pose(pose)

import math
A=[-0.0958316, -0.502295, 2.71239]
B= [-0.094661, -0.189732, 2.69507]


# A=[13.339005, 19.266312, 71.0989]
#
# B=[12.216493, 9.854486, 71.0989]


dis=0
for i in range(len(A)):
    dis += (A[i]-B[i])**2
print (math.sqrt(dis))