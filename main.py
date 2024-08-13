def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print("Number of words in text: " + str(word_count(file_contents)))

def word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

main()