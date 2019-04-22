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
# 올바른 수식 판별

# def solution(expr):
#     match = {
#         ')':'(',
#         '}':'{',
#         ']':'['
#     }
#     S = ArrayStack()
#     for c in expr:
#         if c in '({[':
#             S.push(c)

#         elif c in match:
#             if S.isEmpty():
#                 return False

#             else :
#                 t = S.pop()
#                 if t != match[c]:
#                     return False

#     return S.isEmpty

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
                if prec[opStack.peek()] >= prec[x]:
                    answer += opStack.pop()
            opStack.push(x)

        elif x == ')':
            while not opStack.isEmpty() and opStack.peek() != '(':
                answer += opStack.pop()        

        else : answer += x

    while not opStack.isEmpty():
        if opStack.peek() == '(':opStack.pop()
        answer += opStack.pop()
    return answer
print(solution('A*D-(C-B)'))