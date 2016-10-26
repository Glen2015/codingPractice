price = [0, 1, 5, 8, 9, 10 ,17, 17, 20, 24, 30]

#print price[4]
def cut_rod(price, n):
	if n == 0:
		return 0
	else:
		q = -10000
	#print n
	
	for i in range(1, n + 1): #
		q= max(q, price[i] + cut_rod(price, n - i))
	return q
	

#
if __name__ == "__main__":
	print cut_rod(price, 4)

