def Boss_Baby_Revenge(string):
  chars = list(string.upper())
  rev = 0

  print(f"Input: {string.upper()}")
  
  for char in chars:
    if char == "R" and chars.index(char) == 0:
      rev += 1
      break
    if char == "S":
      rev += 1
    elif char == "R":
      rev -= 1
    elif chr != "R" or char != "S":
      print("Wrong Input")
      break

    if rev < 0:
      rev = 0;

  if rev > 0:
    print("Output:", "Bad Boy")
  else:
    print("Output:", "Good Boy")

if __name__ == "__main__":
  String_Input = input("Input Sequence Event: ")
  Boss_Baby_Revenge(String_Input)