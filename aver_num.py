def main():
	sum=0
	cnt=eval(input("Enter a number:"))
	for i in range(cnt):
		num=eval(input("Type a number: "))
		sum=sum+num
	avg=sum/cnt
	print("avg=",avg)

main()
