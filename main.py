import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # key보다 큰 요소는 한 칸씩 뒤로 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    data_list = []

    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            # ":"로 분리 → 앞은 버리고 뒷부분만 사용
            if ":" in line:
                line = line.split(":", 1)[1]  # 첫 번째 ":" 뒤 내용만

            # 공백 제거 후 콤마로 분리
            numbers = line.strip().split(",")

            # 숫자만 리스트에 추가
            data_list.extend(int(num.strip()) for num in numbers if num.strip())
    
    # 결과 확인
    print("읽어온 데이터:", data_list)
    print(f"총 데이터 개수: {len(data_list)}")

def heapify(arr, n, i):
    """i를 루트로 하는 서브트리를 최대 힙으로 만드는 함수"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """Heap Sort 알고리즘"""
    n = len(arr)

    # 최대 힙 생성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 원소 하나씩 꺼내 힙 재구성
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# -------------------------
# 실행
# -------------------------
print("\n=== Heap Sort 실행 ===")
heap_sort(data_list)
print("정렬된 데이터:", data_list)