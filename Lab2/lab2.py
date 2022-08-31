import random


def population(n):
   population = []
   while 1:
       genomes = []
       for j in range(n):
           g = round(random.random())
           genomes.append(g)
       if genomes not in population:
           population.append(genomes)
       if len(population) == 10:
           break

   return population


def fitness(population, n, t):
   fit = []
   for genomes in population:
       total = 0
       for g in range(len(genomes)):
           if genomes[g] == 1:
               total += data[g][1]

       fit.append([genomes, abs(total - t)])
       return fit


def select(population, n, mutation_threshold):
   selected_population = []
   ind = 0
   while 1:
       g1 = population[ind]
       g2 = population[ind + 1]
       crossed_g = crossover(g1, g2, n)

       if random.random() < mutation_threshold:
           m1 = mutate(crossed_g[0], n)
           m2 = mutate(crossed_g[1], n)
           selected_population.extend([m1, m2])
       else:
           selected_population.extend([crossed_g[0], crossed_g[1]])

       if len(selected_population) == 10:
           break

       ind += 2

   return selected_population


def mutate(g, n):
   mutated = []

   while len(mutated) < max(1, n // 3):
       m_i = round(random.random() * (n - 1))
       if m_i not in mutated:
           mutated.append(m_i)

   for m_g in mutated:
       if g[m_g] == 0:
           g[m_g] = 1
       else:
           g[m_g] = 0

   return g


def crossover(c1, c2, n):
   cross_index = round(random.random() * (n - 1))
   c1[cross_index:], c2[cross_index:] = c2[cross_index:], c1[cross_index:]
   return [c1, c2]


# def string_sequence(sequ):
# return " ".join(map(str,sequ))

def genetic_algo(population, n, t):
   f = fitness(population, n, t)
   sorted(f)
   seq = " ".join(map(str, f[0][0]))
   seq_fit = f[0][1]

   for cnt in range(1000):
       if seq_fit == 0:
           return [seq, seq_fit]

       new_pop = select(population, n, 0.5)
       population = new_pop

       f = fitness(population, n, t)
       sorted(f)

       if f[0][1] < seq_fit:
           seq = seq = " ".join(map(str, f[0][0]))
           seq_fit = f[0][1]

   return [seq, seq_fit]


data = []

f = open("input.txt", "r")
f = f.read()

ar = f.splitlines()
n_target = ar[0].split(" ")
n = int(n_target[0])
t = int(n_target[1])

for i in ar[1:]:
   data_element = i.split(' ')
   data_element[1] = int(data_element[1])
   data.append(data_element)

population = population(n)

for i in range(len(data) - 1):
   print(data[i][0], ", ", sep='', end="")
print(data[len(data) - 1][0])

best_subset = genetic_algo(population, n, t)

if best_subset[1] != 0:
   print(-1)
else:
   print(best_subset[0])

