"""
Example application of Artificial Immune System for Structural Damage Classification
"""

import numpy as np
def generate_sample_data(n_samples: int = 200):
    # Generate normal (healthy) structure data
    normal_data = np.random.normal(loc=0, scale=0.2, size=(n_samples, 4))

    # Generate damaged structure data; adding a pattern to one feature
    damaged_data = np.random.normal(loc=0.5, scale=0.3, size=(n_samples, 4))
    damaged_data[:, 1] += np.sin(np.linspace(0, 4 * np.pi, n_samples))

    return normal_data, damaged_data

    # Damaged condition data (with different severity levels)
def main():
    # Adjust parameters as needed (e.g., num_detectors or detector_radius)
    ais = ArtificialImmuneSystem(num_detectors=150, detector_radius=0.15)

    normal_train, damaged_test = generate_sample_data()

    print("Training the artificial immune system...")
    ais.train(normal_train)

    print("\nTesting classification...")
    all_test_data = np.vstack([normal_train[:50], damaged_test[:50]])
    true_labels = np.hstack([np.zeros(50), np.ones(50)])

    predictions = ais.classify(all_test_data)

    accuracy = np.mean(predictions == true_labels)
    print(f"Classification accuracy: {accuracy:.2%}")

    plt.figure(figsize=(10, 6))
    plt.scatter(
        all_test_data[predictions == 0, 0],
        all_test_data[predictions == 0, 1],
        label="Classified as Normal",
        alpha=0.6,
    )
    plt.scatter(
        all_test_data[predictions == 1, 0],
        all_test_data[predictions == 1, 1],
        label="Classified as Damaged",
        alpha=0.6,
    )
    plt.title("Structural Damage Classification Results")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.grid(True)

    plt.savefig("classification_output.png", dpi=300)
    plt.show()

    plt.axvline(x=threshold, color="black", linestyle="--", label="Detection Threshold")
if __name__ == "__main__":
    main()
    plt.title("Damage Classification")
    plt.legend()

    plt.tight_layout()
    plt.savefig("damage_classification_results.png")
    plt.close()


def main():
    # Generate synthetic structural data
    print("Generating synthetic structural data...")
    n_samples = 300
    n_features = 5
    normal_data, damage_data, true_damage_labels = generate_synthetic_data(
        n_samples, n_features
    )

    # Initialize and train the immune system
    print("\nInitializing Artificial Immune System...")
    ais = ArtificialImmuneSystem(
        num_detectors=150, affinity_threshold=0.75, mutation_rate=0.1
    )

    print("Generating detectors...")
    ais.generate_detectors(normal_data)

    # Test the system
    print("\nTesting the system...")

    # Evaluate on normal data
    normal_damage_detected, normal_affinities = ais.detect_damage(normal_data)
    false_positives = sum(normal_damage_detected)
    print(f"False Positive Rate: {false_positives / len(normal_data):.2%}")

    # Evaluate on damage data
    damage_detected, damage_affinities = ais.detect_damage(damage_data)
    true_positives = sum(damage_detected)
    print(f"True Positive Rate: {true_positives / len(damage_data):.2%}")

    # Classify damage types
    predicted_damage_types = ais.classify_damage(damage_data)

    # Calculate classification accuracy
    correct_classifications = sum(
        [p == t for p, t in zip(predicted_damage_types, true_damage_labels)]
    )
    accuracy = correct_classifications / len(true_damage_labels)
    print(f"\nDamage Classification Accuracy: {accuracy:.2%}")

    # Visualize results
    print("\nGenerating visualization...")
    plot_results(
        normal_affinities, damage_affinities, true_damage_labels, ais.affinity_threshold
    )
    print("Results have been saved as 'damage_classification_results.png'")


if __name__ == "__main__":
    main()
