import string


def create_morse_dictionary():
    # Creating morse alphabet list.
    morse_alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    # Creating alphabet list.
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    # Creating a morse dictionary by zipping the alphabet list and morse list.
    morse_dict = dict(zip(alphabet_list, morse_alphabet))

    return morse_dict


def calc_transformations(words):
    # Empty morse word list created
    morse_words = []

    # A for loop runs over each of the words in the list of words.
    for word in words:
        # An empty string is declared.
        morse_word = ""

        # A nested for loop runs over each letter and adds it to the empty string
        for letter in word:
            morse_word += morse_dictionary[letter]

        # If the word does not already exist, it is added to the list morse_words.
        if morse_word not in morse_words:
            morse_words.append(morse_word)

    # The length of the morse_words is returned.
    return len(morse_words)


word_list = ["gin", "zen", "gig", "msg"]

morse_dictionary = create_morse_dictionary()

transformations = calc_transformations(word_list)

print(word_list)
print("Number of different transformations: " + str(transformations))
