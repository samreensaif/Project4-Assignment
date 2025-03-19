question= "Enter measurement in Feet: "

feet =float(input(question))



def feet_to_inches(num):
  inches = num * 12
  return inches

print(f'Inches: {feet_to_inches(feet)}')
