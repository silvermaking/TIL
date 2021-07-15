#%%
#로또 번호 6개 추첨 코드 
from random import sample
numbers = range(1, 46)
pick = sorted(sample(numbers, 6))
print(pick)
# %%
