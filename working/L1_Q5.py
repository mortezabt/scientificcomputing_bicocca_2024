"""Part1"""


def four_letter_words(message, n):
    words = message.split()
    four_letters = [w for w in words if len(w) == n]
    return four_letters


message = "The quick brown fox jumps over the lazy dog"
print(four_letter_words(message, 5))

""" Part2 """


def panagram(message):
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    for al in alphabet:
        if al in alphabet:
            print(True)
