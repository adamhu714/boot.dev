def markdown_to_text(doc_content):
    lines = doc_content.split("\n")
    linesWithoutHash = [line if line == "" or line[0] != "#" else line[1:].lstrip() for line in lines]
    wordsWithoutHash = [line.split(" ") for line in linesWithoutHash]
    linesWithoutHashRemovedAsterisks = [" ".join(map(remove_asterisks_from_words, words)) for words in wordsWithoutHash]
    return "\n".join(linesWithoutHashRemovedAsterisks)

def remove_asterisks_from_words(word):
    if len(word) < 2:
        return word
    if word[0] == "*":
        word = word[1:]
    if word[-1] == "*":
        word = word[:-1]
    return word