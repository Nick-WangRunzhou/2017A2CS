import pickle
class CarRecord:
    def __init__(self):
        self.VehicleID = ''
        self.Registration = ''
        self.DateofRegistration = None
        self.Enginesize = 0
        self.PurchasePrice = 0.00
def SaveData(Car):
    CarFile = open('CarFile.DAT','wb')
    for i in range(100):
        pickle.dump(Car[i], CarFile)
    CarFile.close()
def LoadData():
    CarFile = open('CarFile.DAT','rb')
    Car = []
    EoF = False
    while not EoF :
        try :
            Car.append(pickle.load(CarFile))
        except :
            EoF = True
    CarFile.close()
    return Car

def OutputRecords(Car) :
    for i in range(100):
        print(Car[i].VehicleID)

def main() :
    ThisCar = CarRecord()
    Car = LoadData()
    OutputRecords(Car)
    i = int(input('Record Number? '))
    while i != 0 :
        Car[i].VehicleID = input('Vehicle ID: ')
        Car[i].Registration = input('Registration: ')
        Car[i].DateOfregistration =(input('Registration Date: '))
        Car[i].EngineSize = int(input('Engine size: '))
        Car[i].PurchasePrice = float(input('Purchaseprice: '))
        i = int(input('next Record Number? '))
    OutputRecords(Car)
    SaveData(Car)
main()

