if __name__ == '__main__':
    words = {}
    order = 'sov'
    types = [
        'noun',
        'verb',
        'subject',
        'object',
        'adverb',
        'adjective',
        'pronun',
        'article',
        'interjection',
        'conjunction',
        'determiner',
        'preposition'
    ]
    while True:
        inp = input(': ')
        if inp == 'q':
            break
        elif inp == 'cl':
            print("\033[2J\033[H", end="")
        elif inp == 'define':
            word = input('word: ')
            mean = input('meaning: ')
            twpe = input('type(optional): ').lower()
            if twpe not in types:
                twpe = 'unknown'
            words[word] = (mean, twpe)
        elif inp == 'dictonary':
            for word in words:
                print(f'{word} -> [{words[word][0]}, {words[word][1]}]')
        elif inp == 'translate':
            print('Under contruction')
        elif inp == 'load':
            print('Under contruction')
        elif inp == 'save':
            print('Under contruction')
        elif inp == 'help':
            print("q cl define dictonary translate load save")