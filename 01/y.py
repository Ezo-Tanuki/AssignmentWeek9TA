from a import A
from b import B

class Y(A, B):
    def __init__(self, y = None):
        self.y = y