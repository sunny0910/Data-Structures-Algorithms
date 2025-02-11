# Parking Lot
'''
Entities:
- ParkingLot
- Floor
- ParkingSpot (abstract class - 4WheelerParkingSpot, )
- Ticket
- EntryExitGates 
- Payment (Abstract class - DebitCardPayment, CC, Wallet, Cash)
- MonitoringService (How many vehicle per floors) (Touch base - not in requirement)
'''

class ParkingSpot:
    def __init__(self) -> None:
        self._id = None
        
        self._floor = None
        self._vacant = None
        # parked vehicle
        self._vehicle = None
        self.type = None
    def get_id():
        pass

class Floor:
    def __init__(self, number, spots) -> None:
        self.number = number
        self.spots = spots
    
class fourWheelerParkingSpot(ParkingSpot):
    def __init__(self) -> None:
        super().__init__()
    # some attributes related to type of vehicle
    
class Ticket:
    def __init__(self) -> None:
        self._id = None
        self._parkingSpot = None
        self._ParkTime = None
        self._payment = None
        self.endTime = None
        
class FareCalculator:
    # different types: (Weekday, weekend, holiday)
    pass

class Gates:
    def __init__(self) -> None:
        self.type = None


class Payment:
    def __init__(self) -> None:
        pass
    
class WalletPayment:
    def __init__(self) -> None:
        super()
        
        
class ParkingLot:
    def __init__(self, floors=1, parkingSPotsPerFloor=10) -> None:
        self.numberOfFloors = floors
        self.parkingSpotsPerFloor = parkingSPotsPerFloor
        self.floors = None
    
    def initializeParkingLot():
        pass
    
    def assignParkingSpot(gate):
        # finding the nearest spot to the gate from which user comes in
        # assign the spot to the user
        # payment layer if fixed time else None
        # generate ticket
        pass
    
    def releaseParkingSpot(ticket):
        # check ticket for payment
        # if time elapsed, call tarrif calculator and get payment
        # generate payment invoice and give to user
        # get parking spot from tha ticket and unassign the spot
        pass
    
    
# singleton for parkingLot
# abstract for initializes
# strategy pattern for payment and parking spots


# mysql
# archiving tables

# type of data - Relation
# scale of data - data
# classification of no sql database
# mongoDB  - document database
# Cassandra - wide column database - Ever incresing data - distributed database, high availability, eventual consistency, consistent hashing (4 - id%n), data replication among nodes, archiving method
# Redis - caching to increase the performance of the system

'''
CustomerId
API endpoints
ParkingLot:
    getAvailableParkingLot(customerId, floorId, carType, gateId, duration)
    assignParkingSpot(customerId, spotId, duration) ticket
    unassignParkingSpot(ticket) bool

    createParkingLot(customerId, numberOfFloors, spotsPerFloor)
    
Payment

Kubernetes - AKS - multiple pods - HPA
Deployment - Basic, Rolling Deployment, Blue Green deployment

ParkingLot:
 - PaymenService
 - TarrifService
 - ParkingLotService
 - InvoiceService
 Queue, Event Streaming service
 
SingleService and different modules - 16GB ram, octaCore system, 16 threads
- direction - DB - multiple DB connections pool - if example 100 - 100 conncurrent requests
RateLimiter - 
SLA
 
'''