import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '/'}

if len(sys.argv) > 1:
    ls = []
    for i in range(1, len(sys.argv)):
        for j in sys.argv[i]:
            if not j.isalnum() and not j.isspace():
                print('ERROR')
                exit()
        ls.append(sys.argv[i])
    string = ' '.join(ls)
    morse = []
    for i in string:
        for key, value in MORSE_CODE_DICT.items():
            if key == i.upper():
                morse.append(value)
    encoded = ' '.join(morse)
    print(encoded)