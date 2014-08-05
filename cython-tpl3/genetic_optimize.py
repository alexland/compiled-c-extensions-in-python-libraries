#!/usr/local/bin/python3

def fitness(self):
    cost = 0
    for index in range(1, GENOME_LENGTH):
        cost += GRAPH[self.genome[index-1], self.genome[index]]
    cost += GRAPH[self.genome[GENOME_LENGTH-1], self.genome[0]]
    return cost
	
	
def fitness(self):
    cdef numpy.float64_t cost = 0
    cdef int index
    cdef numpy.ndarray[numpy.float64_t, ndim=2] graph = self.graph
    cdef numpy.ndarray[numpy.int64_t, ndim=1] genome = self.get_genome()
    for index in range(1, GENOME_LENGTH):
        cost += graph[genome[index-1], genome[index]]
    cost += graph[genome[GENOME_LENGTH-1], genome[0]]
    return cost