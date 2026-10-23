from strands import Agent, tool
from strands.vended_tools import file_editor
from strands_tools import generate_image

# commenting this tool definition and having the messed tool definition below
# would make us think the agent wouldn't choose that tool (letter_mixer)
# but since it is defined in the code itself, it still decided to use the tool
@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count occurrences of a specific letter in a word.

    Args:
        word (str): The input word to search in
        letter (str): The specific letter to count

    Returns:
        int: The number of occurrences of the letter in the word
    """
    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())

@tool
def letter_mixer(word: str, letter: str) -> int:
    """
    Mix occurrences of a specific letter in a word.

    Args:
        word (str): The input word to search in
        letter (str): The specific letter to mix

    Returns:
        int: The word with the mixed  letter in there
    """
    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())


#agent = Agent(tools=[letter_counter, file_editor, generate_image])
agent = Agent(tools=[letter_mixer, letter_counter, file_editor, generate_image])
#agent('How are you doing today?')
#agent('Draw me an image of superman, in halloween style')
agent('How many letter R\'s are in the word "strawberry"? Write the answer to answer.txt. Draw the answer with a halloween themed number')