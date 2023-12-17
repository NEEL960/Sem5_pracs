import random

class Individual:
    def __init__(self,x):
        self.x = x
        self.fitness = self.x**2

    def crossover(self,partner):
        child_x = (self.x + partner.x) / 2.0
        return Individual(child_x)
    
    def mutate(self):
        mutation = (random.random() - 0.5) * 0.1
        self.x += mutation
        return self

def initialize_population(population_size):
    population = [Individual(-10 + random.random() * 20) for _ in range(population_size)]
    return population

def select_parent(population):
    return random.choice(population)


max_generations = int(input("Enter the number of generations : "))
population_size = int(input("Enter the population size : "))

population = initialize_population(population_size)

for generation in range(max_generations):
    new_population = []

    for _ in range(population_size):
        parent1 = select_parent(population)
        parent2 = select_parent(population)
        child = parent1.crossover(parent2)

        if random.random() < 0.1:
            child = child.mutate()
        
        new_population.append(child)

    population = new_population
    population.sort(key=lambda ind: ind.fitness, reverse=True)

    print(f"Generation {generation} Best fitness = {population[0].fitness}")

print(f"Best solution : {population[0].x}")
