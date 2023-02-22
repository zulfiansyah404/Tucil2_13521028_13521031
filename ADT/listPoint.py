# ADT List of Point

class ListPoint:
    def __init__(self):
        self.listPoint = []

    def dimension(self):
        return self.listPoint[0].dimension()

    def size(self):
        return len(self.listPoint)

    def get(self, index):
        return self.listPoint[index]

    def add(self, point):
        self.listPoint.append(point)

    def isEmpty(self):
        return self.size() == 0

    def getClosestPointPairByBruteForce(self):
        # Mencari pasangan titik terdekat dengan brute force
        countEucledian = 0
        minDistance = float('inf')
        closestPointPair = None
        N = self.size()
        for i in range(N):
            for j in range(i+1, N):
                countEucledian += 1
                distance = self.get(i).distance(self.get(j))
                if distance < minDistance:
                    minDistance = distance
                    closestPointPair = (self.get(i), self.get(j))

        closestPointPair = (
            closestPointPair[0], closestPointPair[1], countEucledian)
        return closestPointPair

    def getClosestPointPairByDivideAndConquer(self):
        countEucledian = 0
        # Base Case
        if self.isEmpty():
            return None

        elif self.size() == 1:
            return None

        elif self.size() == 2:
            return (self.get(0), self.get(1), 1)

        # Relasi Rekurens
        else:
            # Urutkan list berdasarkan koordinat x
            self.listPoint.sort(key=lambda point: point.coordinates[0])

            # Bagi list menjadi 2 bagian
            list1 = ListPoint()
            list2 = ListPoint()
            for i in range(self.size()):
                if i < self.size() // 2:
                    list1.add(self.get(i))
                else:
                    list2.add(self.get(i))

            # Cari pasangan titik terdekat dari kedua bagian
            pair1 = list1.getClosestPointPairByDivideAndConquer()
            pair2 = list2.getClosestPointPairByDivideAndConquer()

            closestPointPair = None

            # Lalu bandingkan dengan kedua bagian tersebut
            if pair1 == None:
                closestPointPair = pair2
                countEucledian += pair2[2]
            elif pair2 == None:
                closestPointPair = pair1
                countEucledian += pair1[2]
            else:
                countEucledian += pair1[2] + pair2[2]
                if pair1[0].distance(pair1[1]) < pair2[0].distance(pair2[1]):
                    closestPointPair = pair1
                else:
                    closestPointPair = pair2

            minDistance = closestPointPair[0].distance(closestPointPair[1])

            # Proses Conquer
            x = self.get(self.size()//2).coordinates[0]
            list3 = ListPoint()
            for i in range(self.size()):
                if abs(self.get(i).coordinates[0] - x) < minDistance:
                    list3.add(self.get(i))

            # Mencari pasangan titik terdekat dari titik-titik yang berada di antara kedua bagian
            for i in range(list3.size()):
                for j in range(i+1, min(i+8, list3.size())):
                    countEucledian += 1
                    if list3.get(i).distance(list3.get(j)) < minDistance:
                        closestPointPair = (list3.get(i), list3.get(j))

            closestPointPair = (
                closestPointPair[0], closestPointPair[1], countEucledian)
            return closestPointPair
