colors = ("red", "green", "blue")
shapes = ("circle", "square", "triangle")
art = colors + shapes
print(art)
repeat = colors * 3
print(repeat)
art = ('red', 'green', 'blue', 'circle', 'square', 'triangle')
art_list = list(art)
art_list.append("Diamond")
art = tuple(art_list)
print(art)
middle_element = art[len(art)//2]
print(middle_element)
find = "square" in art
print(find)