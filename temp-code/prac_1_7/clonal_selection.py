"""
Clonal Selection Algorithm (CSA) Implementation

This module implements the Clonal Selection Algorithm, an immune system-inspired
optimization algorithm for pattern recognition and function optimization.
"""

import numpy as np


class ClonalSelectionAlgorithm:
    def __init__(
        self,
        population_size,
        clone_rate,
        mutation_rate,
        random_cells_num,
        dimensions,
        bounds,
        fitness_function,
        max_iterations,
    ):
        self.population_size = population_size
        self.clone_rate = clone_rate
        self.mutation_rate = mutation_rate
        self.random_cells_num = random_cells_num
        self.dimensions = dimensions
        self.bounds = bounds
        self.fitness_function = fitness_function
        self.max_iterations = max_iterations
        self.population = self._initialize_population()
        self.best_solution = None
        self.best_fitness = float("-inf")
        self.fitness_history = []

    def _initialize_population(self):
        population = np.zeros((self.population_size, self.dimensions))
        for i in range(self.population_size):
            for j in range(self.dimensions):
                minimum_value, maximum_value = self.bounds[j]
                population[i, j] = np.random.uniform(minimum_value, maximum_value)
        return population

    def _clone_and_mutate(self, population, fitness_values):
        # Sort by fitness
        sorted_indices = np.argsort(fitness_values)[::-1]
        sorted_population = population[sorted_indices]

        # Clone
        number_of_clones = max(
            int(self.clone_rate * self.population_size), self.population_size
        )
        cloned_population = np.repeat(
            sorted_population, number_of_clones // self.population_size + 1, axis=0
        )[:number_of_clones]

        # Mutate
        for i in range(len(cloned_population)):
            mutation_values = np.random.normal(0, self.mutation_rate, self.dimensions)
            cloned_population[i] += mutation_values
            # Keep within bounds
            for j in range(self.dimensions):
                minimum_value, maximum_value = self.bounds[j]
                cloned_population[i, j] = np.clip(
                    cloned_population[i, j], minimum_value, maximum_value
                )

        return cloned_population

    def run(self):
        for iteration in range(self.max_iterations):
            # Calculate fitness
            current_fitness = np.array(
                [self.fitness_function(x) for x in self.population]
            )

            # Clone and mutate
            cloned_population = self._clone_and_mutate(self.population, current_fitness)
            cloned_fitness = np.array(
                [self.fitness_function(x) for x in cloned_population]
            )

            # Combine and select best
            combined_population = np.vstack((self.population, cloned_population))
            combined_fitness = np.append(current_fitness, cloned_fitness)
            best_indices = np.argsort(combined_fitness)[::-1][: self.population_size]
            self.population = combined_population[best_indices]

            # Add random cells for diversity
            if self.random_cells_num > 0:
                random_population = self._initialize_population()[
                    : self.random_cells_num
                ]
                random_indices = np.random.choice(
                    self.population_size, self.random_cells_num, replace=False
                )
                self.population[random_indices] = random_population

            # Update best solution
            current_best_fitness = np.max(combined_fitness)
            if current_best_fitness > self.best_fitness:
                self.best_fitness = current_best_fitness
                self.best_solution = combined_population[np.argmax(combined_fitness)]

            self.fitness_history.append(self.best_fitness)

            if (iteration + 1) % 10 == 0:
                print(
                    f"Iteration {iteration + 1}/{self.max_iterations}, Best fitness: {self.best_fitness}"
                )

        return self.best_solution, self.best_fitness, self.fitness_history
