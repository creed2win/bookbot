def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print("Number of words in text: " + str(word_count(file_contents)))
        print(char_count(file_contents))

def word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

def char_count(text):
    lower_text = text.lower()

    char_count = {}
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

main()