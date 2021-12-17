color_to_code = {"Baby Blue": "#89cff0", "Bitter Lemon": "#cae00d", "Blue Green": "#0d98ba", "Cadmium Red": "#e30022",
                 "Camouflage Green": "#78866b", "Carnation Pink": "#ffa6c9", "Chartreuse2": "#76ee00"}
colorName = input("Color name:")
while colorName != '':
    print(f"The code of {colorName} is {color_to_code.get(colorName)}")
    colorName = input("Color name:")


