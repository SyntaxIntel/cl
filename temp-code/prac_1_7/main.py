import numpy as np
import matplotlib.pyplot as plt
from clonal_selection import ClonalSelectionAlgorithm


def sphere_function(vector):
    """Sphere function (optimum at vector=0)"""
    return -np.sum(vector**2)


def rastrigin_function(vector):
    """Rastrigin function (optimum at vector=0)"""
    number_of_dimensions = len(vector)
    return -(
        10 * number_of_dimensions + np.sum(vector**2 - 10 * np.cos(2 * np.pi * vector))
    )


if __name__ == "__main__":
    # Problem setup
    number_of_dimensions = 5  # reduced dimensions for faster execution
    parameter_bounds = [(-5.12, 5.12) for _ in range(number_of_dimensions)]

    # Algorithm parameters
    algorithm_parameters = {
        "population_size": 30,
        "clone_rate": 5,
        "mutation_rate": 0.3,
        "random_cells_num": 3,
        "dimensions": number_of_dimensions,
        "bounds": parameter_bounds,
        "max_iterations": 50,
    }

    # Test functions
    optimization_functions = [
        ("Sphere", sphere_function),
        ("Rastrigin", rastrigin_function),
    ]

    # Run experiments
    optimization_results = []
    for function_name, optimization_function in optimization_functions:
        print(f"\nOptimizing {function_name} function:")
        algorithm = ClonalSelectionAlgorithm(
            **algorithm_parameters, fitness_function=optimization_function
        )
        best_solution, best_fitness, optimization_history = algorithm.run()
        optimization_results.append(
            (function_name, [-x for x in optimization_history])
        )  # Convert to minimization

    # Plot results
    plt.figure(figsize=(10, 6))
    for function_name, optimization_history in optimization_results:
        plt.semilogy(optimization_history, label=function_name)

    plt.xlabel("Iteration")
    plt.ylabel("Objective Value (log scale)")
    plt.title("Clonal Selection Algorithm Optimization Progress")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.savefig("optimization_progress.png")
    plt.show()
