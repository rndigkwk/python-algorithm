# flag에 따라 다른 값 반환하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181933
# 알고리즘: 조건문
# 작성자: 학생
# 작성일: 2026. 08. 10. 10:24:13

def solution(a, b, flag):
    answer = 0
    if flag == True:
        answer = a+b
    else :
        answer = a-b
    return answer