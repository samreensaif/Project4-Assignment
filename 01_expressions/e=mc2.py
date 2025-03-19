ask_question: int = "Enter mass:"
speed_of_light :int = 299792458

mass = int(input(ask_question))

def calculate_energy(mass):
  energy = mass * speed_of_light**2
  return energy

print(f'Energy: {calculate_energy(mass)}')
