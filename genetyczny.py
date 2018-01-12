import random
import math
import copy

class Genetyczny:
    def __init__(self, tab, probability, populationSize):
        self.tab = tab
        self.currentPopulation = []

        self.probabilityOfMutation = probability
        self.populationSize = populationSize
        # generowanie populacji początkowej
        self.generateTheInitialPopulation()
        self.ifBetter = 0
        self.bestSolution = self.currentPopulation[0].path
        self.bestValue = self.currentPopulation[0].valueOfPath

        self.run()


    def run(self):
        licznik = 0
        while(self.ifBetter < 50 and licznik < 1000):
            self.selection()
            self.crossAll()
            self.mutationAll()
            self.rateAll()
            licznik += 1
            # # self.displayPopulation()

    # Funkcja generująca populaje
    def generateTheInitialPopulation(self):
        # sizePopulation = len(self.tab


        for i in range(self.populationSize):
            chrom = Chromosome()
            chrom.generate(self.tab)
            self.currentPopulation.append(chrom)


        # print("GENERACJA POCZĄTKOWA")
        # for i in range(len(self.currentPopulation)):
        #     print(self.currentPopulation[i].path," ", self.currentPopulation[i].valueOfPath)

    def generateGreedyTheInitialPopulation(self):

        possibleVerticles  = []
        for i in range(len(self.tab)):
            possibleVerticles.append(i)

    # Metoda Selekcji Turniejowej

    def selection(self):
        self.podglad = {}
        newPopulation = []
        for i in range(self.populationSize):
            group = []
            value = []
            for j in range(len(self.tab)):
                tmp = random.choice(self.currentPopulation)
                group.append(tmp)
                value.append(tmp.valueOfPath)
            mini = min(value)
            chose = group[value.index(mini)]
            newPopulation.append(chose)
            self.podglad[mini] = chose
        self.currentPopulation = newPopulation

    # Metody krzyżowania

    def crossPMX(self, x, y):

        # x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # y = [5, 3, 6, 7, 8, 1, 2, 9, 4]

        # x = [3, 2, 1, 4, 8, 7, 6, 5, 9]
        # y = [4, 9, 6, 1, 2, 8, 5, 3, 7]

        # x = [7, 8, 4, 5, 6, 9, 1, 2, 3]
        # y = [5, 3, 6, 7, 8, 1, 2, 9, 4]

        # wybór zakrezu do krzyżowania
        while True:
            _range1 = random.choice(range(len(x)))
            _range2 = random.choice(range(len(x)))
            if _range1 != _range2 and math.fabs(_range2 - _range1) > 1:
                break

        # _range1 = 2
        # _range2 = 6


        if _range1 > _range2:
            temp = _range1
            _range1 = _range2
            _range2 = temp

        child1 = y[_range1:_range2]
        child2 = x[_range1:_range2]

        # map = dict(zip(child2, child1))
        map = [copy.copy(child2), copy.copy(child1)]
        dl = len(child1)


        # Wypełnienie dziecka bezkonfliktowymi elementami
        flag = False
        # Dziecka 1
        for i in range(_range1 - 1, -1, -1):
            if x[i] not in child1:
                child1.insert(0, x[i])
            else:
                for j in range(dl):    # child1 jest tylko dla rozmiaru nalezy przeszukiwać mape
                    if map[1][j] == x[i]:
                        tmp = map[0][j]
                        if tmp not in child1:
                            child1.insert(0, tmp)
                            break
                        else:
                            try:
                                if map[0][map[1].index(tmp)] not in child1:
                                    child1.insert(0, map[0][map[1].index(tmp)])
                                else:
                                    child1.insert(0, '_')
                                    flag = True
                            except:
                                child1.insert(0 ,'_')
                                flag = True





        for i in (range(_range2, len(x))):
            if x[i] not in child1:
                child1.append(x[i])
            else:
                for j in range(dl):    # child1 jest tylko dla rozmiaru nalezy przeszukiwać mape
                    if map[1][j] == x[i]:
                        tmp = map[0][j]
                        if tmp not in child1:
                            child1.append(tmp)
                            break
                        else:
                            try:
                                if map[0][map[1].index(tmp)] not in child1:
                                    child1.append(map[0][map[1].index(tmp)])
                                else:
                                    child1.append('_')
                                    flag = True
                            except:
                                child1.append('_')
                                flag = True

        if flag == True:
            self.repairCross(child1)

        flag = False
        # Dziecka 2
        for i in range(_range1 - 1, -1, -1):
            if y[i] not in child2:
                child2.insert(0, y[i])
            else:
                for j in range(dl):    # child1 jest tylko dla rozmiaru nalezy przeszukiwać mape
                    if map[0][j] == y[i]:
                        tmp = map[1][j]
                        if tmp not in child2:
                            child2.insert(0, tmp)
                            break
                        else:
                            try:
                                if map[1][map[0].index(tmp)]not in child2:
                                    child2.insert(0, map[1][map[0].index(tmp)])
                                else:
                                    child2.insert(0, '_')
                                    flag = True
                            except:
                                child2.insert(0, '_')
                                flag = True

        for i in (range(_range2, len(x))):
            if y[i] not in child2:
                child2.append(y[i])
            else:
                for j in range(dl):  # child1 jest tylko dla rozmiaru nalezy przeszukiwać mape
                    if map[0][j] == y[i]:
                        tmp = map[1][j]
                        if tmp not in child2:
                            child2.append(tmp)
                            break
                        else:
                            try:
                                if map[1][map[0].index(tmp)] not in child2:
                                    child2.append(map[1][map[0].index(tmp)])
                                else:
                                    child2.append('_')
                                    flag = True
                            except:
                                child2.append('_')
                                flag = True
        if flag == True:
            self.repairCross(child2)


        chrom1 = Chromosome()
        chrom1.path = child1
        chrom2 = Chromosome()
        chrom2.path = child2
        return chrom1, chrom2

    def repairCross(self, x):

        tab = []
        for i in range(len(x)):
            if i not in x:
                tab.append(i)

        for i in range(len(x)):
            if x[i] == '_':
                x[i] = random.choice(tab)
                tab.remove(x[i])

        return x

    def crossAll(self):
        tmp = []
        for i in self.currentPopulation:
             try:
                x = self.crossPMX(i.path, next(i.path))
                tmp.append(x[0])
                tmp.append(x[1])
             except:
                 x = self.crossPMX(i.path, self.currentPopulation[0].path)
                 tmp.append(x[0])
                 tmp.append(x[1])

        self.currentPopulation = tmp

    # Metoda mutacji

    def mutationAll(self):

        for i in self.currentPopulation:
            x = random.randint(0, 1000)

            if x <= 1000*self.probabilityOfMutation:
                a = random.randint(0, len(self.tab) - 1)
                b = random.randint(0, len(self.tab) - 1)

                i.path[a], i.path[b] = i.path[b], i.path[a]

    def rateAll(self):
        flag = False
        for i in self.currentPopulation:
            i.calculateValueOfThePath(self.tab)
            if i.valueOfPath < self.bestValue:
                self.bestValue = i.valueOfPath
                self.bestSolution = i.path
                self.displayBest()
                self.ifBetter = 0
                flag = True

        if flag == False:
            self.ifBetter += 1

    def displayPopulation(self):
        for i in self.currentPopulation:
            print(i.valueOfPath, " -> ", i.path)

    def displayBest(self):
        print("#########################################")
        print("## Najlepszy wynik: ", self.bestValue)
        print("## Ścieżka: ", self.bestSolution)
        print("#########################################")

class Chromosome:

    def __init__(self):
        self.path = []
        self.valueOfPath = 0

    def generate(self, tab):
        listOfVertices = []
        self.path = []
        self.valueOfPath = 0
        for i in range(len(tab)):
            listOfVertices.append(i)

        dlTab = len(tab)
        for i in range(dlTab):
            tmp = random.choice(listOfVertices)
            listOfVertices.remove(tmp)
            self.path.append(tmp)
            if i != 0:
                self.valueOfPath += tab[self.path[i - 1]][self.path[i]]
            if i == dlTab - 1 :
                self.valueOfPath += tab[self.path[i]][self.path[0]]

        # print(self.path,"\nWartość: ",self.valueOfPath)

    def calculateValueOfThePath(self, tab):
        dlTab = len(tab)
        for i in range(dlTab):
            if i != 0:
                self.valueOfPath += tab[self.path[i - 1]][self.path[i]]
            if i == dlTab - 1:
                self.valueOfPath += tab[self.path[i]][self.path[0]]