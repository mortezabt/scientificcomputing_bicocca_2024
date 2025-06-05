titles = [
    "don quixote",
    "in search of lost time",
    "ulysses",
    "the odyssey",
    "war and peace",
    "moby dick",
    "the divine comedy",
    "hamlet",
    "the adventures of huckleberry finn",
    "the great gatsby",
]

titles_capital = []

for book in titles:
    book_capital = []
    for letter in book:
        letter = letter.capitalize()
        book_capital.append(letter)
    res = "".join(book_capital)
    titles_capital.append(res)
print(titles_capital)
