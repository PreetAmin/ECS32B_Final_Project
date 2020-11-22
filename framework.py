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
        #Add package to packages dictionary
        self.packages[pk.id] = pk
        
        #Set package pickedUp to true 
        pk.pickedUp = True 
       
        
    def deliverPackage(self, pk):#Milap
        #Find delivery location
        #drive to required location
        #remove the package from truck
        #set delivery status to true for package  

    def deliverPackageByAddress(self, addr):#Dave
        #drive to address 
        #find all the packages we need to deliver and their names to some DS 
        #loop through all needed packages 
            #remove package from truck
            #set package status to delivered 

            
            
    def removePackage(self, pk, office):#Preet
        #drive to post office 
        #remove package from truck (don't set delivery status to true)
        #set picked up back to false 

    def driveTo(self, loc1, loc2):#Preet 
        #set truck's location to location 2 
        
        

    def getPackagesIds(self):#Preet 
        #intialize empty python list
        #for package on truck:
            #get ID 
            #add ID to list 
            





