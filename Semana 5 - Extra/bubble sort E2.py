class BubbleSortSteps:
    def __init__(self,data):
        self.data=data
        self.iterations=0
        self.exchanges=0
    
    def bubble_sort(self):
        n=len(self.data)
        for i in range(n-1):
            swapped=False
            self.iterations+=1
            for j in range(n-1-i):
                if self.data[j]>self.data[j+1]:
                    self.data[j],self.data[j+1]=self.data[j+1],self.data[j]
                    self.exchanges+=1
                    swapped=True
            if not swapped:
                break
    
    def print_results(self):
        print("List in order:", self.data)
        print("Iterations:", self.iterations)
        print("Exchanges:", self.exchanges)

values=[4,3,5,1,2]
bs=BubbleSortSteps(values)
bs.bubble_sort()
bs.print_results()
