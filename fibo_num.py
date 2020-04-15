def fibo(num):
	if num==1 or num==2:
		return 1
	else:
		return fibo(num-1)+fibo(num-2)

def main():
	n1=eval(input("fibonacci number? "))
	for i in range(1,n1+1):
		if i==10:
			print(fibo(i)) 
			break
		print(fibo(i),end=',')
	print("F",n1,"=",fibo(n1))

main()	

