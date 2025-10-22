rainfall_chennai = {120, 140, 160, 180}
rainfall_madurai = {110, 130, 150, 180}
rainfall_coimbatore = {100, 120, 180, 200}
unique_chennai_madurai = rainfall_chennai.union(rainfall_madurai)
print("Unique rainfall in Chennai and Madurai:", unique_chennai_madurai)
all_rainfall_update = rainfall_chennai.copy()  
all_rainfall_update.update(rainfall_madurai, rainfall_coimbatore)
print("All rainfall (update method):", all_rainfall_update)
all_rainfall_union = rainfall_chennai.union(rainfall_madurai, rainfall_coimbatore)
print("All rainfall (union method):", all_rainfall_union)
common_rainfall = rainfall_chennai.intersection(rainfall_madurai, rainfall_coimbatore)
print("Common rainfall in all cities:", common_rainfall)
unique_chennai = rainfall_chennai - (rainfall_madurai.union(rainfall_coimbatore))
print("Unique rainfall in Chennai:", unique_chennai)