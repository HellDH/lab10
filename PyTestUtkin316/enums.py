import enum

class TriangleType(enum.Enum):
    undefined = "Неопределён" # Тип треугольника не определён
    scalene = "Разносторонний" # Треугольник разносторонний
    isosceles = "Равнобедренный" # Треугольник равнобедренный
    equilateral = "Равносторонний" # Треугольник равносторонний

class TriangleSidesType(enum.Enum):
    rectangular = "Прямоугольный"
    sharp_angled = "Остроугольный"
    obtuse_angle = "Тупоугольный"
