import random

# Function to generate a random dataset of 30 integers
def generate_random_dataset(size):
    return [random.randint(1, 100) for _ in range(size)]

# Function to perform the bubble sort algorithm
def bubble_sort(dataset):
    n = len(dataset)
    for i in range(n):
        for j in range(0, n - i - 1):
            if dataset[j] > dataset[j + 1]:
                dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]

# Main function to demonstrate the sorting process
def main():
    dataset = generate_random_dataset(30)
    print("Original dataset:")
    print(dataset)

    bubble_sort(dataset)
    print("Sorted dataset:")
    print(dataset)

if __name__ == "__main__":
    main()