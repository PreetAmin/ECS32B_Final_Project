class Package:
    def __init__(self, id):
        self.id = id
        self.address = ""
        self.office = ""
        self.ownerName = ""
        self.collected = False
        self.delivered = False


class Truck:
    def __init__(self, id, n, loc):
        self.id = id
        self.size = n
        self.location = loc
        self.packages = {}

    def collectPackage(self, pk):
        if self.location == pk.office and len(self.packages) < self.size :
        # Add package to packages dictionary
            self.packages[pk.id] = pk

        # Set package pickedUp to true
            pk.collected = True

    def deliverPackage(self, pk):
        # Find delivery location
        # drive to required location
        if pk.id in self.packages:

        # remove the package from truck
            del self.packages[pk.id]

        # set delivery status to true for package
            pk.delivered = True

    def deliverPackageByAddress(self, addr):
        # drive to address
        # find all the packages we need to deliver
        # loop through all needed packages
        delivered_pack = []
        for key in self.packages:
            if self.packages[key].address == addr:
                # set package status to delivered
                self.packages[key].delivered = True
                delivered_pack.append(key)
        for key in delivered_pack:
            if self.packages[key].delivered == True:
                # remove package from truck
                del self.packages[key]

                

    def removePackage(self, pk, office):
        # drive to post office
        # set picked up back to false
        if self.location == office and pk.id in self.packages:
            if self.packages[pk.id].office != office:
                self.packages[pk.id].office = office
            self.packages[pk.id].collected = False
        # remove package from truck (don't set delivery status to true)
            del self.packages[pk.id]

    def driveTo(self, loc1, loc2):
        # set truck's location to location 2
        if self.location == loc1 and loc1 != loc2:
            self.location = loc2
        
    def getPackagesIds(self):
        # intialize empty python list
        Id_list = []
        # for package on truck:
        for package in self.packages:
            # get ID
            # add ID to list
            Id_list.append(package)
        # return output list
        return Id_list
