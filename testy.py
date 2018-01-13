import time
import random
import genetyczny
import macierz

class Test:

    def __init__(self):
        self.scieżkaTSP = ['gr17.tsp', 'gr24.tsp', 'gr48.tsp', 'gr120.tsp']
        self.scieżkaATSP = ['br17.atsp', 'ftv33.atsp', 'ftv47.atsp', 'ftv70.atsp', 'ftv170.atsp']
        self.populationSize = [500, 1000, 1500]
        self.probability = [0.01, 0.04, 0.08, 0.1]

    def start(self):

        # Testy dla TSP
        for i in self.scieżkaTSP:
            for popu in self.populationSize:
                for prop in self.probability:
                    avgTime = 0
                    avgValue = 0
                    if i != 'gr120.tsp':
                        for k in range(10):
                            print(i + " " + str(popu) + " " + str(prop) + " " + str(k))
                            tab = macierz.creatematrix_TSP(i, 15)
                            x = self.runForTest(tab, prop, popu)
                            avgTime += x[0]
                            avgValue += x[1]

                        avgTime = avgTime/10
                        avgValue = avgValue/10
                        file = open("TestyTSP.txt", "a")
                        file.write(i + ";" + str(popu) + ";" + str(prop) + ";" + str(avgTime) + ";" + str(avgValue)
                                   + "\n")

                    else:
                        for k in range(5):
                            print(i + " " + str(popu) + " " + str(prop) + " " + str(k))
                            tab = macierz.creatematrix_TSP(i, 19)
                            x = self.runForTest(tab, prop, popu)
                            avgTime += x[0]
                            avgValue += x[1]

                        avgTime = avgTime / 5
                        avgValue = avgValue / 5
                        file = open("TestyTSP.txt", "a")
                        file.write(i + ";" + str(popu) + ";" + str(prop) + ";" + str(avgTime) + ";" + str(avgValue)
                                   + "\n")

########################################################################################################################
        # Testy dla ATSP
        for i in self.scieżkaATSP:
            for popu in self.populationSize:
                for prop in self.probability:
                    avgTime = 0
                    avgValue = 0
                    if i == 'br17.atsp':
                        for k in range(10):
                            print(i + " " + str(popu) + " " + str(prop) + " " + str(k))
                            tab = macierz.creatematrix_ATSP(i, 16, '9999')
                            x = self.runForTest(tab, prop, popu)
                            avgTime += x[0]
                            avgValue += x[1]

                        avgTime = avgTime / 10
                        avgValue = avgValue / 10
                        file = open("TestyATSP.txt", "a")
                        file.write(i + ";" + str(popu) + ";" + str(prop) + ";" + str(avgTime) + ";" + str(
                            avgValue) + "\n")

                    else:
                        for k in range(5):
                            tab = macierz.creatematrix_ATSP(i, 15, '100000000')
                            x = self.runForTest(tab, prop, popu)
                            avgTime += x[0]
                            avgValue += x[1]

                        avgTime = avgTime / 5
                        avgValue = avgValue / 5
                        file = open("TestyATSP.txt", "a")
                        file.write(i + ";" + str(popu) + ";" + str(prop) + ";" + str(avgTime) + ";" + str(
                            avgValue) + "\n")


    @staticmethod
    def runForTest(tab, probability=0.08, population=1000):
        start = time.clock()
        int = random.randint(0, 100)

        gen = genetyczny.Genetyczny(tab, probability, population)

        end = time.clock()
        total = end - start

        return total, gen.bestValue