class Glassware:
    def __init__(self, material):
        self.material = material


class Beaker(Glassware):
    def __init__(self, capacity, material):
        super().__init__(material)
        self.capacity = capacity


class Tray:
    def __init__(self):
        self.beakers = [
            Beaker(100, "Glass"),
            Beaker(100, "Glass"),
            Beaker(100, "Glass"),
            Beaker(100, "Glass"),
            Beaker(100, "Glass")
        ]


tray = Tray()

print(len(tray.beakers))
print(tray.beakers[0].capacity)
print(tray.beakers[0].material)
del tray
