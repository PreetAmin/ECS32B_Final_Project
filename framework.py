class Package:
    def __init__(self, id):
        self.id = id
        self.address = ""
        self.ownerName = ""
        self.delivered = False
        self.pickedUp = False



class Truck:
    def __init__(self, id, n):
        self.id = id
        self.size = n
        self.location = ""
        # self.packages = ?

    def addPackage(self, pk):



    def deliverPackage(self, pk):



    def deliverPackageByAddress(self, addr):
        


    def removePackage(self, pk):



    def driveTo(self, loc1, loc2):



    def getPackagesIds(self):





