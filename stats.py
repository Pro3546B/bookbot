def wordcount(main):
    num_words = main.split()
    word_count = len(num_words)
    return word_count

def character_frequency(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
def sort_character_frequency(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_list
