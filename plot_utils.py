import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plot_camera_axis(ax, R, t):
    """
    R and t are used to transform a point P's coordinates in the 
    world frame into coordinates in the camera's frame according
    to the formula: Pc = R@Pw + t
    """
    pts_cam = np.array([
        [0,0,0],
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]).reshape((4, 3, 1))
    pts_world = camera_to_world(pts_cam, R, t)
    ax.quiver(*pts_world[0], *(pts_world[1]-pts_world[0]), color='r', zorder=1)
    ax.quiver(*pts_world[0], *(pts_world[2]-pts_world[0]), color='g', zorder=1)
    ax.quiver(*pts_world[0], *(pts_world[3]-pts_world[0]), color='b', zorder=1)
    
    
    
    
def world_to_camera(pts_world, R, t):
    """
    pts_world is an Nx3x1 array of points in the world frame
    pts_world may also be a single 3x1 point in the world frame
    """
    return R@pts_world + t




def camera_to_world(pts_camera, R, t):
    """
    pts_camera is an Nx3x1 array of points in the camera frame
    pts_camera may also be a single 3x1 point in the camera frame
    """
    return R.T@pts_camera - R.T@t


def project(pts, K, R, t):
    pts_arr = pts.reshape((-1,3,1))
    pts_cam = K @ (R @ pts_arr + t)
    pts_2d = (pts_cam[:,:2]/pts_cam[:,2:]).reshape((-1,2))
    return pts_2d