"""
AA00 = 10
AB00 = (AA00 + AA01) *15
AA01 = 20 + AB00

求公式内的循环调用
union find？
"""
def str_match_0(s, target):
	for i in range(len(s)):
		for j in range(len(target)):
			if target[j] != s[i]:
				break
			i +=1
			if j>=len(target)-1:
				return i-len(target) + 1
	return -1