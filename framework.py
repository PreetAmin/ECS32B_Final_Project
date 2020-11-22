class Package:
    def __init__(self, id):
        self.id = id
        self.address = ""
        self.ownerName = ""
        self.collected = False
        self.delivered = False


class Truck:
    def __init__(self, id, n):
        self.id = id
        self.size = n
        self.location = ""
        self.packages = {}

    def addPackage(self, pk):
        # Add package to packages dictionary
        self.packages[pk.id] = pk

        # Set package pickedUp to true
        pk.collected = True

    def deliverPackage(self, pk):  # Milap

    # Find delivery location
    # drive to required location
    # remove the package from truck
    # set delivery status to true for package

    def deliverPackageByAddress(self, addr):  # Dave
    # drive to address
        self.driveTo(self.location,addr)
    # find all the packages we need to deliver
    # loop through all needed packages
        for key in self.packages:
            if self.packages[key].address == addr:
                # set package status to delivered
                self.packages[key].deliver = True
                # remove package from truck
                #del self.packages[key]






    def removePackage(self, pk, office):  # Preet

    # drive to post office
    # remove package from truck (don't set delivery status to true)
    # set picked up back to false

    def driveTo(self, loc1, loc2):  # Preet

    # set truck's location to location 2

    def getPackagesIds(self):  # Preet
# intialize empty python list
# for package on truck:
# get ID
# add ID to list






