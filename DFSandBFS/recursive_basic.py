'''
재귀 함수 (Recursive Function)
: 자기 자신을 다시 호출하는 함수

* 문제풀이에서 사용할 경우 반드시 재귀 함수 종료 조건을 명시해야한다.
* 종료 조건을 명시하지 않을 경우 무한으로 호출하게 된다.
'''

def recursive_func(i):
    if i == 100:
        return
    print(i,"번째 재귀함수에서 ",i+1,"번째 재귀함수 호출중")
    recursive_func(i+1)
    print(i,"번째 재귀함수를 종료")

recursive_func(1)