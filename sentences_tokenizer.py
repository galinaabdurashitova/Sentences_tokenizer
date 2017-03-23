# With no comments there's 25 lines :)

# This function splits text for blocks that are probably sentences
def lines_splitter(text):
    for symbol in '.!?…':
        text = text.replace(symbol + ' ', symbol)  # To escape empty elements
        text = text.replace(symbol, '\n' + symbol + '\n')  # \n is a sign for separation
    text = text.replace(': "', ':\n"')  # Some quotes can be sentences as well
    return [line for line in text.split('\n') if line != '']  # Returns array of sentence-blocks and punctuation

# This function makes text tokenized
def tokenizer(text):
    lines = lines_splitter(text)
    capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТТУФХЦЧШЩЪЫЬЭЮЯ"'  # No RegEx to make the process faster
    sentences, line = [], lines[0]
    for i in range(1, len(lines)):  # Looking at the pair of elements
        if lines[i][0] not in capitals:  # If the this element doesn't look like a beginning of a sentence
            line = line + ' ' + lines[i]  # It should be joined to the previous part
        else:
            sentences.append(line)
            line = lines[i]  # Otherwise remember the previous sentence and start the new one
    sentences.append(line)  # Last sentence
    return sentences

if __name__ == '__main__':
    with open('C:/Users/S451/Desktop/aa/long_poem.txt', 'r', encoding='utf-8') as f:
        f = f.read()
    tokens = tokenizer(f)
#    for sentence in tokens:
#        print(sentence)
