from Rectangle import Rectangle

class Surface:
    def __init__(self, filename, x, y, h, w):
        '''
        Takes the filename string as a parameter and saves it as an instance           variable
        args: filename, x y coordinates, and rectangle height and width
        return: None
        '''
        self.rect = Rectangle(x, y, h, w)
        self.image = str(filename)

    def getRect(self):
        '''
        Recieves and returns rectangle from __init__
        args: none
        return: rectangle
        '''
        return self.rect