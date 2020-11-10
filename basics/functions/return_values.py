def sum_weights(Beep_weight, bop_weight):
  total_weight = Beep_weight + bop_weight
  return total_weight

def calc_avg_weight(Beep_weight, bop_weight):
  average = (Beep_weight + bop_weight) / 2

  return average

def run():
  print('What is the weight of Beep?')
  Beep_weight = float(input())

  print('What is the weight of Bop?')
  bop_weight = float(input())

  print('What would you like to calculate (sum or average)?')
  calculate = input()

  if calculate == 'sum':
    print('The sum of Beep and Bop''s weight is', sum_weights(Beep_weight, bop_weight))

  elif calculate == 'average':
    print('The average of Beep and Bop''s weight is', calc_avg_weight(Beep_weight, bop_weight))
  
  else:
    print('i''m not sure what you want me to do')

run()

