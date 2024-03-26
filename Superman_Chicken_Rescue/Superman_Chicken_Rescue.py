def rescue_chicken(roof_height, chicken_positions):
  if not chicken_positions:
      return 0 
  try:
      chicken_positions = list(map(int, chicken_positions))
  except ValueError:
      print("Invalid input: Please enter comma-separated integers for chicken positions.")
      return 0

  num_rescued = 0
  size = len(chicken_positions)
  for i in range(size):
    reach = chicken_positions[i] + roof_height - 1
    count = 1
    for j in range(size):
      if reach >= chicken_positions[j]:
        count += 1
      else:
        break
    if count > num_rescued:
      num_rescued = count
  return num_rescued

if __name__ == "__main__":
  roof_height = int(input("Enter Superman Roof: "))
  chicken_positions_str = input("Enter Superman Chickens Position 'comma-separated integers': ")
  chicken_positions = chicken_positions_str.split(",")

  max_rescued = rescue_chicken(roof_height, chicken_positions)
  print("Maximum Chickens Rescued:", max_rescued)
