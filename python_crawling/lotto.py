#%%
#로또 번호 6개 추첨 코드 
from random import sample
numbers = range(1, 46)
pick = sorted(sample(numbers, 6))
print(pick)
# %%
dust = 100

if dust > 30 : 
    print('좋음')

elif dust > 80 :
    print(1)
# %%
n = 0
while n <= 5:
    print('출력')
    n = n+1
# %%
