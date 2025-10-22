rainfall_data = {120, 150, 180, 120, 90, 110, 130}
print("Number of unique rainfall values:", len(rainfall_data))
print("Is 150 present?", 150 in rainfall_data)
rainfall_list = list(rainfall_data)
print("Set converted to list:", rainfall_list)
print("Rainfall values:")
for value in rainfall_data:
    print(value)
rainfall_data.discard(120) 
print("After removing 120:", rainfall_data)
rainfall_data.add(110)
print("After adding 110 again:", rainfall_data)
