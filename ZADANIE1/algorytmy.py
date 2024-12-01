from ZADANIE1.tablica import MonitorowanaTablica

def insertion_sort(array: MonitorowanaTablica, left=0, right=None):
    if right is None:
        right = len(array) - 1

    i = left + 1
    while i <= right:
        j = i
        while j > left and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1


def bubble_sort(array: MonitorowanaTablica):
    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                swapped = True

        if not swapped:
            break


def shell_sort(array: MonitorowanaTablica):
    left = 0
    right = len(array) - 1

    h = 1
    while h <= (right - left) // 9:
        h = 3 * h + 1

    while h > 0:
        for i in range(left + h, right + 1):
            j = i

            item = array[i]
            while j >= left + h and item < array[j - h]:
                array[j] = array[j - h]
                j = j - h
            array[j] = item

        h = h // 3




def merge_sort(array: MonitorowanaTablica, left=None, right=None):
# twoj kod
    pass


def merge(array: MonitorowanaTablica, left, middle, right):
    """Merges two sorted subarrays."""
    # twoj kod, moze sie przydac
    pass


def quick_sort(array: MonitorowanaTablica, left=None, right=None):
    """Performs quick sort on the given array."""
    # twoj kod
    pass


def partition(array: MonitorowanaTablica, left, right):
    """Partitions the array into two parts."""
    # twoj kod, moze sie przydac
    pass


def tim_sort(array: MonitorowanaTablica):
# twoj kod
    pass



algorytmy = [
    (insertion_sort, "Insertion Sort"),
    (bubble_sort, "Bubble Sort"),
    (shell_sort, "Shell Sort"),
    # (merge_sort, "Merge Sort"),
    # (quick_sort, "Quick Sort"),
    # (tim_sort, "Tim Sort"),
]