class Codec:

    def encode(self, input):
        return "".join([f"{len(i)}#{i}" for i in input])

    def decode(self, input):
        index, result = 0, []

        while index < len(input):
            j = index

            length = int(input[j])

            word = input[j + 2: j + 2 + length]

            result += [word]

            index = j + 2 + length

        return result


_ = Codec()

print(_.decode("6#Hello;5#World"))
