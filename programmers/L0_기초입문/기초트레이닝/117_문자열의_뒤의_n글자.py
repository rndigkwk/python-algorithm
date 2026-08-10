# 문자열의 뒤의 n글자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181910
# 알고리즘: 문자열
# 작성자: 학생
# 작성일: 2026. 08. 10. 10:36:51

def solution(my_string, n):
    answer = my_string[-n:]
    return answer