class Rectangle:
    def __init__(self, x, y, h, w):
        '''
        Takes x y coordinates, and height and width, and saves them as                 instance variables
        args: x y coordinates
        return: None
        '''
        self.x = x
        self.y = y
        self.height = h
        self.width = w

        if x < 0:
            self.x = 0
        if y < 0:
            self.y = 0
        if h < 0:
            self.height = 0
        if w < 0:
            self.width = 0

    def __str__(self):
        '''
        returns a string containing the x y coordinates, width, and height of         the rectangle
        args: none
        return: data strings
        '''
        return f'(x: {self.x}, y: {self.y}) width: {self.width}, height: {self.height}'