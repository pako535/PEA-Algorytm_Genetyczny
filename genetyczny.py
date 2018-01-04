
class Genetyczny:
    def __init__(self, tab):
        self.tab = tab



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

    # Metoda mutacji

class Chromosome:
    def __init__(self):
        self.path = []
        self.valueOfPath = int

        pass