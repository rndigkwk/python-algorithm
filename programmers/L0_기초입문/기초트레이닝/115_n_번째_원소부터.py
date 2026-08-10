# n 번째 원소부터
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181892
# 알고리즘: 리스트(배열)
# 작성자: 학생
# 작성일: 2026. 08. 10. 11:02:26

def solution(num_list, n):
    answer = num_list[n-1:]
    return answer