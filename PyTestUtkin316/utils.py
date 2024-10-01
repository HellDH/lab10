from .enums import TriangleType, TriangleSidesType
from .enums import TriangleType as tr_type
from typing import Set, Tuple

class TriangleProblemOne:
    """Класс с методами из задания 1 , лаб. работы 3"""

    def __scaleneTriangle(self,
                          a: float,
                          b: float,
                          c: float) -> float:
        """Вычисляет площадь разностороннего треугольника по формуле Герона"""
        half_perimeter = (a + b + c) / 2

        return 0.5 ** ((half_perimeter - a) * \
                       (half_perimeter - b) * \
                       (half_perimeter - c))
    
    def __isoscelesTriangle(self,
                            a: float,
                            b: float) -> float:
        """Вычисляет площадь равнобедренного треугольника по двум сторонам"""
        h = 0.5 * (0.5 ** (4 * (a ** 2) - (b ** 2))) # Высота треугольника

        return 0.5 * b * h
    
    def __equilateralTriangle(self,
                              a: float) -> float:
        """Вычисляет площадь равностороннего треугольника через высоту"""
        h = (a * (0.5 ** 3)) / 2 # Высота треугольника

        return 0.5 * a * h
    
    def defineTriangle(self,
                       a: float,
                       b: float,
                       c: float) -> Tuple[float, TriangleType] | bool:
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
                return (self.__scaleneTriangle(a, b, c), triangle_type)
            case tr_type.isosceles:
                if a == b:
                    return (self.__isoscelesTriangle(a, c), triangle_type)
                elif a == c:
                    return (self.__isoscelesTriangle(a, b), triangle_type)
                elif b == c:
                    return (self.__isoscelesTriangle(b, a), triangle_type)
            case tr_type.equilateral:
                return (self.__equilateralTriangle(a), triangle_type)
            case _:
                return False
            
class TriangleProblemTwo:
    def defineTriangleSides(self,
                            a: float,
                            b: float,
                            c: float) -> TriangleSidesType | bool:
        
        sides = [a, b, c]
        
        biggest = sides.index(max(sides))

        sides.remove(sides[biggest])

        if sides[biggest] == ((sides[0] ** 0.5) + (sides[1] ** 0.5)):
            return TriangleSidesType.rectangular
        elif sides[biggest] > ((sides[0] ** 0.5) + (sides[1] ** 0.5)):
            return TriangleSidesType.obtuse_angle
        elif sides[biggest] < ((sides[0] ** 0.5) + (sides[1] ** 0.5)):
            return TriangleSidesType.sharp_angled
        