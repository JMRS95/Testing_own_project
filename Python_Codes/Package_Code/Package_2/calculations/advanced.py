class VectorCalculator:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def dot_product(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def cross_product(self, other):
        return VectorCalculator(
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x
        )
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"