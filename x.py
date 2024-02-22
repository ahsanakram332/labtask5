class Shape():
    def _init_(self, name, width=None, height=None):
        self._name = name
        if width is not None and height is not None:
            self._width = width
            self._height = height
        else:
            raise ValueError("Both width and height must be provided.")

    @property
    def name(self):
        return self._name

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    
class Rectangle(Shape):
    def _init_(self, name, width, height):
        super()._init_(name, width, height)
        
    def calculate_area(self):
        return self._width * self._height

    def calculate_perimeter(self):
        return 2 * (self._width + self._height)


class Circle(Shape):
    def _init_(self, name, radius):
        super()._init_(name, None, None)  # Since a circle does not have explicit width and height
        self.radius = radius

    def calculate_area(self):
        return pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * pi * self.radius
    
    from math import pi

class Shape():
    def _init_(self, name, width=None, height=None):
        self._name = name
        if width is not None and height is not None:
            self._width = width
            self._height = height
        else:
            raise ValueError("Both width and height must be provided.")

    @property
    def name(self):
        return self._name

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    
class Rectangle(Shape):
    def _init_(self, name, width, height):
        super()._init_(name, width, height)
        
    def calculate_area(self):
        return self._width * self._height

    def calculate_perimeter(self):
        return 2 * (self._width + self._height)


class Circle(Shape):
    def _init_(self, name, radius):
        super()._init_(name, None, None)  # Since a circle does not have explicit width and height
        self.radius = radius

    def calculate_area(self):
        return pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * pi * self.radius
    
    from math import pi

class Shape():
    def _init_(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    
class Rectangle(Shape):
    def _init_(self, name, width, height):
        super()._init_(name)
        self._width = width
        self._height = height
        
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value
        
    def calculate_area(self):
        return self._width * self._height

    def calculate_perimeter(self):
        return 2 * (self._width + self._height)


class Circle(Shape):
    def _init_(self, name, radius):
        super()._init_(name)
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value

    def calculate_area(self):
        return pi * (self._radius ** 2)

    def calculate_perimeter(self):
        return 2 * pi * self._radius
    
    my_rectangle = Rectangle("My Rectangle", 5, 10)
print(f"Area: {my_rectangle.calculate_area()}")
print(f"Perimeter: {my_rectangle.calculate_perimeter()}")

my_circle = Circle("My Circle", 7)
print(f"Area: {my_circle.calculate_area()}")
print(f"Perimeter: {my_circle.calculate_perimeter()}")

class Circle(Shape):
    ...
    
    def calculate_area(self):
        return pi * (self._radius ** 2)

    def calculate_perimeter(self):
        return 2 * pi * self._radius
    

    import unittest
from data_structures import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def test_adding_elements(self):
        dp_tuple = DataProcessor((1, 2, 3))
        dp_tuple.add_element(4)
        self.assertCountEqual(sorted(dp_tuple.data), sorted((1, 2, 3, 4)))

        dp_list = DataProcessor([1, 2, 3])
        dp_list.add_element(4)
        self.assertEqual(len(dp_list.data), 4)
        self.assertListEqual(dp_list.data, [1, 2, 3, 4])

        dp_dict = DataProcessor({'a': 1, 'b': 2})
        dp_dict.add_element(('c', 3))
        self.assertEqual(len(dp_dict.data), 3)
        self.assertDictEqual(dp_dict.data, {'a': 1, 'b': 2, ('c', 3): None})

    def test_removing_elements(self):
        dp_tuple = DataProcessor((1, 2, 3))
        dp_tuple.remove_element(2)
        self.assertNotIn(2, dp_tuple.data)
        self.assertCountEqual(sorted(dp_tuple.data), sorted((1, 3)))

        dp_list = DataProcessor([1, 2, 3])
        dp_list.remove_element(2)
        self.assertNotIn(2, dp_list.data)
        self.assertListEqual(dp_list.data, [1, 3])

        dp_dict = DataProcessor({'a': 1, 'b': 2})
        dp_dict.remove_element('a')
        self.assertNotIn('a', dp_dict.data)
        self.assertDictEqual(dp_dict.data, {'b': 2})

if _name_ == "_main_":
    unittest.main()