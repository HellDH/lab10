from .enums import TriangleType as tr_type
from typing import Set

class TriangleProblemOne:
    """Класс с методами из задания 1 , лаб. работы 3"""

    def __scaleneTriangle(self,
                          a: float|int,
                          b: float|int,
                          c: float|int) -> float|int:
        """Вычисляет площадь разностороннего треугольника по формуле Герона"""
        half_perimeter = (a + b + c) / 2

        return 0.5 ** ((half_perimeter - a) * \
                       (half_perimeter - b) * \
                       (half_perimeter - c))
    
    def __isoscelesTriangle(self,
                            a: float|int,
                            b: float|int):
        """Вычисляет площадь равнобедренного треугольника по двум сторонам"""
        h = 0.5 * (0.5 ** (4 * (a ** 2) - (b ** 2))) # Высота треугольника

        return 0.5 * b * h
    
    def __equilateralTriangle(self,
                              a: float|int):
        """Вычисляет площадь равностороннего треугольника через высоту"""
        h = (a * (0.5 ** 3)) / 2 # Высота треугольника

        return 0.5 * a * h
    
    def defineTriangle(self,
                       a: float|int,
                       b: float|int,
                       c: float|int) -> str|bool:
        """Определяет тип треугольника и вычисляет его площадь"""
        triangle_type = tr_type.undefined

        triangle_sides: Set[float|int] = {a, b, c}

        set_length: int = len(triangle_sides)

        match set_length:
            case 3:
                triangle_type = tr_type.scalene
            case 2:
                triangle_type = tr_type.isosceles
            case 1:
                triangle_type = tr_type.equilateral
            case _:
                return False

        match triangle_type:
            case tr_type.scalene:
                return self.__scaleneTriangle(a, b, c)
            case tr_type.isosceles:
                if a == b:
                    return self.__isoscelesTriangle(a, c)
                elif a == c:
                    return self.__isoscelesTriangle(a, b)
                elif b == c:
                    return self.__isoscelesTriangle(b, a)
            case tr_type.equilateral:
                return self.__equilateralTriangle(a)
            case _:
                return False
            
        
        