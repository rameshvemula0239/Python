For the word frequency computation:
from collections import Counter

def compute_word_frequency(text):

    """
    Computes the frequency of each word in the given text and returns a sorted list of tuples.
    """

    # Replace digits with spaces to consider only words
    text = re.sub(r'\d+', '', text)
    words = text.split()
    frequency = Counter(words)
    return sorted(frequency.items())

def main_word_frequency():

    """
    The main function to compute word frequency from an input string.
    """

    input_string = "which is better python 2 or python 3"
    frequency = compute_word_frequency(input_string)
    for word, count in frequency:
        print(f"('{word}', {count})")

# Example usage:
main_word_frequency()