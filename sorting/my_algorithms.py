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
class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")
    def algorithm(self):
        for i in range(1,len(self.array)):
            key=self.array[i]
            j=i-1
            while j>=0 and self.array[j]>key:
                self.array[j+1]=self.array[j]
                j-=1
            self.update_display(self.array[i],self.array[j+1])
            self.array[j+1]=key
class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")
    def merge(self,l,r,m):
        n1=m-l+1
        n2=r-m
        L,R=[0]*n1,[0]*n2
        for i in range(n1):
            L[i]=self.array[i+l]
        for i in range(n2):
            R[i]=self.array[i+m+1]
        i,j,k=0,0,l
        while i<n1 and j<n2:
            if L[i]>R[j]:
                self.array[k]=R[j]
                k+=1
                j+=1
            else :
                self.array[k]=L[i]
                k+=1
                i+=1
        while i<n1:
            self.array[k]=L[i]
            k+=1
            i+=1
        while j<n2:
            self.array[k]=R[j]
            k+=1
            j+=1
        # self.update_display()
    def mSort(self,l,r):
        if l>=r:
            pass
        else:
            mid=l+(r-l)//2
            self.mSort(l,mid)
            self.mSort(mid+1,r)
            self.merge(l,r,mid)
            self.update_display(self.array[l],self.array[mid])
        
    def algorithm(self):
        self.mSort(0,len(self.array)-1)
class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")
    def PivoT(self,l,r):
        pivot=self.array[r]
        i=l-1
        for j in range(l,r):
            if self.array[j]<pivot:
                i+=1
                self.array[i],self.array[j]=self.array[j],self.array[i]
        self.array[i+1],self.array[r]=self.array[r],self.array[i+1]
        self.update_display(self.array[i],self.array[j])
        return i+1
    def QSort(self,l,r):
        if l<r:
            Pivot=self.PivoT(l,r)
            self.QSort(l,Pivot-1)
            self.QSort(Pivot+1,r)
            # self.update_display()
    def algorithm(self):
        self.QSort(0,len(self.array)-1)
