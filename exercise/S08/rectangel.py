class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #   def get_width(self):
    # 	return self.width

    #   def get_height(self):
    # 	return self.height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_premeter(self):
        premeter = 2 * (self.width + self.height)
        return premeter

    def set_area(self, value):
        previous_area = self.width * self.height
        new_ratio = (value / previous_area) ** 1 / 2
        self.width = new_ratio * self.width
        self.height = new_ratio * self.height

    def set_perimeter(self, value):
        previous_premeter = 2 * (self.width + self.height)

        new_premeter_ratio = value / previous_premeter
        self.width = new_premeter_ratio * self.width
        self.height = new_premeter_ratio * self.height


pass

o = Rectangle(20, 30)
print(o.get_height())
print(o.get_width())
print(o.get_area())
print(o.get_premeter())
print(o.def_area_changing_width(10))
print(o.def_premeter_change_width(10))



