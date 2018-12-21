class NotInAlphabetException(BaseException):
    def __init__(self, symbol):
        print("Symbol " + str(symbol) + " is not in this alphabet")
        super(NotInAlphabetException, self).__init__()


class Alphabet:
    def __init__(self, symbols):
        """

        :param symbols: an iterable of symbols (strings of length 1) which will define the alphabet. 
        """
        self.symbols = self._init_symbols(symbols)

    @staticmethod
    def _init_symbols(symbols):
        """

        :param symbols: a list of symbols in this alphabet
        :return: a hashable dictionary of symbols in the alphabet.
        If the symbol exists, the symbol maps to "1". Otherwise, the symbol
        is not in the dictionary.
        """
        result = {}

        for symbol in symbols:
            if symbol not in result:
                result[symbol] = True
        return result

    def is_in_alphabet(self, new_symbol):
        """

        :param new_symbol: some symbol. We are trying to determine whether or not
        this symbol is in the alphabet. This is a string of length 1
        :return: True if the symbol is in the alphabet. False otherwise
        """
        return new_symbol in self.symbols

    def add_symbol(self, new_symbol):
        """

        :param new_symbol: The new symbol to add to the alphabet. A string of length 1.
        :return: None.
        """
        if new_symbol not in self.symbols:
            self.symbols[new_symbol] = 1

    def remove_symbol(self, symbol):
        """

        :param symbol: The symbol to remove from the alphabet
        :return: None
        """
        if symbol in self.symbols:
            self.symbols.pop(symbol)

