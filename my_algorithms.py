import random,time
class Algorithm:
    def __init__(self,name):
        self.array=random.sample(range(512),512)
        self.name=name
    def update_display(self,swap1=None,swap2=None):
        import Sorting_Visual
        Sorting_Visual.update(self,swap1,swap2)
    def run(self):
        self.start_time=time.time()
        self.algorithm()
        time_elapsed=time.time()-self.start_time
        return self.array,time_elapsed

class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")
    def algorithm(self):
        for i in range(len(self.array)):
            min_idx=i
            for j in range(i+1,len(self.array)):
                if(self.array[j]<self.array[min_idx]):
                    min_idx=j
            self.array[i],self.array[min_idx]=self.array[min_idx],self.array[i]
            self.update_display(self.array[i],self.array[min_idx])
            

class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")
    def algorithm(self):
        for i in range(len(self.array)-1):
            for j in range(1,len(self.array)-i):
                if self.array[j]<self.array[j-1]:
                    self.array[j],self.array[j-1]=self.array[j-1],self.array[j]
            self.update_display(self.array[j],self.array[j-1])


#other algo coming soon!
