import numpy as np
import matplotlib.pyplot as plt
from aco import AntColonyOptimizer


def create_random_cities(n_cities):
    """Create random city coordinates"""
    return np.random.rand(n_cities, 2)


def calculate_distances(coordinates):
    """Calculate distance matrix between cities"""
    n_cities = len(coordinates)
    distances = np.zeros((n_cities, n_cities))
    for i in range(n_cities):
        for j in range(n_cities):
            distances[i][j] = np.sqrt(np.sum((coordinates[i] - coordinates[j]) ** 2))
    return distances


def plot_solution(coordinates, path, title, save_file=None):
    """Plot the TSP solution and optionally save it to a file"""
    plt.figure(figsize=(8, 6))

    # Plot cities
    plt.scatter(coordinates[:, 0], coordinates[:, 1], c="red", marker="o")

    # Plot path
    path_coords = np.concatenate([coordinates[path], [coordinates[path[0]]]])
    plt.plot(path_coords[:, 0], path_coords[:, 1], "b-")

    # Add city labels
    for i, coord in enumerate(coordinates):
        plt.annotate(
            f"City {i}", (coord[0], coord[1]), xytext=(5, 5), textcoords="offset points"
        )

    plt.title(title)
    if save_file:
        plt.savefig(save_file)
        print(f"Plot saved to {save_file}")
    else:
        plt.show()
    plt.close()


def main():
    # Problem parameters
    n_cities = 15
    n_ants = 20
    n_iterations = 100

    # Generate random cities
    coordinates = create_random_cities(n_cities)
    distances = calculate_distances(coordinates)

    # Create and run ACOun ACO
    aco = AntColonyOptimizer(
        distances=distances,
        n_ants=n_ants,
        n_iterations=n_iterations,
        decay=0.1,
        alpha=1.0,
        beta=2.0,
    )

    best_path, best_distance = aco.solve()

    # Plot solution and save image to file instead of showing it interactively instead of showing it interactively
    plot_solution(
        coordinates, best_path, f"TSP Solution\nBest Distance: {best_distance:.2f}",
        save_file="tsp_solution.png"
    )

    # Optionally, save the result details to a text file
    with open("tsp_solution_details.txt", "w") as f:
        f.write(f"Best path found: {best_path}\n")
        f.write(f"Total distance: {best_distance:.2f}\n")
    print("Solution details saved to tsp_solution_details.txt")


if __name__ == "__main__":
    main()
