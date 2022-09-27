# import unittest
# # class Class1:
# #     def method1(self):
# #         pass#заглушка, которая ничего не делает
# # class Class2(Class1):#Class2 наследует все возможности class1
# #     def method2(self):
# #         pass
# # Class1.method1()
# # Class2.method2()
# # Class2.method1()
# # #Class1.method2()#нет возможности обратиться к методам потомка
#
# import unittest
# class TestStringMethods(unittest.TestCase):
#     def setUp(self):
#         #print("Test start")
#         self.test_string = "foo"
#
#     def tearDown(self):
#         pass
#        # print("Test stop")
#
#
#     def test_upper(self):
#        # print("test_upper")
#         self.assertEqual(self.test_string.upper(), 'FOO')
#
#     def test_isupper(self):
#         #print("test_isupper")
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse(self.test_string.isupper())
#
#     def test_split(self):
#        # print("test_split")
#         s = self.test_string
#         self.assertEqual(s.split(), ['foo'])
#      # Проверим, что s.split не работает, если разделитель - не строка
#         with self.assertRaises(TypeError):
#             s.split(1)
#
# if __name__ == '__main__':
#     unittest.main()
#
#
# class Point(object):
#     def __init__(self, x, y):
#         self.x = float(x)
#         self.y = float(y)
#         #__eq__ - ==
#         #__str__ - str()
#     def __str__(self):return f"({self.x}, {self.y})"
#     def __eq__(self, other):return True if ((self.x == other.x) and (self.y == other.y)) else False
#     def __add__(self, other):#перегрузка  (функция) - описываем логику + для наших объектов
#         x = self.x + other.x
#         y = self.y - other.y
#         return x,y
# point1 = Point("1",2)
# point2 = Point(2,3)
# a = 5
# b = 3
# print(a+b)
# print(point1 + point2)# теперь умеем складывать наши объекты
# point1 = Point("1", 0)
# print(point1.__str__())


""" start"""



# # content of test_expectation.py
# class numberIsNegative(Exception):
#     pass
# class argIsNotNumbers(Exception):
#     pass
#
# """
# на выбор написать тесты для 2 любых исключений
# не int и не float исключение
# равносторонний треугольник 3,3,3 true
# египетский треугольник стороны - 3,4,5 true
# передать десятичные числа в качестве сторон true
# 1 2 3 false
# -1-1-1 - исключение
# 000 - исключение
#
# один аргумент? исключение
# больше 4  исключение
# 1 2 3 false
# """
# class TriangleChecker:
#     def __init__(self, sides):
#         self.sides = sides
#     def is_triangle(self):
#         if all(isinstance(side, (int, float)) for side in self.sides):#Функция isinstance() вернет True, если проверяемый объект object является экземпляром указанного класса (классов)
#             if all(side > 0 for side in self.sides):
#                 sorted_sides = sorted(self.sides)
#                 if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
#                     return True
#                 return False
#             raise numberIsNegative
#         raise argIsNotNumbers
# sides=[1,2,3]
# TriangleChecker(sides).is_triangle()
# # стороны 1,2,3 ожидаемо вернется false
# # стороны 3,2,3 ожидаемо вернется True
# @pytest.fixture()
# def Trianglesides():
#     return TriangleChecker([-1, 0, -5])
# def test_numberIsNegative_exception(Trianglesides):
#     with pytest.raises(numberIsNegative):
#         Trianglesides.is_triangle()
# @pytest.mark.parametrize("sides, expected_boolean", [
#     ([3, 4, 5], True),
#     ([3, 3, 3], True),
#     ([1.5, 6, 2.2], True),
#     ([1, 2, 3], False),
# ])
# def test_isTriangle_function(sides, expected_boolean):
#     assert TriangleChecker(sides).is_triangle() == expected_boolean
# print("x,y,z,f")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             if not(x or y)or(z==x):
#                 print(x, y, z, 1)
#             else:
#                 print(x, y, z, 0)
print("x,y,z,f")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not(not(x or y)or(z==x)):
                print(x, y, z, 0)




