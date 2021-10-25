
def funcao(string1, string2):
	for i in range(len(string1)):
		substring1 = string1[i:]
		substring2 = string2[:len(substring1)]
		if substring2.find(substring1) >= 0:
			return(len(substring1))
	return 0

print(funcao('abcxxxxa', 'xxaabcd'))
print(funcao('abcxxxxa', 'yxxaabcd'))