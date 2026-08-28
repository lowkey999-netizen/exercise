"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    Parameters:
        title (str): Essay title that needs title casing.

    Returns:
        str: The title string in title case (first letters capitalized).
    """
    new = title.split()
    new_2 = []
    for i in new:
        new_1 = i.title()
        new_2.append(new_1)
    return " ".join(new_2)


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    Parameters:
        sentence (str): A sentence to check.

    Returns:
        bool: Is the sentence punctuated correctly?
    """
    new = sentence.strip()
    return new.endswith(".")


def clean_up_spacing(sentence):
    """Trim any leading or trailing whitespace from the sentence.

    Parameters:
        sentence (str): A sentence to clean of leading and trailing space characters.

    Returns:
        str: A sentence that has been cleaned of leading and trailing space characters.
    """
    return " ".join(sentence.split())

def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    Parameters:
        sentence (str): A sentence to replace words in.
        old_word (str): The word to replace.
        new_word (str): The replacement word.

    Returns:
        str: Input sentence with new words in place of old words.
    """

    return sentence.replace(old_word, new_word)
