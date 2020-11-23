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
        if self.location == pk.office:
        # Add package to packages dictionary
            self.packages[pk.id] = pk

        # Set package pickedUp to true
            pk.collected = True

    def deliverPackage(self, pk):
        # Find delivery location
        # drive to required location

        # remove the package from truck
        del self.packages[pk.id]

        # set delivery status to true for package
        pk.delivered = True

    def deliverPackageByAddress(self, addr):
        # drive to address
        self.driveTo(self.location, addr)

        # find all the packages we need to deliver
        # loop through all needed packages
        for key in self.packages:
            if self.packages[key].address == addr:
                # set package status to delivered
                self.packages[key].delivered = True

                # remove package from truck
                del self.packages[key]

    def removePackage(self, pk, office):
        # drive to post office
        self.driveTo(self.location, office)

        # set picked up back to false
        self.packages[pk.id].collected = False

        # remove package from truck (don't set delivery status to true)
        del self.packages[pk.id]

    def driveTo(self, loc1, loc2):
        # set truck's location to location 2
        if loc1 != loc2:
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
