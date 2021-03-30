from node import Node

class Heap:
    """
    Heap representation via list.

    Zero index in the list is ignored to avoid offsets when calculating parent
    and child indices.
    """
    def __init__(self, array=None):
        self.heap = []
        if array:
            self.heap = self.heapify(array)
    
    def find_max(self):
        pass

    def insert(self):
        pass

    def extract_max(self):
        """
        Removes the maximum value in the heap and returns this value to the
        caller.

        Returns None if heap is empty.
        """
        size = len(self.heap)
        if size == 2:
            return self.heap.pop()
        elif size == 1:
            return None
        rv = self.heap[1]
        self.heap[1] = self.heap.pop()
        ancestor = [1]
        left = None
        right = None
        size = len(self.heap)
        while ancestor:
            index = ancestor.pop()
            parent = self.heap[index]
            if (index * 2) < size:
                left = self.heap[index * 2]
            if (index * 2) + 1 < size:
                right = self.heap[(index * 2) + 1]
            if not left and not right:
                continue
            elif left and parent > left and right and parent > right:
                continue
            else:
                if left and not right:
                    largest = left
                elif right and not left:
                    largest = right
                else:
                    largest = left if left > right else right
            if largest and parent < largest:
                if largest == self.heap[index * 2]:
                    self.heap[index] = self.heap[index * 2]
                    self.heap[index * 2] = parent
                    ancestor.append(index * 2)
                elif largest == self.heap[(index * 2) + 1]:
                    self.heap[index] = self.heap[(index * 2) + 1]
                    self.heap[(index * 2) + 1] = parent
                    ancestor.append((index * 2) + 1)
            left = None
            right = None
            largest = None
        return rv


    def heapify(self, array):
        """
        Create a heap out of a given array of elements.
        """
        size = len(array)
        ancestors = []

        counter = size - 1
        while counter > 1:
            parent = array[int(counter / 2)]
            if parent < array[counter]:
                array[int(counter / 2)], array[counter] = array[counter], array[int(counter / 2)]
                parent = array[int(counter / 2)]
                ancestors.append(counter)
            counter -= 1

        left = None
        right = None
        while ancestors:
            index = ancestors.pop()
            parent = array[index]
            if index * 2 < size:
                left = array[index * 2]
            if (index * 2) + 1 < size:
                right = array[(index * 2) + 1]
            if left == None and right == None:
                continue
            elif left or right:
                if left and not right:
                    largest = left
                elif left and not right:
                    largest = right
                else:
                    largest = left if left and left > right else right
            if largest and parent < largest:
                array[index] = largest
                if largest == array[index * 2]:
                    array[index * 2] = parent
                    ancestors.append(index * 2)
                elif largest == array[(index * 2) + 1]:
                    array[(index * 2) + 1] = parent
                    ancestors.append((index * 2) + 1)
            left = None
            right = None
            largest = None
        return array
