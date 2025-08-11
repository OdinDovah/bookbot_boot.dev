def get_word_count(filepath):
    with open(filepath) as f:
        file_text = f.read()
        word_count = 0
        for word in file_text.split():
            word_count += 1
        return word_count


def get_char_count(filepath):
    with open(filepath) as f:
        file_text = f.read()
        chars = {}
        for char in file_text.lower():
            if char in chars:
                chars[char] += 1
            else:
                chars.update({char: 1})
        return chars


def sort_on(count):
    return count["num"]


def sorted_count(char_count):
    chars = []
    for char in char_count.items():
        if char[0].isalpha():
            chars.append({"char": char[0], "num": char[1]})
    chars.sort(reverse=True, key=sort_on)
    return chars
