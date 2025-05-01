import numpy as np


class AntColonyOptimizer:
    def __init__(self, distances, n_ants, n_iterations, decay=0.1, alpha=1.0, beta=2.0):
        """
        Initialize ACO for TSP
        :param distances: Matrix of distances between cities
        :param n_ants: Number of ants in the colony
        :param n_iterations: Number of iterations to run
        :param decay: Pheromone decay rate
        :param alpha: Pheromone weight factor
        :param beta: Distance weight factor
        """
        self.distances = distances
        self.n_cities = len(distances)
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        self.pheromone = np.ones((self.n_cities, self.n_cities)) / self.n_cities

    def solve(self):
        """Run the ACO algorithm and return the best path found"""
        best_path = None
        best_distance = float("inf")

        for iteration in range(self.n_iterations):
            paths = self._simulate_ants()
            distances = [self._calculate_path_distance(path) for path in paths]

            # Update best solution
            iteration_best_idx = np.argmin(distances)
            iteration_best_distance = distances[iteration_best_idx]
            if iteration_best_distance < best_distance:
                best_distance = iteration_best_distance
                best_path = paths[iteration_best_idx]

            # Update pheromones
            self._update_pheromone(paths, distances)

        return best_path, best_distance

    def _simulate_ants(self):
        """Simulate all ants constructing their paths"""
        paths = []
        for _ in range(self.n_ants):
            path = self._construct_solution()
            paths.append(path)
        return paths

    def _construct_solution(self):
        """Construct a single solution (path) for an ant"""
        path = []
        unvisited = set(range(self.n_cities))
        current = np.random.randint(self.n_cities)
        path.append(current)
        unvisited.remove(current)

        while unvisited:
            current = self._select_next_city(current, unvisited)
            path.append(current)
            unvisited.remove(current)

        return path

    def _select_next_city(self, current, unvisited):
        """Select the next city for an ant to visit based on pheromone and distance"""
        pheromone = np.array(
            [
                self.pheromone[current][j] if j in unvisited else 0
                for j in range(self.n_cities)
            ]
        )
        distance = np.array(
            [
                1 / self.distances[current][j] if j in unvisited else 0
                for j in range(self.n_cities)
            ]
        )

        # Calculate probabilities
        probabilities = (pheromone**self.alpha) * (distance**self.beta)
        probabilities = probabilities / probabilities.sum()

        return np.random.choice(self.n_cities, p=probabilities)

    def _calculate_path_distance(self, path):
        """Calculate the total distance of a path"""
        total_distance = 0
        for i in range(len(path)):
            total_distance += self.distances[path[i]][path[(i + 1) % self.n_cities]]
        return total_distance

    def _update_pheromone(self, paths, distances):
        """Update pheromone levels on all edges"""
        # Evaporation
        self.pheromone *= 1 - self.decay

        # Add new pheromone
        for path, distance in zip(paths, distances):
            amount = 1 / distance
            for i in range(len(path)):
                self.pheromone[path[i]][path[(i + 1) % self.n_cities]] += amount
                self.pheromone[path[(i + 1) % self.n_cities]][path[i]] += (
                    amount  # Symmetric TSP
                )
