#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.

from counter import _Counter
from collections import Counter
import random
import numpy
from deap import creator, tools, base, algorithms


creator.class_replacers[Counter] = _Counter

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", Counter, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_int", random.randint, 0, 10)

toolbox.register("individual", tools.initRepeat, creator.Individual,
        toolbox.attr_int, 15)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalCounter(individual):
    fit = 0
    for key, count in individual.items():
        fit += abs(key - 5) * count
    return -fit, 

def mateCounter(ind1, ind2, indpb = 0.1):
    for key in ind1:
        if random.random() < indpb:
            ind1[key], ind2[key] = ind2[key], ind1[key]
    return ind1, ind2

def mutateCounter(individual):
    if random.randint(0,1) > 0:
        individual.update([random.randint(0,10)])
    else:
        val = random.randint(0,10)
        individual.subtract([val])
        if individual[val] < 0:
            del individual[val]
        
    return individual,

toolbox.register("evaluate", evalCounter)
toolbox.register("mate", mateCounter, indpb = 0.1)
toolbox.register("mutate", mutateCounter)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb =0.2, ngen=40,
            stats=stats, halloffame=hof, verbose=True)
    return pop, log, hof

if __name__ == "__main__":
    _,_,hof = main()
    print(hof[0])
    print(hof[0].fitness)
    print(evalCounter(hof[0]))
