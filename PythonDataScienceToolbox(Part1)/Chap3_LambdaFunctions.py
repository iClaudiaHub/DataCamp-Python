"""Chapter3 Lambda Function"""
# -------------------------------------------------------------------------------------------------------------------- #
# Pop quiz on lambda functions

# How would you write a lambda function add_bangs that adds three exclamation points '!!!' to the end of a string a?
# How would you call add_bangs with the argument 'hello'?
add_bangs = lambda a: a + '!!!'
add = add_bangs('hello')
print(add)

# -------------------------------------------------------------------------------------------------------------------- #
# Writing a lambda function you already know
echo_word = lambda word1, echo: word1 * echo
result = echo_word('hey', 5)
print(result)

# -------------------------------------------------------------------------------------------------------------------- #
# Map() and lambda functions

# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Print the result
print(shout_spells_list)

# -------------------------------------------------------------------------------------------------------------------- #
# Filter() and lambda functions

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6, fellowship)

#  Convert result to a list: result_list
result_list = list(result)

print(result_list)

# -------------------------------------------------------------------------------------------------------------------- #
# Reduce() and lambda functions

# Import reduce from functools
from functools import reduce

# Create a list of stings:stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)

print(result)


# -------------------------------------------------------------------------------------------------------------------- #
# Error handling with try-except

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word = ''
    shout_words = ""

    # Add exception handling with try-except
    try:
        echo_word = word1 * echo
        #         Concatenate "!!!" to echo_word: shout_words
        shout_words = echo_word + "!!!"
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

        # Return shout_words
    return shout_words


# Call shout_echo
shout_echo("particle", echo="accelerator")


# -------------------------------------------------------------------------------------------------------------------- #
# Error handling by raising an error

def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError("echo must be greater than or equal to 0")

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word


# Call shout_echo
shout_echo("particle", echo=5)

# -------------------------------------------------------------------------------------------------------------------- #
# Bringing it all together (1)

import pandas as pd

tweets_df = pd.read_csv('datasets/tweets.csv')

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x.startswith('RT'), tweets_df['text'])

# Create a list from filter object:res_list
res_list = list(result)

for tweet in res_list:
    print(tweet)


# -------------------------------------------------------------------------------------------------------------------- #
# Bringing it all together (2)

def count_entries(tweets_df, col_name='lang'):
    """Return a dictionary with counts of
        occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Add try block
    try:
        col = tweets_df[col_name]
        for entry in col:
            if entry in cols_count.keys():
                cols_count['entry'] += 1
            else:
                cols_count['entry'] = 1

        return cols_count
    except:
        'The DataFrame does not have a ' + col_name + ' column.'


# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)

# -------------------------------------------------------------------------------------------------------------------- #
# Bringing it all together (3)

def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

        # Return the cols_count dictionary
    return cols_count


# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Print result1
print(result1)


# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
