"""
Iterables.
"""
TOKENS = '''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789'''


class SentenceIterator:
    """
    Iterator for Sentence class.
    """
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.text):
            raise StopIteration
        word = self.text[self.index]
        self.index += 1
        return word


class Sentence:
    """
    Class-container.

    Processes sentences.
    """
    def __init__(self, text):
        if not isinstance(text, str):
            raise TypeError(f'Input data must be str, not {type(text).__name__}.')
        if text[-1] not in '.?!':
            raise ValueError('Entered sentence must be complete.')
        self.text = text

    def __repr__(self):
        return f"<Sentence(words={len(self.words)}, other_chars={len(self.other_chars)})>"

    def __iter__(self):
        return SentenceIterator(self.words)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return ' '.join(self.words[item])
        return self.words[item]

    def _words(self):
        """
        _words() -> generator object

        Generator for getting words from sentence.
        """
        for word in self.text.split():
            yield ''.join(char for char in word if char not in TOKENS)

    @property
    def words(self):
        """
        words() -> str[]

        Returns a list of words in sentence.
        """
        return [word for word in self._words()]

    @property
    def other_chars(self):
        """
        other_chars() -> str[]

        Returns a list of non-words in sentence.
        """
        other_characters = []
        for char in self.text:
            if char in TOKENS:
                other_characters += char
        return other_characters


print(Sentence('Hello word!'))

print('\n_words() method is a generator:')
print(Sentence('Hello world!')._words())

print("\nGet item by index (Sentence('Hello world!')[0]):")
print(Sentence('Hello world!')[0])

print("\nSlicing (Sentence('Hello world!')[:]):")
print(Sentence('Hello world!')[:])

print('\nUsage in for loop:')
for i in Sentence('Hello world!'):
    print(i)

print('\niter() returns SentenceIterator:')
print(iter(Sentence('Hello world!')))
