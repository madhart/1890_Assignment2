import random


# Calling 'List' class inside RandomIntList, so class RandomintList itself can be a list.
class RandomIntList(list):

    def __init__(self, number_in):
        # For every number until input variable 'number_in' add a randint to Randomintlist.
        for i in range(number_in):
            # Specifications clarify that randints must be between 1 and 100.
            self.append(random.randint(1, 100))

    # Method determining how many integers are in the list for 'count' in main function.
    def getCount(self):
        count = len(self)
        return count

    # Method determining average by dividing sum of ints by number of ints in list to display 'average' in main function.
    def getAverage(self):
        sumforavg = sum(self)
        average = sumforavg / len(self)
        return average

    # Method determining sum of all the lists' randints for 'total' in main function.
    def getTotal(self):
        total = sum(self)
        return total

    # String method to print RandomIntList as comma separated values.
    def __str__(self):
        return ','.join(str(element) for element in self)