# 문자열 뒤집기

s = 'Reverse this strings'
s_reverse = s[::-1]
print(s_reverse)

p = 'abcd'
p_lst = list(p)
p_lst.reverse()
print(p_lst)
p_reverse = ''.join(p_lst)
print(p_reverse)