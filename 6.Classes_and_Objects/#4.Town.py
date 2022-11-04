class Town:

    def __init__(self, name: str, latitude="0°N", longitude="0°E"):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def set_latitude(self, new_latitude):
        self.latitude = new_latitude

    def set_longitude(self, new_longitude):
        self.longitude = new_longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
