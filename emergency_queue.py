
class Patient:
    def __init__(self, name, urgency):
        if not isinstance(urgency, int) or isinstance(urgency, bool) or not 1 <= urgency <= 10:
            raise ValueError("Urgency must be between 1 and 10")

        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.data[index].urgency >= self.data[parent].urgency:
                break

            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent

    def heapify_down(self, index):
        size = len(self.data)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left

            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")

        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        if len(self.data) == 0:
            return None

        return self.data[0]

    def remove_min(self):
        if len(self.data) == 0:
            return None

        first = self.data[0]
        last = self.data.pop()

        if len(self.data) > 0:
            self.data[0] = last
            self.heapify_down(0)

        return first


if __name__ == "__main__":
    heap = MinHeap()

    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))

    heap.print_heap()

    next_up = heap.peek()
    print("Next patient:", next_up.name, next_up.urgency)

    served = heap.remove_min()
    print("Served:", served.name)

    heap.print_heap()

    print("Removing remaining patients:")
    while heap.peek() is not None:
        patient = heap.remove_min()
        print(patient.name, patient.urgency)

# Design Memo
#
# For this assignment, I made two systems for a hospital using a
# binary tree and a min-heap. The doctor tree is useful because it
# helps organize the doctors and shows who reports to who. Instead
# of having all the doctors in one big list, the tree makes it
# easier to see how everyone is connected.
#
# I also used three different ways to go through the tree.
# Preorder starts at the top and works its way down. This could
# help show the doctors in order starting with management.
# Inorder goes through the left side first, then the main doctor,
# and then the right side. This could be useful for checking the
# structure of the tree. Postorder starts with the doctors at
# the bottom before going back to the top. This could help when
# doctors need to report information to their managers.
#
# For the emergency queue, I used a min-heap to organize patients
# based on how serious their situation is. Patients with lower
# urgency numbers get treated first. I think this makes sense
# because someone with a serious emergency should not have to
# wait behind someone who just got there first.
#
# The min-heap also makes it easier to add new patients and
# remove patients while keeping the most urgent ones first.
# Overall, this assignment helped me understand how different
# data structures can be used to solve different problems.
