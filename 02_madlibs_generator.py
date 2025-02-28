# Replace the replacable words with the values that user provides

with open('story.txt', 'r') as story_file:
    story = story_file.read()

replacables = [[letter for letter in word if letter != '<' and letter != '>' and letter != ','] for word in story.split() if word.startswith('<')]
print(replacables)
words = []
for replacalble in replacables:
    word = ''.join(replacalble[::])
    words.append(word)
words = set(words)

for word in words:
    a = input(f'Enter the value for {word}: ')
    print(f'replacing {a}')
    story = story.replace(f"<{word}>", a)

with open('story2.txt', 'w') as f:
    f.write(story)
