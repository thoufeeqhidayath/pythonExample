import graph_lib


def main():
   sequence=int(raw_input("Enter the sequence"))
   separateNumberslist=[]
   separateNumberslist=separateNumbers(sequence)
   separateNumberslist.reverse()
   print separateNumberslist

def separateNumbers(sequences):
    numbers = []
    while (1):
        number = sequences % 10
        sequences = sequences / 10
        numbers.append(number)
        if (sequences == 1):
            number = sequences % 10
            numbers.append(number)

            break
    return numbers