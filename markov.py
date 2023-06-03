"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    
    text = open(file_path).read()

    return text


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    chainwords = text_string.split()
    # print(chainwords)
    # chainwords = text_string.split()

    for i in range(len(chainwords) - int(n)):
       
        key_list = []

        for j in range(i, i + int(n)):
            key_list.append(chainwords[j])
        
        key_tuple = tuple(key_list)

        value = chainwords[i + int(n)]
        
        if key_tuple not in chains:
            chains[key_tuple] = []

        chains[key_tuple].append(value)
        
    # your code goes here

    # print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""
    # print(chains)
    words = []

    # Step 1: Pick a Starting Point¶
    random_key = choice(list(chains.keys()))
    # ('Would', 'you', 'could', 'you', 'in')
    # print(random_key)
    words.extend(random_key)
    # ['Would', 'you', 'could', 'you', 'in']
    # print(words)
    random_choice = choice(chains[random_key])
    # ('Would', 'you', 'could', 'you', 'in'): ['a', 'a']
    # => random_chocie = 'a'
    
    # Step 2: Choose Your Next Word
    while random_key in chains:

        random_key = tuple(list(random_key[1:]) + [random_choice])

        words.append(random_choice)

        if random_key in list(chains.keys()):
            random_choice = choice(chains[random_key])
        

    # return words
    return ' '.join(words) 


# input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(sys.argv[1])

n = sys.argv[2]

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains)

print(random_text)
