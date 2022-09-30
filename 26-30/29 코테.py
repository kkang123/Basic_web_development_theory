#문제 설명
'''
Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15

자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.
'''

#제한사항
'n은 10,000 이하의 자연수 입니다.'

#입출력 예
'''
n	result
15	4
'''

#문제해결


def solution(n):
    answer = 0
    for i in range(1, n+1): #'15=15'가 있어 (1, n+1)을 함으로 1부터 15까지 범위 설정
        sum = 0
        for j in range(i, n+1): # 반복 시작
            sum += j #계속 값 +
            if sum == n: # 더한 값(sum)이 n과 같으면  answer += 1 실행
                answer += 1
                break
            elif sum > n:  #더한 값이 n보다 크면 멈추기
                break
    return answer
