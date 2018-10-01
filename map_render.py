import numpy as np
import matplotlib.pyplot as plt
from navigation import *
from io import BytesIO
import base64

# coordinates for map rendering

center_corridor = [[0, 0, 0, 1], [1, 0, -2, -4]]
north_face = [[-3, -2, -1, 0, 1, 3], [0, 0, 0, 0, 0, 0]]
south_face = [[-5, -2, 1, 3, 4], [-4, -4, -4, -4, -4]]
west_face = [[-3, -4, -5], [0, -2, -4]]
east_face = [[3, 4, 4], [0, -2, -4]]
elev_shaft = [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 2, 3, 4]

faces = [center_corridor, north_face, south_face, west_face, east_face]

levels = [[0], [1], [2], [3], [4]]

coord_map = {'elevator': [0,1],
             'corner1': [0,0],
             '01': [-1,0],
             '02': [-2,0],
             'corner2': [-3,0],
             '03': [-4,-2],
             'corner3': [-4,-4],
             '07': [-1,-4],
             'corner4': [1,-4],
             '09': [4,-4],
             'corner5': [5,-4],
             '10': [4,-2],
             'corner6': [3,0],
             '12': [1,0],
             '13': [0,-2], }


def render_map(nodes_list):

    f, axarr = plt.subplots(2, sharex=True)

    level_a = nodes_list[0][:3]
    level_a_points = [[],[]]
    level_b_points = [[],[]]

    for node in nodes_list:
        key = node[3:]
        if node[:3] == level_a:
            level_a_points[0].append(coord_map[key][0])
            level_a_points[1].append(coord_map[key][1])
        else:
            level_b_points[0].append(coord_map[key][0])
            level_b_points[1].append(coord_map[key][1])

    start_lev = str(nodes_list[0][0:3]).split(".")
    end_lev = str(nodes_list[-1][0:3]).split(".")
    for face in faces:
        axarr[0].set_title("Start: Building " + start_lev[0] + " Level " + start_lev[1])
        axarr[0].plot(face[0], face[1], c=[0, 0, 0, 0.2], linewidth=10)
        axarr[0].plot(face[0], face[1], c=[0, 0, 0, 0.5], linewidth=3)
        axarr[0].scatter(face[0], face[1], c='g', s=100, marker='o')

        try:
            axarr[1].set_title("End: Building " + end_lev[0] + " Level " + end_lev[1])
            axarr[1].plot(face[0], face[1], c=[0, 0, 0, 0.2], linewidth=10)
            axarr[1].plot(face[0], face[1], c=[0, 0, 0, 0.5], linewidth=3)
            axarr[1].scatter(face[0], face[1], c='g', s=100, marker='o')
        except:
            pass

    axarr[0].plot(level_a_points[0], level_a_points[1], c='r', linewidth=3)
    axarr[0].scatter(level_a_points[0][0], level_a_points[1][0], c='r', s=200, marker='o')
    axarr[0].scatter(level_a_points[0][-1], level_a_points[1][-1], c='r', s=400, marker='^')
    axarr[0].text(level_a_points[0][0]-0.3, level_a_points[1][0]+0.4, nodes_list[0])
    axarr[0].text(level_a_points[0][-1]-0.3, level_a_points[1][-1]+0.4, nodes_list[len(level_a_points[0])])

    try:
        axarr[1].plot(level_b_points[0], level_b_points[1], c='r', linewidth=3)
        axarr[1].scatter(level_b_points[0][0], level_b_points[1][0], c='r', s=200, marker='o')
        axarr[1].scatter(level_b_points[0][-1], level_b_points[1][-1], c='r', s=400, marker='^')
        axarr[1].text(level_b_points[0][0]-0.3, level_b_points[1][0]+0.4, nodes_list[-1*len(level_b_points[0])])
        axarr[1].text(level_b_points[0][-1]-0.3, level_b_points[1][-1]+0.4, nodes_list[-1])
    except:
        pass

    axarr[0].axis('off')
    axarr[1].axis('off')
    plt.tight_layout()
    
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata = base64.b64encode(figfile.getvalue())
    result = figdata
    return(result)


if __name__ == '__main__':
    nodes = g.shortest_path('1.201', '2.5corner4')
    print(render_map(nodes))
