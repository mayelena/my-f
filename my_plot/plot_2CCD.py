
import numpy as np

A_str="5.338686 -16.130848 66.122620 5.179210 -12.811609 71.098900 2.849276 -11.674003 66.122620 8.533082 -11.458598 62.744511 11.670403 -16.926208 67.208153 7.605481 -13.782166 75.467804 10.464470 -8.352649 73.657356 10.952366 -11.233860 68.329918 6.281290 0.845912 72.355515 3.710232 10.734985 75.467804 0.410728 19.533665 75.467804 10.911740 0.413861 73.657356 12.216493 9.854486 71.098900 13.339005 19.266312 71.098900 4.174284 -16.251303 66.122620 5.338686 -17.174793 66.122620 2.156041 -15.715007 68.329918 -92.350845 -56.521004 155.978638"
A=list(map(float,A_str.split(" ")))



A = np.array(A)
A = A.reshape(18,3)

B = A.tolist()
B = B[:14]
print (B[11],B[12],B[13])

zd = [(B[8][0]+B[11][0])/2, (B[8][1]+B[11][1])/2, (B[8][2]+B[11][2])/2]
B.append(zd)
print(B)

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

p=np.array(B
)
x,y,z=list(zip(*p))
y=list(map(lambda x:-x,y))

pose=np.array([x,z,y])
pose-=np.mean(pose,axis=1,keepdims=True)

plot_pose(pose)
