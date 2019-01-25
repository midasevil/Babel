class Sorter:
    def bubblesort(self, array):
        l = len(array)
        i = l - 1
        while i > 0:
            for j in range(i):
                print(array)
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
            i = i - 1
        
    def quicksort(self,array):
        pivotlist = []
        less = []
        more = []
        l = len(array)
        if l <= 1:
            return array
        pivot = array[0]
        for e in array:
            if e < pivot:
                less.append(e)
            elif e > pivot:
                more.append(e)
            else:
                pivotlist.append(e)
        return self.quicksort(less) + pivotlist + self.quicksort(more)


        

s = Sorter()
li = [9,8,7,6,5,4,3,2,1]
# soort = s.quicksort



def pop_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] =array[j+1],array[j]

        
    return array

pop_sort(li)
print(li)