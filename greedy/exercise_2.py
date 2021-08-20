'''
프로그래머스 > 그리디 > 체육복
링크 : https://programmers.co.kr/learn/courses/30/lessons/42862

'''
reserve = [1]
lost = [3]
n = 3

participants = []

def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    print(n - len(set_lost))
    return n - len(set_lost)

solution(n, lost, reserve)