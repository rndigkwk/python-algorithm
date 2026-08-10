# 부분 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181842
# 알고리즘: 조건문 활용
# 작성자: 학생
# 작성일: 2026. 08. 10. 10:38:53

def solution(str1, str2):
    if str1 in str2:
        answer = 1
    else :
        answer = 0
    return answer