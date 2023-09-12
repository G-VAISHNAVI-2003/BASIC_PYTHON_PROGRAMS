from itertools import permutations
s = str(input())
s_per = list(permutations(s))
print("permutation:",s_per)
out_per = [''.join(i) for i in s_per]
print("listed permutation:",out_per)

