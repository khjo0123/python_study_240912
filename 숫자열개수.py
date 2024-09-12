# 자연수 A,B,C
# A= 150, B= 266, C=427 이면 A * B * C = 150 * 266 * 427 = 17037000
# 등장하는 숫자(0~9)의 개수를 세는 문제 :

# a, b, c = map(int, input("정수 입력 : ").split()) # 숫자를 공백 기준으로 입력 받음
# print(a * b * c)
# ls = str(a * b * c)
# for i in range(10): # 0~9
#     print(ls.count(str(i)), end=" ")


# 범위 기반 for 문 사용, count("찾고자하는 문자")

# 실습 2번 : 문자열 반전, 문자열을 입력 받아서 역순으로 출력


# str = input("문자열 입력 : ")
# re_Str = str[ : : -1]
# print(re_Str)

in_str = input("문자열 입력 : ")
for i in range(len(in_str)-1, -1, -1):
    print(in_str[i], end="")



