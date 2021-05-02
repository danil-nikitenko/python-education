"""Multiple function arguments"""


# edit the functions prototype and implementation
def foo(a, b, c, *args):
    """Returns the length of args"""

    return len(list(args))


def bar(a, b, c, **kwargs):
    """Returns True if the argument with the keyword "magicnumber" is worth 7,
    and False otherwise"""

    if kwargs.get("magicnumber") == 7:
        return True
    return False


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber = 6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber = 7) == True:
    print("Awesome!")
