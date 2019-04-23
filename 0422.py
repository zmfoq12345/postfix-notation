class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

# 중위표현식을 후위표현식으로 변경
prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1 
    }

def solution(Sik):
    opStack = ArrayStack()
    answer = ''
    for x in Sik:
        if x in prec:
            if x != '(' and not opStack.isEmpty():
                if prec[opStack.peek()] >= prec[x]: # 우선순위 비교
                    answer += opStack.pop()
            opStack.push(x)

        elif x == ')':
            while not opStack.isEmpty() and opStack.peek() != '(':
                answer += opStack.pop()        
            opStack.pop() # 여는 괄호 제외

        else : answer += x

    while not opStack.isEmpty():
        if opStack.peek() == '(' : opStack.pop() #스택에서 괄호 제외
        if opStack.size() > 0: answer += opStack.pop()
    return answer



import timeit
start = timeit.default_timer()

#s = input() # 입력받기
s = '(2+(8-2*1)*6)+6*1024' # 직접 입력
print(solution(s))

stop = timeit.default_timer()
print("RunTime : ",stop - start)
