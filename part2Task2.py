from collections import defaultdict
from queue import Empty, Queue
from part2task1 import bfs, dfs, dijkstra
from project import Truck
from project import Package 



"""
deliveryService
"""
def deliveryService(map, truck, packages):
    deliveredTo = {}
    stops = []
    #store all the packages info to make a while loop
    pk_dic = {}
    for package in packages:
        if package.office in pk_dic:
            pk_dic[package.office] = pk_dic[package.office] + [package.id]
        else:
            pk_dic[package.office] = [package.id]
    # keep running until all packages are gone
    while pk_dic or truck.packages:
        # check to see if we are at an office
        if "UPS" in truck.location:
            #counter to remove from pk_dic
            s_space = len(truck.packages)
            for i in packages:
                truck.collectPackage(i)
            #if counter is greater than 0
            new_space = len(truck.packages) - s_space
            # we will reduce diction
            if new_space > 0:
                pk_dic[truck.location] = pk_dic[truck.location][new_space:]
            if pk_dic[truck.location] == []:
                del pk_dic[truck.location]
        #check for path of eath packages and drive there and delivers
        q = Queue()
        for key in truck.packages:
            q.put(key)
        while q:
            path = dijkstra(map, truck.location)
            temp = q.get()
            for i in path[temp][1:]:
                truck.driveTo(truck.location, i)
                stops.append(i)
            truck.deliverPackage(temp)
            deliveredTo[temp] = truck.location
        #drive to new UPS stop in pk_dic
        if truck.packages == {} and pk_dic != {}:
            temp = list(pk_dic.keys)[0]
            path = dijkstra(map, truck.location)
            for i in path[temp][1:]:
                truck.driveTo(truck.location, i)
                stops.append(i)

    return (deliveredTo, stops)
