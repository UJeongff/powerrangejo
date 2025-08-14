import time
if __name__ == "__main__":
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
        print("오류: 파일에 숫자가 아닌 값이 포함되어 있다.")
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
=======

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
