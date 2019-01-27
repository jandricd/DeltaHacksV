import math
import matplotlib.pyplot as plt
import numpy as np
import time

def process_start_end():
    infile = open("ITM_20190121.csv")
    data = infile.readlines()
    infile.close()

    data[:] = [line.strip().split(',') for line in data]
    start_tup = ([], [])
    end_tup = ([], [])

    truck_dict = {}
    for truck in data:
        if truck[8] != 'NULL' and truck[9] != 'NULL':
            if truck[4] == "Trip Start":
                start_tup[0].append(float(truck[9]))
                start_tup[1].append(float(truck[8]))

            elif truck[4] == "Trip End":
                end_tup[0].append(float(truck[9]))
                end_tup[1].append(float(truck[8]))

    return [start_tup, end_tup]

def process_all():
    # open file
    infile = open("ITM_20190121.csv")
    # read lines
    data = infile.readlines()
    infile.close()
    data[:] = [line.strip().split(',') for line in data] 
    
    # latlong_list = []
    # for truck in data:
    #     if (truck[8] != 'NULL' and truck[9] != 'NULL') and (truck[8] != 'Latitude' and truck[9] != 'Longitude'):
    #         latlonge = (truck[8], truck[9])
    #         latlong_list.append(latlonge)

    # latlong_list = [[], []]
    # for truck in data:
    #     if (truck[8] != 'NULL' and truck[9] != 'NULL') and (truck[8] != 'Latitude' and truck[9] != 'Longitude'):
    #         lat = truck[8]
    #         longe = truck[9]
    #         latlong_list[0].append(float(lat))
    #         latlong_list[1].append(float(longe))
    truck_dict = {}
    
    for truck in data:
        if (truck[8] != 'NULL' and truck[9] != 'NULL') and (truck[8] != 'Latitude' and truck[9] != 'Longitude'):
            lat = float(truck[8])
            longe = float(truck[9])
            truck = truck[14]
            try:
                truck_dict[truck][0].append(longe)
                truck_dict[truck][1].append(lat)
            except KeyError:
                truck_dict[truck] = ([], [])
                truck_dict[truck][0].append(longe)
                truck_dict[truck][1].append(lat)
    
    print(truck_dict.keys())
    # print(latlong_list)
    return truck_dict

def display_all(data):
    return

def main():

    # start_end = process_start_end()
    # data = (start_end[0], start_end[1])
    # colors = ('b', 'r')
    # groups = ('start', 'end')
    
    # # Create plot
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1, facecolor="1.0")
    # print
    # for data, color, group in zip(data, colors, groups):
    #     x, y = data
    #     ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
    
    # plt.title('Matplot scatter plot')
    # plt.legend(loc=2)
    # plt.show()


    # truck_dict = process_all()
    # data = (truck_dict['816807'],truck_dict['816829'],truck_dict['816839'], truck_dict['820366'], truck_dict['820487'], 
    # truck_dict['820510'], truck_dict['820553'], truck_dict['820583'], truck_dict['821623'], truck_dict['821659'], truck_dict['832993'])
    # colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'k', 'g', 'r', 'c')
    # groups = ('816807', '816829', '816839', '820366', '820487', '820510', '820553', '820583', '821623', '821659', '832993')
    
    # clear: 816807, 816829, 816839, 820366, 820487, 820553, 820583
    # sus: 820510, 821623
    
    truck_dict = process_all()
    start_end_dict = process_start_end()
    truck = '821623'
    start = (
        start_end_dict[0][0],
        start_end_dict[0][1])
    end = (
        start_end_dict[1][0],
        start_end_dict[1][1])
    data = (truck_dict[truck], start, end)
    print(start, end)
    print(truck)
    colors = ('b', 'g', 'r')
    groups = (truck, 'start', 'end')
    
    # Create plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor="1.0")
    
    for data, color, group in zip(data, colors, groups):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
    
    plt.title('Matplot scatter plot')
    plt.legend(loc=2)
    plt.show()

    return

if __name__ == '__main__':
    main()




 

