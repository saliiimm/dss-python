def is_prime(num: int):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

count = 0
num = 2
while count < 10:
  if is_prime(num):
    print(num)
    count += 1
  num += 1
  
if is_prime(3):
    print('chiffre donne premier')
    

