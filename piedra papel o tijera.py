import random
options = ("piedra", "papel", "tijera")

for game in range(3):
    user_option = input("Escoge Piedra, Papel o Tijera: ").lower()
    if user_option not in options:
       print("Opción no válida.")
       user_option = input("Elige Piedra, Papel o Tijera: ")

    computer_option = random.choice(options)
    print("La computadora elige =>", computer_option)
    if user_option == computer_option:
      print("Es un empate, usted tiene", user_option, "y la computadora tiene", computer_option)
    elif (user_option == "piedra" and computer_option == "tijera") or (user_option == "papel" and computer_option == "piedra") or (user_option == "tijera" and computer_option == "papel"):
      print("Gana con", user_option, "y pierde la computadora con", computer_option)
    else:
      print("Gana la computadora con", computer_option, "y pierde  con", user_option)