def word_count(book_text):
    text = book_text.split()
    return len(text)

def letter_count(book_text):
    letters = {}
    text = book_text.lower()
    for char in text:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def sort_dict(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict