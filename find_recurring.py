class problems:
    def __init__(self):
        self.graph={}

    def main(self):
        x = int(raw_input("enter nuber"))
        self.rec_func(x)
        print self.graph

    def rec_func(self, x):
        for i in range(1, x):
            self.graph[i] = i * i

    if __name__ == '__main__':
        main()

