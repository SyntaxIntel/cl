"""
Artificial Immune System Pattern Recognition for Structural Damage Classification
"""

import numpy as np
from sklearn.preprocessing import StandardScaler
from typing import List, Tuple


class ArtificialImmuneSystem:
    def __init__(
        self,
        num_detectors: int = 100,
        affinity_threshold: float = 0.7,
        mutation_rate: float = 0.1,
    ):
        """
        Initialize the Artificial Immune System for damage detection

        Args:
            num_detectors: Number of detector cells to generate
            affinity_threshold: Threshold for considering a match
            mutation_rate: Rate of mutation during detector generation
        """
        self.num_detectors = num_detectors
        self.affinity_threshold = affinity_threshold
        self.mutation_rate = mutation_rate
        self.detectors = None
        self.scaler = StandardScaler()

    def generate_detectors(self, training_data: np.ndarray) -> np.ndarray:
        """
        Generate a set of detector cells through negative selection

        Args:
            training_data: Normal condition data for training

        Returns:
            np.ndarray: Generated detector cells
        """
        # Scale the training data
        scaled_data = self.scaler.fit_transform(training_data)

        detectors = []
        attempts = 0
        max_attempts = self.num_detectors * 10

        while len(detectors) < self.num_detectors and attempts < max_attempts:
            # Generate random detector
            candidate = np.random.randn(training_data.shape[1])

            # Check if it doesn't match any normal sample
            if self._is_valid_detector(candidate, scaled_data):
                detectors.append(candidate)

            attempts += 1

        self.detectors = np.array(detectors)
        return self.detectors

    def _is_valid_detector(
        self, detector: np.ndarray, normal_samples: np.ndarray
    ) -> bool:
        """
        Check if a detector is valid (doesn't match normal samples)
        """
        affinities = self._calculate_affinity(detector, normal_samples)
        return not np.any(affinities > self.affinity_threshold)

    def _calculate_affinity(
        self, detector: np.ndarray, samples: np.ndarray
    ) -> np.ndarray:
        """
        Calculate affinity between a detector and samples using Euclidean distance
        """
        distances = np.linalg.norm(samples - detector, axis=1)
        return 1 / (1 + distances)  # Convert distance to affinity (0-1)

    def detect_damage(
        self, test_data: np.ndarray, threshold: float = None
    ) -> Tuple[List[bool], np.ndarray]:
        """
        Detect structural damage in test data

        Args:
            test_data: Data to test for damage
            threshold: Optional custom threshold for detection

        Returns:
            Tuple containing:
            - List of boolean flags indicating damage detection
            - Array of maximum affinities for each test sample
        """
        if self.detectors is None:
            raise ValueError("Detectors not generated. Call generate_detectors first.")

        if threshold is None:
            threshold = self.affinity_threshold

        # Scale the test data
        scaled_data = self.scaler.transform(test_data)

        # Calculate affinities with all detectors
        max_affinities = np.zeros(len(test_data))
        for i, sample in enumerate(scaled_data):
            affinities = self._calculate_affinity(sample, self.detectors)
            max_affinities[i] = np.max(affinities)

        # Detect damage based on threshold
        damage_detected = [affinity > threshold for affinity in max_affinities]

        return damage_detected, max_affinities

    def classify_damage(
        self, test_data: np.ndarray, damage_types: List[str] = None
    ) -> List[str]:
        """
        Classify the type of structural damage

        Args:
            test_data: Data to classify damage type
            damage_types: List of damage type labels

        Returns:
            List of predicted damage types
        """
        if damage_types is None:
            damage_types = ["Minor", "Moderate", "Severe"]

        _, affinities = self.detect_damage(test_data)

        # Classify based on affinity levels
        classifications = []
        for affinity in affinities:
            if affinity > 0.9:
                classifications.append(damage_types[2])  # Severe
            elif affinity > 0.8:
                classifications.append(damage_types[1])  # Moderate
            else:
                classifications.append(damage_types[0])  # Minor

        return classifications
