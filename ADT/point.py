# ADT Titik pada bidang N dimensi

from math import sqrt


class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def dimension(self):
        return len(self.coordinates)

    def distance(self, other):
        return sqrt(sum((x-y)**2 for x, y in zip(self.coordinates, other.coordinates)))

    def __str__(self):
        return str(self.coordinates)
