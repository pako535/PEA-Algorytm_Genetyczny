import random
import math
class Genetyczny:
    def __init__(self, tab):
        self.tab = tab
        self.crossPMX()



    def run(self):
        pass

    def select_start_point(self):

        x0 = []
        value_of_x0 = 0


        listOfVertices = []

        for i in range(len(self.tab)):
            listOfVertices.append(i)

        for i in range(len(listOfVertices) - 1):
            if not x0:
                value = min(filter(lambda x: x >= 0, self.tab[i, :]))
                value_of_x0 += value
                id = self.tab[i, :].tolist()
                id = id.index(value)
                #listOfVertices.pop(id)
                x0.append(i)
                x0.append(id)
            else:

                 newlist = self.tab[x0[len(x0) - 1], :].tolist()
                 mini = max(newlist)
                 for i in range(len(newlist)):
                    if i not in x0:
                        if newlist[i] < mini:
                            mini = newlist[i]
                            id = i

                 #listOfVertices.pop(id)
                 value_of_x0 += mini
                 x0.append(id)

        value_of_x0 += self.tab[x0[len(x0) - 1]][0]


        print("Ścieżka początkowa: ", x0)
        print("Wartość ścieżki początkowej: ", value_of_x0)
        return x0

    # Metody krzyżowania

    def crossPMX(self):

        x = [1, 2, 3, 4, 5, 6, 7, 8]
        y = [3, 2, 1, 4, 5, 6, 8, 7]

        # wybór zakrezu do krzyżowania
        while True:
            _range1 = random.choice(range(len(x)))
            _range2 = random.choice(range(len(x)))
            if _range1 != _range2 and math.fabs(_range2 - _range1) > 1:
                break

        if _range1 > _range2:
            temp = _range1
            _range1 = _range2
            _range2 = temp

        child1 = y[_range1:_range2]
        child2 = x[_range1:_range2]

        print(child1)

        for i in range(_range1 + 1, -1, -1):
            print(i)
            if x[i] not in child1:
                child1.insert(0, x[i])


        print(_range1, " ", _range2)
        print(child1, " ", child2)


    # Metoda mutacji

class Chromosome:
    def __init__(self):
        self.path = []
        self.valueOfPath = int

        pass