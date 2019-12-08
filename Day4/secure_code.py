
class Secure_Container(object):

   

    def calc_numbers(self,val1,val2,max_iteraton):

        i = val1

        count = 0

       

        for i in range(0,max_iteraton):

            if i == val2:

                count += 1

 

        print(count)

   

 

min = 138307

max = 654504

min_data = [int(j) for j in str(min)]

max_data = [int(j) for j in str(max)]

 

secure_container = Secure_Container()

secure_container.calc_numbers(1,3,6)