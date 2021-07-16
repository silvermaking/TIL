#로또 번호 6개 추첨 코드 
from random import sample
def get_lotto_num():
    numbers = range(1, 46)
    pick = sorted(sample(numbers, 6))
    return pick

