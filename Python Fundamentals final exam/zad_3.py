initial_definitions = input().split(' | ')

dictionary = {}

for current_definition in initial_definitions:
    word, definition = current_definition.split(': ')

    if word not in dictionary:
        dictionary[word] = []
        dictionary[word].append(definition)
    else:
        dictionary[word].append(definition)

tested_words = input().split(' | ')

command = input()


if command == 'Test':
    for word in tested_words:
        if word in dictionary:
            print(f"{word}:")
            for definition in dictionary[word]:
                print(f"-{definition}")


elif command == 'Hand Over':
    for word in dictionary:
        print(word, end=' ')