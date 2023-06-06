import random

a = tuple(random.sample(range(20), 5))
print(f"Os valores sorteados foram: {a}")
print(f"o maior valor sorteado foi {max(a)}")
print(f"o menor numero sorteado foi {min(a)}")

