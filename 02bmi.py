h=float(input("请输入身高:"))
w=float(input("请输入体重:"))
bmi=w/(h**2)
if bmi<18.5:
	print("过轻")
elif bmi>=18.5 and bmi<23.9:
	print("正常")
elif bmi>=24 and bmi<27:
	print("过重")
elif bmi>=28 and bmi<32:
	print("肥胖")
elif bmi>=32:
	print("非常肥胖")
print("您的身高为%.2f,体重为%.2f"%(h,w))
print("您的BMI指数为%.2f"%bmi)	
	
	
	

