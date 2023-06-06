def escreva(msg):
  i = len(msg) + 6
  print('~' * i)
  print(f'{msg:^{i}}')
  print('~' * i)


escreva("HELLOWORLD")
escreva("HELLOWORLDHELLOWORLD")
escreva("HELLOWORLDHELLOWORLDHELLOWORLD")
