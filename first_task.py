class Letters:

    def __init__(self, some_string: str):
        self.__some_string = some_string
        self.o_symbol = 'o'
        self.a_symbol = 'a'

    def find_result_with_for(self):
        a_counter = 0
        o_counter = 0

        for symbol in self.__some_string:
            if symbol == self.a_symbol:
                a_counter += 1
            elif symbol == self.o_symbol:
                o_counter += 1

        if a_counter > o_counter:
            print(f'\'a\' symbols is more\nQuantity: {a_counter}')
        elif o_counter > a_counter:
            print(f'\'o\' symbols is more\nQuantity: {o_counter}')
        else:
            print(f'Quantity is equal: {a_counter}')

    def find_result_with_methods(self):
        a_counter = self.__some_string.count(self.a_symbol)
        o_counter = self.__some_string.count(self.o_symbol)

        if a_counter > o_counter:
            print(f'\'a\' symbols is more\nQuantity: {a_counter}')
        elif o_counter > a_counter:
            print(f'\'o\' symbols is more\nQuantity: {o_counter}')
        else:
            print(f'Quantity is equal: {a_counter}')

