from x import X
from y import Y
from z import Z

class Object(X, Y, Z):
    def __init__(self, objectInput = None):
        self.objectInput = objectInput