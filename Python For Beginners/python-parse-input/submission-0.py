from typing import List

def read_integers() -> List[int]:
   line = input() 
   strings = line.split(",")
   user_list = []

   for i in strings:
    user_list.append(int(i))
   return user_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
