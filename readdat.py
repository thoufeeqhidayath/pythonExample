
class readDat():

    def main(self):
        i=0
        self.reads()

    def reads(self):
        f=open("/Users/Mubarak/Documents/temp/pyml/filereading/xas.csv","r")
        readData=f.read();
        print(readData)


readDa=readDat()
readDa.main()