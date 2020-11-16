def solution(S):
    brackets = "{[()]}"
    o_b = ['[', '{', '(']  # elelment to push on stack
    po = {']': '[', '}': '{', ')': '('}
    dict = {'{': 0, '[': 0, '(': 0, ')':0 , ']':0, '}':0}
    mystr=""
    for s in S:
        if s in brackets:
            mystr+=s
    if len(mystr)%2 == 1:
        return 0
    stack=[]
    for s in mystr:
        if s in o_b:
            stack.append(s)
        if s in po.keys():
            if len(stack)==0:
                return 0

            if (stack[-1] == po[s]):
                print("stack |", stack)
                print("{0}  |  {1}".format(stack[-1], po[s]))
                stack.pop()
            else:
                return 0
    if len(stack) == 0:
        return 1
    else:
        return 0

s="{[() sdfsdf ((]))]}]"
s = ".join([random.choice(['{'*100000, '}'*100000]) for p in range(0, 2)])"
print(solution(s))