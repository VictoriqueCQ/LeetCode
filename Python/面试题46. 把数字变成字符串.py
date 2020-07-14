class Solution:
    def translateNum(self, num: int) -> int:
    	num=str(num)
    	if len(num)==1:
    		return 1
    	n_minus_2=1
    	n_minus_1=1
    	res=0
    	for i in range(1,len(num)):
    		flag=num[i-1:i+1]
    		if int(flag)>25 or int(flag)<10:
    			res=n_minus_1
    		else:
    			res=n_minus_1+n_minus_2
    		n_minus_2,n_minus_1=n_minus_1,res
    	return res