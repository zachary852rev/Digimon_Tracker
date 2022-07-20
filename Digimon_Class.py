
# This is the main Digimon class.
class Digimon():
    def __init__(self, device, version, shape, color=""):
        self._device = str(device)
        self._version = str(version)
        self._shape = str(shape)
        self._color = str(color)

    # Set and get for device name.
    def setDevice(self, device):
        self._device = str(device)

    def getDevice(self):
        return self._device


    # Set and get for version name.
    def setVersion(self, version):
        self._version = str(version)

    def getVersion(self):
        return self._version


        # Set and get for shape name.
    def setShape(self, shape):
        self._shape = str(shape)

    def getShape(self):
        return self._shape
    

        # Set and get for color name.
    def setColor(self, color):
        self._color = str(color)

    def getColor(self):
        return self._color


    def __str__(self): 
        return "» Device: " + self._device + ", Version: " + self._version + ", Shape: " + self._shape + ", Color: " + self._color

# If time allows, would like to implement an active/inactive system
class Active(Digimon):
    def active(self):
        print(self._device, " is active.")

class Inactive(Digimon):
    def inactive(self):
        print(self._device, " is inactive.")