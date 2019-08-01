class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_premeter(self):
        premeter = 2 * (self.width + self.height)
        return premeter

    def set_area_changing_width(self, value):
        self.width = value / self.height
        return self.width

    def set_premeter_change_width(self, value):
        self.width = (value / 2) - self.height
        return self.height


o = Rectangle(20, 30)
print(o.get_height())
print(o.get_width())
print(o.get_area())
print(o.get_premeter())
print(o.def_area_changing_width(10))
print(o.def_premeter_change_width(10))



