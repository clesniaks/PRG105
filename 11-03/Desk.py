import OfficeFurniture


class Desk(OfficeFurniture.OfficeFurniture):

    def __init__(self, category, material, length, width, height, price, drawer_location, num_drawers):
        OfficeFurniture.OfficeFurniture.__init__(self, category, material, length, width, height, price)
        self.__drawer_location = drawer_location
        self.__num_drawers = num_drawers

    def set_drawer_location(self, drawer_location):
        self.__drawer_location = drawer_location

    def set_num_drawers(self, num_drawers):
        self.__num_drawers = num_drawers

    def get_drawer_location(self):
        return self.__drawer_location

    def get_num_drawers(self):
        return self.__num_drawers

    def __str__(self):
        OfficeFurniture.OfficeFurniture.__str__(self)
        print("Drawer Location: " + self.get_drawer_location())
        print("Number of Drawers: " + str(self.get_num_drawers()))
        
