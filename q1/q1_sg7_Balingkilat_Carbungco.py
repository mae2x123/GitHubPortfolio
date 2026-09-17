class Glassware:
    def __init__(self, material):
        self.material = material


class Beaker(Glassware):
    def __init__(self, capacity):
        super().__init__("Glass")
        self.capacity = capacity


class Tray:
    def __init__(self):
        self.beakers = [
            Beaker(100),
            Beaker(200),
            Beaker(250),
            Beaker(350),
            Beaker(500)
        ]
    def show_inv(self):
        print("The tray exists.")
        print("All glassware in the tray: ")
        for i, beaker in enumerate(self.beakers, 1):
            print(f"Beaker {i}: {beaker.material}, {beaker.capacity} mL")


tray = Tray()
tray.show_inv()
del tray
print("The tray, as well as the beakers, has been disposed of.")
