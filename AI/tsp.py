from itertools import permutations

def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    num_cities = len(tour)

    for i in range (num_cities - 1):
        total_distance += distance_matrix[tour[i]][tour[i + 1]]

    total_distance += distance_matrix[tour[-1]][tour[0]]

    return total_distance

def tsp_brute_force(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))

    all_possible_tours = permutations(cities)

    min_distance = float('inf')
    best_tour = None

    for tour in all_possible_tours:
        current_distance = calculate_total_distance(tour, distance_matrix)
        print(f"Tour: {tour}, Distance: {current_distance}")
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = tour

    return best_tour, min_distance

# Example usage

distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_tour, min_distance = tsp_brute_force(distance_matrix)

print(f"Best tour: {best_tour}")
print(f"Minimum distance: {min_distance}")
        