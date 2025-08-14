import time

def merge_sort(data_list):
    """
    병합 정렬(Merge Sort)을 사용하여 숫자 리스트를 오름차순으로 정렬합니다.
    Args:
        data_list (list): 정렬할 숫자가 담긴 리스트.
    Returns:
        list: 정렬된 새로운 리스트.
    """
    if len(data_list) <= 1:
        return data_list

    mid = len(data_list) // 2
    left_half = data_list[:mid]
    right_half = data_list[mid:]

    sorted_left_half = merge_sort(left_half)
    sorted_right_half = merge_sort(right_half)

    return _merge(sorted_left_half, sorted_right_half)

def _merge(left, right):
    """
    정렬된 두 리스트(left, right)를 하나로 병합하여 정렬된 리스트를 반환합니다.
    """
    merged_list = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])
    return merged_list

if __name__ == "__main__":
    # 1. 데이터 읽기
    data_list = []
    try:
        with open("data.txt", "r", encoding="utf-8") as f:
            for line in f:
                if ":" in line:
                    line = line.split(":", 1)[1]
                numbers = line.strip().split(",")
                data_list.extend(int(num.strip()) for num in numbers if num.strip())
    except FileNotFoundError:
        print("오류: data.txt 파일을 찾을 수 없습니다.")
        exit()
    except ValueError:
        print("오류: 파일에 숫자가 아닌 값이 포함되어 있습니다.")
        exit()

    # 읽어온 데이터 확인
    print("--- 원본 데이터 ---")
    print(data_list)
    print(f"총 데이터 개수: {len(data_list)}\n")

    # 2. 병합 정렬 수행 및 시간 측정
    print("--- 병합 정렬 수행 ---")
    start_time = time.time()
    sorted_data = merge_sort(data_list)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("정렬 완료!\n")

    # 3. 최종 결과 출력
    print("--- 최종 결과 ---")
    print("정렬된 데이터:", sorted_data)
    print(f"정렬 소요 시간: {elapsed_time:.6f}초")
