
graph = { }

class sequence:
 def __init__(self):
     self.n=1

Matrix=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
def createGraph():
    for i in range(10):
        for j in range (10):

def main():
   sequence=int(raw_input("Enter the sequence"))
   separateNumberslist=[]
   separateNumberslist=separateNumbers(sequence)
   separateNumberslist.reverse()
   print separateNumberslist
   storeArray(separateNumberslist)


def separateNumbers(sequences):
      numbers=[]
      while(1):
       number=sequences%10
       sequences=sequences/10
       numbers.append(number)
       if(sequences==1):
          number = sequences % 10
          numbers.append(number)

          break
      return numbers

def storeArray(numberList):
    for i in range(len(numberList)-1):
        matrix[numberList[i]][numberList[i+1]]=







if __name__ == '__main__':
    main()
