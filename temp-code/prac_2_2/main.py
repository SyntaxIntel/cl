import numpy as np
import random
from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt

# Problem constants
BOUND_LOW, BOUND_UP = -5.0, 5.0  # Boundaries of the problem
NDIM = 2  # Number of dimensions

# Genetic Algorithm constants
POPULATION_SIZE = 100
P_CROSSOVER = 0.9
P_MUTATION = 0.1
MAX_GENERATIONS = 50
HALL_OF_FAME_SIZE = 5

# Create fitness and individual classes
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)


def init_individual(icls):
    """Initialize a random individual within the bounds"""
    return icls([random.uniform(BOUND_LOW, BOUND_UP) for _ in range(NDIM)])


def evaluate(individual):
    """
    Evaluation function: Sphere function
    f(x) = x[0]^2 + x[1]^2
    """
    return (sum(x * x for x in individual),)


def main():
    # Initialize toolbox
    toolbox = base.Toolbox()

    # Register operators
    toolbox.register("individual", init_individual, creator.Individual)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", evaluate)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
    toolbox.register("select", tools.selTournament, tournsize=3)

    # Create initial population
    population = toolbox.population(n=POPULATION_SIZE)

    # Create hall of fame to store best individuals
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    # Create statistics tracker
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)
    stats.register("max", np.max)

    # Run the evolution
    pop, logbook = algorithms.eaSimple(
        population,
        toolbox,
        cxpb=P_CROSSOVER,
        mutpb=P_MUTATION,
        ngen=MAX_GENERATIONS,
        stats=stats,
        halloffame=hof,
        verbose=True,
    )

    # Plot statistics
    gen = logbook.select("gen")
    fit_mins = logbook.select("min")
    fit_avgs = logbook.select("avg")
    fit_maxs = logbook.select("max")

    plt.figure(figsize=(10, 6))
    plt.plot(gen, fit_mins, "b-", label="Minimum Fitness")
    plt.plot(gen, fit_avgs, "r-", label="Average Fitness")
    plt.plot(gen, fit_maxs, "g-", label="Maximum Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Evolution Progress")
    plt.legend(loc="best")
    plt.grid(True)
    plt.savefig("evolution_progress.png")
    plt.close()

    # Print best solution
    best_solution = hof[0]
    print("\nBest solution:", best_solution)
    print("Best fitness:", best_solution.fitness.values[0])


if __name__ == "__main__":
    main()
