def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d):
    return d["num"]


def get_counted(chars_dict):
    listed = []
    for char, count in chars_dict.items():
        listed.append({"char": char, "num": count})
    listed.sort(reverse=True, key=sort_on)
    return listed
