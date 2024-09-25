class MinHeap:
    def __init__(self):
        self.heap = []

    def build_heap(self, elements):
        self.heap = elements[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def insert(self, element):
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def get_min(self):
        return self.heap[0] if self.heap else None

    def print_heap(self):
        print(self.heap)

# Example usage for MinHeap
min_heap = MinHeap()
min_heap.build_heap([10, 20, 15, 30, 40])
min_heap.insert(5)
min_heap.insert(25)
print("MinHeap after inserts:")
min_heap.print_heap()  # Output: [5, 20, 10, 30, 40, 15, 25]
print("Removed:", min_heap.remove())  # Output: 5
print("MinHeap after removal:")
min_heap.print_heap()  # Output: [10, 20, 15, 30, 40, 25]
