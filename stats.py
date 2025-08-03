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
        chars = {
            "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0, " ": 0, ",": 0, ".": 0, "!": 0, "?": 0, "'": 0, ";": 0, "æ": 0, "â": 0, "ê": 0, "ë": 0, "ô": 0,
        }
        for char in file_text.lower():
            if char in chars:
               chars[char]  += 1
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
