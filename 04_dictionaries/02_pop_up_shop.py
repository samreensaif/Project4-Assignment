
fruit_list={'mango':200,
            'banana':150,
            'jackfruit':200,
            'pear':100,
            'grapes':200}

total_cost = 0
for i in fruit_list:
  
  price = fruit_list[i]

  amount = int(input(f"How many {i} u want to buy? "))
  total_cost += amount * price

print("total cost", total_cost)
