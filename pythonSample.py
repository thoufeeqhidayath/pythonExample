
class sequenceIdentify():

    def __init__(self):
        self.name=0

grouping_graph={}
basicelements=[]
elements={}
graph_count=0
i=0

def main():
    sequence =int(raw_input("Enter the sequence"))
    print(sequence)
    separateNumberslist = []
    separateNumberslist = separateNumbers(sequence)
    storeArray(separateNumberslist)


def separateNumbers(sequences):
    numbers = []
    try:
        while (1):
            number = sequences % 10
            sequences = sequences / 10
            numbers.append(number)
            if (sequences == 1):
                number = sequences % 10
                numbers.append(number)
                break
        numbers.reverse()
    except:
       print("error")
    return numbers


def storeArray(numberList):
    numberLists={}
    numberLists[0]=(numberList[0],numberList[1])

    for i in range(1,len(numberList)-1):
        numberLists[i]=(numberList[i],numberList[i+1])

    elements[0]=numberLists
    findExistMore(numberLists)




def findExistMore(checkList):
    countOf={}
    count=0
    for i in range(0, len(checkList)):
        for j in range(i+1,len(checkList)):
            if checkList[i]==checkList[j]:
                countOf[i]=checkList[i]
                count=count+1
    print countOf
    separateListElement(countOf)


def separateListElement(toSeparateList):
    flag=0
    temporary_store=[]
    length=len(toSeparateList)
    for count in (0,length-2):
        list1 =toSeparateList[count]
        list2 =toSeparateList[count+1]
        if(list1[1]==list2[0]):
         if(flag==0):
           temporary_store=temporaryStorefun(list1[0],list1[1],list2[1])
           flag=1
         else:
             temporary_store=temporaryStorefuns( temporary_store,7)

        elif(list1[1]!=list2[0]):
            pass
        print temporary_store


def temporaryStorefun(first,second,third):
    lists=[]
    lists.append(first)
    lists.append(second)
    lists.append(third)
    return lists


def temporaryStorefuns(lists, second):
    list = []
    list=lists
    list.append(second)
    return list


def make_into_separate(group_data):
    grouping_graph[graph_count]=group_data


if __name__ == '__main__':
    main()



