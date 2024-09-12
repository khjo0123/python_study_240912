#양의 정수 n을 입력 받아 n*n 크기의 행렬을 출력하는 프로그램 작성
# 이 때 행렬의 값은 1부터 시작하여 왼쪽에서 오른쪽 위에서 아래 순서대로 채워 넣음
#입력 3
# 1 2 3
# 4 5 6
# 7 8 9
# 입력 받은 값으로 실제 출력 범위 정해야 함
# 줄 바꿈  %
# 줄 맞춤

# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

n = int(input(" n 입력: "))
# for i in range(1,n+1):
#     print(i, end=" ")
#     if i%n == 0:
#         print("\n")
#
# for j in range(n+1,n+5):
#     print(j, end=" ")

for i in range(1, n*n+1):
    # print()
#     print(f"{i:5}", end="") # {i:5} 5칸 정렬
#     if i%n == 0:
#         print("\n")

