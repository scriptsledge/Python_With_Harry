from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self, to):
        print(f"Train no: {self.trainNo} is on the way to {to}")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(500, 1000)}")

worldpur = Train(14544)
worldpur.book("Rampur", "Sitapur")
worldpur.getStatus("Ravanpur")
worldpur.getFare("Hanupur", "Lankapur")
