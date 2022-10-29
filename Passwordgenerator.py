import random

print(" __    __  __       __   __  __ __")
print("|    \  /    ||    \     |    \ /    |/ _// _/")
print("|  D  )|  o  ||  _  |    |  o  )  o  (   \_(   \_ ")
print("|    / |     ||  |  |    |   /|     |\_  |\__  |")
print("|    \ |  _  ||  |  |    |  |  |  _  |/  \ |/  \ |")
print("|  .  \|  |  ||  |  |    |  |  |  |  |\    |\    |")
print("|_|\||_|||||    ||  ||| \_| \__|")
print("--------------------------------------------------")

combination = "ABCFEFGHIJKLMNOPQRSTUVWXYZ<)@)@~!%&*+)_$1234567890abcdefghijkl"

passLength = int(input("\n what is the length of password you want: "))

password = []
for each_char in range(passLength):
  password.append(random.choice(combination))

finalpassword = ""

for each in password:
  finalpassword = finalpassword + each


print("\n This is your new password: ", finalpassword)