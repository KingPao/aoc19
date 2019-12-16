data_input = ["COM)B",
"B)C",
"C)D",
"D)E",
"E)F",
"B)G",
"G)H",
"D)I",
"E)J",
"J)K",
"K)L"]

 
class Orbital_Map(object):
    connections = []

    def dummy(self):
        com = "tba"
        for orbit_relation in data_input:
            orbits = orbit_relation.split(")")


            predecessor = orbits[0]
            successor   = orbits[1]

            while True:
                if self.find_com(predecessor):
                    starting_point = predecessor
                    break

    def find_com(self, predecessor):

        if predecessor == "COM":
            return True

        return False