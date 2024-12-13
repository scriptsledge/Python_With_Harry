from random import randint

class Train:
    def __init__(modifiedSelf, trainNo):
        modifiedSelf.trainNo = trainNo

    def book(modifiedSelf, fro, to):
        print(f"Ticket is booked in train no: {modifiedSelf.trainNo} from {fro} to {to}")

    def getStatus(modifiedSelf, to):
        print(f"Train no: {modifiedSelf.trainNo} is on the way to {to}")

    def getFare(modifiedSelf, fro, to):
        print(f"Ticket fare in train no: {modifiedSelf.trainNo} from {fro} to {to} is {randint(500, 1000)}")

worldpur = Train(14544)
worldpur.book("Rampur", "Sitapur")
worldpur.getStatus("Ravanpur")
worldpur.getFare("Hanupur", "Lankapur")
# Using self is the recommended approach