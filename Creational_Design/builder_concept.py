"Builder Concept Sample Code"
from abc import ABCMeta, abstractmethod

class IBuilder(metaclass=ABCMeta):
    "The Builder Interface"
    @staticmethod
    @abstractmethod
    def build_part_a():
        "Build part a"
    
    @staticmethod
    @abstractmethod
    def build_part_b():
        "Build part b"
    
    @staticmethod
    @abstractmethod
    def build_part_c():
        "Build part c"
    
    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"

class Builder(IBuilder):
    "The Concrete Builder."
    def __init__(self):
        self.product = Product()
    
    def build_part_a(self):
        self.product.parts.append('tile')
        return self
    
    def build_part_b(self):
        self.product.parts.append('caementum')
        return self
    
    def build_part_c(self):
        self.product.parts.append('sand')
        return self
    
    def get_result(self):
        return self.product

class Product():
    "The Product"
    def __init__(self):
        self.parts = []

class Director:
    "The Director, building a complex representation."
    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return Builder()\
            .build_part_b()\
            .build_part_c()\
            .build_part_a()\
            .get_result()

# The Client
PRODUCT = Director.construct()
print(PRODUCT.parts)
