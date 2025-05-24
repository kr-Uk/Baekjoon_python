MSG_FORMAT = '#{} {}'

for t in range(1, 11):
    _type = {'(':0, '[':0, '{':0, '<':0, ')':0, ']':0, '}':0, '>':0}
    _type2 = ['(', '[', '{', '<', ')', ']', '}', '>']
    n = int(input())
    gwalho = list(input())
    result = True
    for i in range(n):
        if gwalho[i] == '(':
            _type['('] += 1
        elif gwalho[i] == '[':
            _type['['] += 1
        elif gwalho[i] == '{':
            _type['{'] += 1
        elif gwalho[i] == '<':
            _type['<'] += 1
        elif gwalho[i] == ')':
            _type[')'] += 1
        elif gwalho[i] == ']':
            _type[']'] += 1
        elif gwalho[i] == '}':
            _type['}'] += 1
        elif gwalho[i] == '>':
            _type['>'] += 1
    for i in range(4):
        if _type[_type2[i]] != _type[_type2[i+4]]:
            result = False
    if result:
        print(MSG_FORMAT.format(t, 1))
    else:
        print(MSG_FORMAT.format(t, 0))
