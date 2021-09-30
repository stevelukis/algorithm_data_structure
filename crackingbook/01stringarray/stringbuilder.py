class StringBuilder:
    def __init__(self, first_string=None):
        super().__init__()
        string_list = []
        if first_string is not None:
            string_list.append(first_string)
        self.string_list = string_list

    def append(self, another_string):
        self.string_list.append(another_string)

    def to_string(self):
        result = ""
        for m_string in self.string_list:
            result += m_string
        return result


if __name__ == '__main__':
    builder = StringBuilder("My")
    builder.append(' name')
    builder.append(' is')
    builder.append(' Steve')
    print(builder.to_string())
