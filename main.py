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
