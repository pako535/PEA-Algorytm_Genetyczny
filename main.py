import macierz
import random
import time
import genetyczny






#tab = macierz.creatematrix_TSP('gr120.tsp')
tab = macierz.creatematrix_ATSP('br17.atsp')
gen = genetyczny.Genetyczny(tab)
start = time.clock()
int = random.randint(0, 100)

print(tab, "\n\n")
#TS = tabu.Tabu(tab, 7, 1000)

gen.select_start_point()

end = time.clock()
total = end - start
print("{0:02f}s".format(total))




