B=[[-52.730831272846167, 8.6193282979668044, 497.66538876040426], [-114.14317443336842, 46.345506352083071, 402.77741235054083], [-189.48140796866434, -81.972364493772147, 352.04683038700199], [39.833834425670425, -315.93420852092953, 320.64972004616561], [164.48060576683798, -242.48593229529521, 520.6560514762923], [-3.9422489546267983, 163.96332696623938, 352.05117402959911], [123.42722570333879, 238.36386503141591, 210.88074540638334], [170.27908546597379, 105.63844336242131, 331.22097451914647], [-62.830699542679355, -121.13403809655424, -122.39787477796804], [-139.24889906526838, -104.25423957585434, -580.57052979867638], [-281.48206586631858, -22.074502030080456, -954.08899891075964], [102.29255886074068, 97.853969318387612, -119.42806639286269], [166.19573335747901, 47.986299437685489, -573.6310522476075], [194.12637516976991, 92.85382164757938, -968.34714163864464], [9.2190455637893081, -11.639993828495312, -139.45391262228244]]
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
