
def fitness(self):
    cdef numpy.float64_t cost = 0
    cdef int index
    cdef numpy.ndarray[numpy.float64_t, ndim=2] graph = self.graph
    cdef numpy.ndarray[numpy.int64_t, ndim=1] genome = self.get_genome()
    for index in range(1, GENOME_LENGTH):
        cost += graph[genome[index-1], genome[index]]
    cost += graph[genome[GENOME_LENGTH-1], genome[0]]
    return cost
	
	

positions = (randrange(GENOME_LENGTH), randrange(GENOME_LENGTH))
cdef int start = min(positions)
cdef int stop = max(positions)
cdef int counter
cdef int counter2
cdef numpy.int64_t gene
cdef numpy.ndarray[numpy.int64_t, ndim=1] mother_genome = mother.get_genome()
cdef numpy.ndarray[numpy.int64_t, ndim=1] father_genome = father.get_genome()
son = father.copy()
daughter = mother.copy()
cdef numpy.ndarray[numpy.int64_t, ndim=1] son_genome = son.get_genome()
cdef numpy.ndarray[numpy.int64_t, ndim=1] daughter_genome = son.get_genome()
if start == stop:
    return (son, daughter)
# Crossover for mother-son.
for gene in mother_genome[start:stop]:
    for counter in range(GENOME_LENGTH):
        if son_genome[counter] == gene:
            son_genome[counter] = -1
for counter in range(start, stop):
    if son_genome[counter] != -1:
        for counter2 in range(start):
            if son_genome[counter2] == -1:
                son_genome[counter2] = son_genome[counter]
                son_genome[counter] = -1
        for counter2 in range(stop, GENOME_LENGTH):
            if son_genome[counter2] == -1:
                son_genome[counter2] = son_genome[counter]
                son_genome[counter] = -1
son_genome[start:stop] = mother_genome[start:stop]