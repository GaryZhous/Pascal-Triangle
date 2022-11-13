def pascal(number):
  counter1 = 1
  counter2 = 0
  counter3 = number - 2
  list = ''
  for i in range(number-1):
    list += " "
  list += '1'
  print(list)
  list = ''
  while counter1 < number:
    for i in range(counter3):
      list += " "
    while counter2 <= counter1:
      sum1 = 1
      for i in range(1, counter1+1):
          sum1 = sum1*i
      sum2 = 1
      if counter2 == 0:
        sum2 =1 
      else:
        for i in range(1, counter2+1):
          sum2 = sum2 * i
      sum3 = 1
      if counter1 - counter2 == 0:
        sum3 = 1
      else:
        for i in range(1, counter1-counter2+1):
          sum3 = sum3*i
      list += str(abs(int(sum1/(sum2*sum3)))) + " "
      counter2 += 1
    print(list)
    counter1 += 1
    counter2 = 0
    counter3 -= 1
    list = ''

number = int(input("enter the number of lines:"))
pascal(number)
