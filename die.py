import random

class die:
    value = 1
    #position
    x = 0
    y = 0
    image = "./dice/die_face_blank.png"
    keep = False

    def roll(self):
        if not self.keep == True:
            self.value = random.randrange(1, 7, 1)
            self.image = "./dice/die_face_"+str(self.value)+".png"

    def setLocation(self, x, y):
        self.x = x
        self.y = y
    def getLocation(self):
        return (self.x, self.y)

    def setKeep(self, keep):
        self.keep = keep
    def getKeep(self):
        return self.keep

    def getValue(self):
        return self.image

