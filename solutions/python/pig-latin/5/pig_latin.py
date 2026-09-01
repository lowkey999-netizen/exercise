"""
Code to Translate given pig latin words.
"""

vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l','m','n','p','q',     'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}

def translate_word(word):
    """
    Handles Words. Returns Words in pig-latin
    """
    if word[0] in vowels or word[0:2] == 'xr' or word[0:2] == 'yt':
        word = word +'ay'
        return word
    elif word[0] in consonants:
        for i in range(len(word)):
            if word[i] == 'q' and i + 1 < len(word) and word[i+1] == 'u':
                split = i+2
                break
            if word[i] == 'y' and i !=0:
                split = i
                break
            if word[i] in vowels:
                split = i
                break
        word = word[split:] + word[:split] + 'ay'
        return word

def translate(text):
    """
    Handles Sentences.
    """
    words = text.split()
    translated_words = []
    for word in words:
        translated_words.append(translate_word(word))
    return ' '.join(translated_words)