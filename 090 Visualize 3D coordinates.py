import numpy as np
from glob import glob
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


data = np.load('data/tab/npz/player_101_results.npz',allow_pickle=True)['results'][()]
coordinates = data['../drive/MyDrive/pose_video/player_101_frames/000000.jpg'][0]['j3d_smpl24']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

side_1 = [23, 21, 19, 17, 14, 9, 6, 3, 0, 2, 5, 8, 11]
ax.plot(xs = [coordinates[xs][0] for xs in side_1], 
        ys = [coordinates[ys][1] for ys in side_1], 
        zs = [coordinates[zs][2] for zs in side_1],
        marker='.')

side_2 = [22, 20, 18, 16, 13, 9, 6, 3, 0, 1, 4, 7, 10]
ax.plot(xs = [coordinates[xs][0] for xs in side_2], 
        ys = [coordinates[ys][1] for ys in side_2], 
        zs = [coordinates[zs][2] for zs in side_2],
        marker='.')

spine = [15, 12, 14, 9, 13, 12, 13, 9, 6, 3, 0]
ax.plot(xs = [coordinates[xs][0] for xs in spine], 
        ys = [coordinates[ys][1] for ys in spine], 
        zs = [coordinates[zs][2] for zs in spine],
        marker='.')

limbs_3d = {'left_hand':22, 'left_wrist':20, 'left_elbow':18, 'left_shoulder':16, 'left_back':13,
        'right_hand':23, 'right_wrist':21, 'right_elbow':19, 'right_shoulder':17, 'right_back':14,
        'nose':15, 'neck':12, 'upper_back':9, 'back':6, 'lower_back':3, 'hip':0,
        'left_hip':1, 'left_knee':4, 'left_ankle':7, 'left_foot': 10,
        'right_hip':2, 'right_knee':5, 'right_ankle':8, 'right_foot': 11}

plt.show()
