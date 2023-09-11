import utilities
def utils_tests():
    # testing reversed:
    # with string
    assert(utilities.utils.reversed("random-string") == "Error!")
    # with float
    assert(utilities.utils.reversed(3.14) == "Error!")
    # with positive int
    assert(utilities.utils.reversed(155) == 551)
    # with negative int
    assert(utilities.utils.reversed(-155) == -551)
    
    # testing formatter:
    # with string
    assert(utilities.utils.formatter("random-string") == "Error!")
    # with float
    assert(utilities.utils.formatter(3.14) == "Error!")
    # with positive int
    assert(utilities.utils.formatter(128) == ('0b10000000', '0o200'))
    assert(utilities.utils.formatter(135) == ('0b10000111', '0o207'))
    # with negative int
    assert(utilities.utils.formatter(-128) == ('-0b10000000', '-0o200'))

