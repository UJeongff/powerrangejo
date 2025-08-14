# PowerRangeJo
BoB 14기 Digital Forensics 07조

## 📑 목차
- [👥 팀원](#-팀원)
- [📌 프로젝트 개요](#-프로젝트-개요)
- [🛠 사용 기술 & 도구](#-사용-기술--도구)
- [⚙️ 정렬 알고리즘 설명](#️-정렬-알고리즘-설명)
- [▶ 실행 방법](#-실행-방법)
- [📅 진행 일정](#-진행-일정)

---

## 👥 팀원
- 서동연 (팀원)
- 송성호 (팀원)
- 유인희 (팀원)
- 최우정 (조장)
- 최원혁 (팀원)

---

## 📌 프로젝트 개요
이 레포지토리는 BoB 14기 Digital Forensics 07조의 활동과 과제를 기록합니다.  

이번 과제에서는 Python을 활용해 **여러 정렬 알고리즘(Merge Sort, Heap Sort, Quick Sort, Bubble Sort, Insertion Sort)**을 구현하고,  
동일한 데이터에 대해 알고리즘별 실행 시간과 결과를 비교하였습니다.

---

## 📂 디렉토리 구조
PowerRangeJo/
├── main.py # 정렬 알고리즘 구현 및 실행 스크립트
├── data.txt # 테스트 데이터
└── README.md # 프로젝트 설명 문서

---

## 🛠 사용 기술 & 도구
- Python 3.12
- VSCode
- Git & GitHub

---

## ⚙️ 정렬 알고리즘 설명
- **Merge Sort**  
  분할 정복(Divide and Conquer) 방식으로 리스트를 반으로 나누고 각각 정렬한 뒤 병합합니다.  
  시간 복잡도: O(n log n)

- **Heap Sort**  
  최대 힙(Max Heap)을 구성하고, 루트 노드(최대값)를 제거하며 재정렬합니다.  
  시간 복잡도: O(n log n)

- **Quick Sort**  
  기준(pivot)을 정해 작은 값과 큰 값으로 분할하고 재귀적으로 정렬합니다.  
  평균 시간 복잡도: O(n log n), 최악: O(n²)

- **Bubble Sort**  
  인접한 두 원소를 비교하여 교환하며 정렬합니다.  
  시간 복잡도: O(n²)

- **Insertion Sort**  
  이미 정렬된 부분에 새로운 원소를 알맞은 위치에 삽입합니다.  
  시간 복잡도: O(n²)

---

## ▶ 실행 방법
```bash
# 1. 저장소 클론
git clone https://github.com/USERNAME/PowerRangeJo.git
cd PowerRangeJo

# 2. data.txt 파일 준비
#    - 쉼표(,) 또는 공백으로 구분된 숫자 리스트
#    - 최대 10,000개까지 처리 가능

# 3. main.py 실행
#    형식: python main.py <data_file> [asc|desc]
#    기본은 오름차순(asc)
python main.py data.txt
python main.py data.txt desc   # 내림차순 정렬

# 실행 예시
# 결과: Bubble, Selection, Insertion, Merge, Quick, Heap 순서로 모두 실행 및 시간 측정
```
