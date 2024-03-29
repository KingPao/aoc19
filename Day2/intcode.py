class Intcode_logic(object):
    data = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 19, 5, 23, 1, 23, 5, 27, 2, 27, 10, 31, 1, 31, 9, 35, 1, 35, 5, 39, 1, 6, 39, 43, 2, 9, 43, 47, 1, 5, 47, 51, 2, 6, 51, 55, 1, 5, 55, 59, 2, 10, 59, 63, 1, 63, 6, 67, 2, 67, 6, 71, 2, 10, 71, 75, 1, 6, 75, 79, 2, 79, 9, 83, 1, 83, 5, 87, 1, 87, 9, 91, 1, 91, 9, 95, 1,
            10, 95, 99, 1, 99, 13, 103, 2, 6, 103, 107, 1, 107, 5, 111, 1, 6, 111, 115, 1, 9, 115, 119, 1, 119, 9, 123, 2, 123, 10, 127, 1, 6, 127, 131, 2, 131, 13, 135, 1, 13, 135, 139, 1, 9, 139, 143, 1, 9, 143, 147, 1, 147, 13, 151, 1, 151, 9, 155, 1, 155, 13, 159, 1, 6, 159, 163, 1, 13, 163, 167, 1, 2, 167, 171, 1, 171, 13, 0, 99, 2, 0, 14, 0]

    def calculate_intcode(self, pos1, pos2):
        indicator_operation = 0
        indicator_replace = 3

        self.data[1] = pos1
        self.data[2] = pos2

        for dummy in self.data:
            operation = Intcode_logic.data[indicator_operation]

            if operation == 99:
                print("ENDE")
                break

            value1 = self.data[self.data[1]]
            value2 = self.data[self.data[2]]

            replace = self.data[indicator_replace]

            #print("\n", operation, " | ", value1,
            #     " | ", value2, " | ", replace, "\n")

            if operation == 1:
                self.data[replace] = value1 + value2

            if operation == 2:
                self.data[replace] = value1 * value2

            indicator_operation += 4
            indicator_replace += 4
            #print(Intcode_logic.data)
        return self.data[0]
        
    def mutate_data(self):
        for i in range(0, 100):
            for j in range(0, 100):
                res = self.calculate_intcode(i,j)

                if  res == 19690720:
                    print("noun=", i, " verb=", j)

intcode = Intcode_logic()
intcode.mutate_data()
