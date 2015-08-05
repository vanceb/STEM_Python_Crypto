MORSE = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': ' '
}

class Morse:
    _message = ''
    _decode = {}

    def __init__(self, msg = ''):
        self.setMessage(msg)
        self._decode = self._invert(MORSE)

    def _invert(self, dict):
        inverted = {}
        for key in dict:
            inverted[dict[key]] = key
        return inverted

    def _decodeMorse(self, morse):
        msg = []
        for symbol in morse:
            msg.append(self._decode[symbol])
        return msg

    def _decodeMorseString(self, morseString):
        msg = ''
        words = morseString.split("   ")
        for word in words:
            for symbol in word.split():
                msg += self._decode[symbol]
            msg += " "
        return msg.strip()

    def _encodeMorse(self, msg):
        morse = []
        for letter in msg:
            morse.append(MORSE[letter])
        return morse

    def _encodeMorseString(self, msg):
        morseString = ""
        morse = self._encodeMorse(msg)
        for symbol in morse:
            if symbol == ' ':
                morseString += "   "
            else:
                morseString += symbol + " "
        return morseString.strip()

    def setMessage(self, msg):
        self._message = ''.join(msg)
        self._message = self._message.lower()

    def setMorse(self, morse):
        self._message = ''.join(self._decodeMorse(morse))

    def setMorseString(self, morseString):
        self.setMessage(self._decodeMorseString(morseString))

    def getMessage(self):
        return self._message

    def getMorse(self):
        return self._encodeMorse(self._message)

    def getMorseString(self):
        return self._encodeMorseString(self._message)

    def playMorse(self):
        # No easy cross-platform way of making a beep!!!
        pass
