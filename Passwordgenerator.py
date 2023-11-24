import random

print("************************************************************************\ ") 
print("@@@@@@@@@@@@@@@@@@@@ copyright of Mr_Cyber 2023 @@@@@@@@@@@@@@@@@@@@@@@@/") 
print("************************************************************************\ ") 
print("************************************************************************/") 
print(" _         _    ___         ______           ______     ______    ___")
print("| \       / | |     \     /         \     / |       \  |        |      \ ")
print("|  \     /  | |  D   )   /           \   /  |   D    | |        |   O   )")
print("|   \ _ /   | |     /   /             \ /   | _____ /  |______  |      /")
print("|     O     | |    / __ \              |    |       \  |        |     /")
print("|    ___    | |  _ \     \             |    |   D    | |        |  __ \ ")
print("| _ |   | _ | |_| |_\     \ ______     |    | ______ / |______  |_|  |_\ ")
print("************************************************************************")
print("@@@@@@@@@@@@@ github link = https://github.com/Mr-cyber200 @@@@@@@@@@@@@") 
print("LinkendIn link = https://www.linkedin.com/in/nwarienne-michael-378b5a183") 
print("************************************************************************")
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
