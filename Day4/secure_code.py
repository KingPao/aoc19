class Secure_Container(object):

    MIN = 138307
    MAX = 654504

    def calc_numbers(self):
        count = 0

        for i in range(self.MIN, self.MAX):
            number_sequence = [int(j) for j in str(i)]

            if self.check_ascending(number_sequence) and self.check_matching_adjacent(number_sequence):
                count += 1

        print(count)

    def check_ascending(self, number_sequence):
        for i in range(0, len(number_sequence)-1):
            if number_sequence[i] > number_sequence[i+1]:
                return False

        return True

    def check_matching_adjacent(self, number_sequence):
        for i in range(0, len(number_sequence)-1):
            res = number_sequence.count(number_sequence[i])
            if res == 2:
                return True
                
        return False


secure_container = Secure_Container()
secure_container.calc_numbers()

