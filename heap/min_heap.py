from collections import deque

class MinHeap:
    def __init__(self):
        self.array = [None]

    def get_size(self):
        """
        Returns the number of values in the min-heap.
        One is subtracted to account for the zero index which is never used.
        """
        return len(self.array) - 1

    def peek(self):
        """
        Returns smallest value without modifying the min-heap.
        """
        size = self.get_size()
        if size == 0:
            raise Exception("Cannot peek from empty heap.")
        return self.array[1]

    def extract_min(self):
        """
        Pops the minimum value from the min-heap and returns said value.
        """
        size = self.get_size()
        if size == 0:
            raise Exception("Cannot extract min from empty heap.")
        elif size == 1:
            return self.array.pop()
        minimum = self.array[1]
        last = self.array.pop()
        self.array[1] = last
        resolve = deque()
        resolve.append(1)
        self.heapify_down(resolve)
        return minimum

    def bulk_insert(self, numbers):
        """
        Inserts multiple values into the heap.
        """
        for no in numbers:
            self.array.append(no)
        self.build_min_heap()

    def single_insert(self, number):
        """
        Inserts a single value into the heap.
        """
        size = self.get_size()
        self.array.append(number)
        resolve = deque()
        resolve.append(size + 1)
        self.heapify_up(resolve)

    def heapify_up(self, resolve):
        """
        Maintains the min-heap property by pushing smaller values towards the
        top of the min-heap.

        Requires the heap to be partially built.
        """
        while resolve:
            index = resolve.popleft()
            parent = index // 2
            if parent < 1:
                continue
            if self.array[parent] > self.array[index]:
                self.array[parent], self.array[index] = \
                    self.array[index], self.array[parent]
                # make sure the smaller value is saved to be pushed further
                # towards the top as long as it is still smaller than the values
                # above it.
                resolve.append(parent)

    def heapify_down(self, resolve):
        """
        Maintains min-heap property by pushing larger values towards the bottom
        of the min-heap.

        Requires the heap to be partially built.
        """
        size = self.get_size()
        while resolve:
            index = resolve.popleft()
            left_child = index * 2
            if left_child > size:
                continue
            right_child = left_child + 1
            if right_child > size:
                # left_child only
                self.array[index]
                self.array[left_child]
                if self.array[index] > self.array[left_child]:
                    self.array[index], self.array[left_child] = \
                        self.array[left_child], self.array[index]
                    # make sure the larger value is saved to be pushed further
                    # towards the bottom later as long as it is still bigger
                    # than the values below it.
                    resolve.append(left_child)
            elif (self.array[index] > self.array[left_child] or
                    self.array[index] > self.array[right_child]):
                if (self.array[index] > self.array[left_child] and
                        self.array[left_child] < self.array[right_child]):
                    self.array[index], self.array[left_child] = \
                        self.array[left_child], self.array[index]
                    resolve.append(left_child)
                elif (self.array[index] > self.array[right_child] and
                        self.array[right_child] <= self.array[left_child]):
                    self.array[index], self.array[right_child] = \
                        self.array[right_child], self.array[index]
                    resolve.append(right_child)

    def build_min_heap(self):
        """
        Builds a min-heap from scratch.
        """
        size = self.get_size()
        if size == 1:
            return
        resolve = deque()
        for index in range(size, 1, -1):
            parent = index // 2
            if self.array[index] < self.array[parent]:
                # trade places with the larger value
                self.array[index], self.array[parent] = \
                    self.array[parent], self.array[index]
                # make sure the larger value is saved to be pushed further
                # towards the bottom later as long as it is still bigger
                # than the values below it.
                resolve.append(index)
        self.heapify_down(resolve)
