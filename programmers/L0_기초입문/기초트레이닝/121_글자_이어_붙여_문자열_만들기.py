# 글자 이어 붙여 문자열 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181915
# 알고리즘: 문자열
# 작성자: 학생
# 작성일: 2026. 08. 10. 10:50:16

def solution(my_string, index_list):
    answer = ''
    for i in range(len(index_list)):
        a = index_list[i]
        answer += my_string[a]
    return answer