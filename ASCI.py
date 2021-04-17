class ASCI:
    num_to_char = dict()
    char_to_num = dict()

    for num_char in range(0,128):
        char = chr(num_char)
        pos = len(char_to_num)
        num_to_char[pos] = char
        char_to_num[char] = pos

    @staticmethod
    def contains(char: str) -> bool:
        return (char in ASCI.char_to_num)
        pass

    @staticmethod
    def isalpha(char: str) -> bool:
        return (contains(char) and char.isalpha())
        pass

    @staticmethod
    def lower(char: str) -> str:

        return char.lower()

    @staticmethod
    def order(char: str) -> int:

        return ASCI.char_to_num[char]
        pass

    @staticmethod
    def getchar(num: int) -> str:

        return ASCI.num_to_char[num]
        pass

    @staticmethod
    def size() -> int:
        return len(ASCI.num_to_char)
        pass

    pass
