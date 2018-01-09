import macierz
import random
import time
import genetyczny






#tab = macierz.creatematrix_TSP('gr120.tsp')
tab = macierz.creatematrix_ATSP('br17.atsp')
gen = genetyczny.Genetyczny(tab, 0.01)
start = time.clock()
int = random.randint(0, 100)

print("\n\n",tab, "\n\n")
#TS = tabu.Tabu(tab, 7, 1000)

# gen.generateTheInitialPopulation()

end = time.clock()
total = end - start
print("{0:02f}s".format(total))




