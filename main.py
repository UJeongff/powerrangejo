import sys
import time
from typing import List

MAX_N = 10000

# ---------------------------
# Bubble Sort
# ---------------------------
def bubble_sort(arr: List[int], asc: bool = True) -> List[int]:
    a = arr[:]
    n = len(a)
    if asc:
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True
            if not swapped:
                break
    else:
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if a[j] < a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True
            if not swapped:
                break
    return a

# ---------------------------
# Selection Sort
# ---------------------------
def selection_sort(arr: List[int], asc: bool = True) -> List[int]:
    a = arr[:]
    n = len(a)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if asc:
                if a[j] < a[idx]:
                    idx = j
            else:
                if a[j] > a[idx]:
                    idx = j
        if idx != i:
            a[i], a[idx] = a[idx], a[i]
    return a

# ---------------------------
# Insertion Sort
# ---------------------------
def insertion_sort(arr: List[int], asc: bool = True) -> List[int]:
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        if asc:
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                j -= 1
        else:
            while j >= 0 and a[j] < key:
                a[j + 1] = a[j]
                j -= 1
        a[j + 1] = key
    return a

# ---------------------------
# Merge Sort
# ---------------------------
def merge_sort(data_list: List[int], asc: bool = True) -> List[int]:
    n = len(data_list)
    if n <= 1:
        return data_list[:]
    mid = n // 2
    left = merge_sort(data_list[:mid], asc=asc)
    right = merge_sort(data_list[mid:], asc=asc)
    return _merge(left, right, asc)

def _merge(left: List[int], right: List[int], asc: bool) -> List[int]:
    i = j = 0
    out = []
    if asc:
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i]); i += 1
            else:
                out.append(right[j]); j += 1
    else:
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                out.append(left[i]); i += 1
            else:
                out.append(right[j]); j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out

# ---------------------------
# Quick Sort
# ---------------------------
def quick_sort(arr: List[int], asc: bool = True) -> List[int]:
    a = arr[:]
    _quick(a, 0, len(a) - 1, asc)
    return a

def _less(x, y, asc):
    return x < y if asc else x > y

def _quick(a, lo, hi, asc):
    while lo < hi:
        p = _partition(a, lo, hi, asc)
        if (p - lo) < (hi - p):
            _quick(a, lo, p, asc)
            lo = p + 1
        else:
            _quick(a, p + 1, hi, asc)
            hi = p

def _partition(a, lo, hi, asc):
    pivot = a[(lo + hi) // 2]
    i, j = lo - 1, hi + 1
    while True:
        i += 1
        while _less(a[i], pivot, asc):
            i += 1
        j -= 1
        while _less(pivot, a[j], asc):
            j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]

# ---------------------------
# Heap Sort
# ---------------------------
def heap_sort(arr: List[int], asc: bool = True) -> List[int]:
    a = arr[:]
    n = len(a)

    def sift_down(i: int, size: int):
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            best = i
            if l < size and a[l] > a[best]:
                best = l
            if r < size and a[r] > a[best]:
                best = r
            if best == i:
                break
            a[i], a[best] = a[best], a[i]
            i = best

    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n)
    size = n
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        size -= 1
        sift_down(0, size)
    if not asc:
        a.reverse()
    return a

# ---------------------------
# 실행/출력 유틸
# ---------------------------
def run_and_report(name: str, sorter, data: List[int], asc: bool):
    t0 = time.perf_counter()
    out = sorter(data, asc=asc)
    ms = (time.perf_counter() - t0) * 1000.0
    print(f"[{name}] N={len(out)} -> time={ms:.3f} ms")
    preview = ", ".join(map(str, out[:50]))
    print("sorted:", preview + (" ..." if len(out) > 50 else ""))
    print()

# ---------------------------
# main
# ---------------------------
ALGOS = [
    ("Bubble", bubble_sort),
    ("Selection", selection_sort),
    ("Insertion", insertion_sort),
    ("Merge", merge_sort),
    ("Quick", quick_sort),
    ("Heap", heap_sort),
]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python main.py <data_file> [asc|desc]")
        sys.exit(1)

    file_path = sys.argv[1]
    order = sys.argv[2].lower() if len(sys.argv) > 2 else "asc"
    asc = (order == "asc")

    # 데이터 읽기
    data_list: List[int] = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if ":" in line:
                    line = line.split(":", 1)[1]
                parts = [p.strip() for p in line.replace(",", " ").split()]
                for p in parts:
                    if p and p.lstrip("-").isdigit():
                        data_list.append(int(p))
                if len(data_list) >= MAX_N:
                    data_list = data_list[:MAX_N]
                    break
    except FileNotFoundError:
        print(f"오류: {file_path} 파일을 찾을 수 없습니다.")
        sys.exit(1)

    print(f"입력 데이터 개수: {len(data_list)} (최대 {MAX_N})\n")

    for name, func in ALGOS:
        run_and_report(name, func, data_list, asc=asc)
