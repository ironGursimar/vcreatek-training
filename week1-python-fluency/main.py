import string
from collections import Counter


# Task 1
def word_count(text):
    """
    Returns a dictionary of word counts.
    Converts text to lowercase and removes punctuation.
    """
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.lower().translate(translator)

    words = cleaned_text.split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


# Task 2
def word_count_counter(text):
    """
    Returns word counts using collections.Counter.
    """
    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.lower().translate(translator)

    words = cleaned_text.split()
    return Counter(words)


# Task 3 (Loop)
def flatten_loop(list_of_lists):
    """
    Flattens a nested list using loops.
    """
    flattened = []

    for sublist in list_of_lists:
        for item in sublist:
            flattened.append(item)

    return flattened


# Task 3 (List Comprehension)
def flatten_comprehension(list_of_lists):
    """
    Flattens a nested list using list comprehension.
    """
    return [item for sublist in list_of_lists for item in sublist]


# Task 4
def mean_of_file(path):
    """
    Reads numbers from a file.
    Skips invalid lines and returns the mean.
    """
    numbers = []

    try:
        with open(path, "r") as file:
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    continue

        if not numbers:
            return None

        return sum(numbers) / len(numbers)

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None


# Task 5
# List comprehension creates the entire list in memory at once.
# Generator expression creates values one at a time, making it
# more memory efficient for large datasets.


# Task 6
if __name__ == "__main__":

    sample_text = "Hello, Python! Python is fun. Hello."

    print("Task 1: word_count()")
    result1 = word_count(sample_text)
    print(result1)

    print("\nTask 2: word_count_counter()")
    result2 = word_count_counter(sample_text)
    print(result2)

    print("\nDo both methods agree?")
    print(dict(result2) == result1)

    sample_lists = [[1, 2], [3, 4], [5]]

    print("\nTask 3: flatten using loop")
    print(flatten_loop(sample_lists))

    print("\nTask 3: flatten using list comprehension")
    print(flatten_comprehension(sample_lists))

    print("\nTask 4: mean_of_file()")
    mean = mean_of_file("numbers.txt")

    if mean is not None:
        print(f"Mean = {mean}")

    print("\nTesting missing file:")
    mean_of_file("missing.txt")
