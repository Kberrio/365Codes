import time
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr
        arr[j + 1] = key
        yield arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr

def visualize_sort(sort_func, arr):
    n = len(arr)
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(n), arr, align="edge")

    ax.set_xlim(0, n)
    ax.set_ylim(0, int(1.1 * max(arr)))
    
    iteration = [0]
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")

    anim = FuncAnimation(fig, func=update_fig,
                         fargs=(bar_rects, iteration),
                         frames=sort_func(arr.copy()),
                         interval=50,
                         repeat=False)
    
    plt.show()

# Example usage
arr = [random.randint(1, 100) for _ in range(30)]
visualize_sort(bubble_sort, arr)
visualize_sort(insertion_sort, arr)
visualize_sort(selection_sort, arr)