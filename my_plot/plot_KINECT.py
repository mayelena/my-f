import numpy as np

A=[-0.205497,0.317856,2.61465,-0.20071,0.384783,2.60052,-0.1756,0.719803,2.5476,-0.158493,0.86136,2.44676,-0.3619,0.660523,2.59608,-0.531606,0.478228,2.65811,-0.677565,0.359932,2.56136,-0.708053,0.327118,2.51712,-0.020397,0.612456,2.54628,-0.0528336,0.394365,2.5062,-0.290771,0.310309,2.46979,-0.354356,0.317127,2.46116,-0.285849,0.246159,2.63947,-0.340629,-0.249113,2.69552,-0.368561,-0.587021,2.67328,-0.377882,-0.666294,2.60669,-0.135635,0.234024,2.61052,-0.094661,-0.189732,2.69507,-0.0958316,-0.502295,2.71239,-0.0802723,-0.628217,2.65897]

A = np.array(A)
A = A.reshape(20,3)

A = A.tolist()

B = [A[3],A[2],A[5],A[6],A[7],A[8],A[9],A[10],A[12],A[13],A[14],A[16],A[17],A[18]]
print (B)
zd = [(B[8][0]+B[11][0])/2, (B[8][1]+B[11][1])/2, (B[8][2]+B[11][2])/2]
B.append(zd)
print(B)

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

p=np.array(B)
x,y,z=list(zip(*p))
y=list(map(lambda x:-x,y))

pose=np.array([x,z,y])
pose-=np.mean(pose,axis=1,keepdims=True)

plot_pose(pose)