class Insert:

    def __init__(
            self,
            some_string: str,
            purpose_of_combination: str,
            insert_combination: str
    ):
        self.__some_string = some_string
        self.__purpose_of_combination = purpose_of_combination
        self.__insert_combination = insert_combination

    def insert_string(self):
        words = self.__some_string.split()
        result = ""

        for word in words:
            if self.__purpose_of_combination in word:
                result += word.replace(
                    self.__purpose_of_combination,
                    self.__purpose_of_combination + self.__insert_combination
                ) + " "
            else:
                result += word + " "

        print(result.strip())
