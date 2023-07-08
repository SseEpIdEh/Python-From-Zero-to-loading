#Colorgram analyzes the pixels of an image and extracts the dominant colors present in the image.
# It can be useful for various purposes, such as generating color palettes, analyzing color distribution,
# or creating visualizations based on the colors in an image.

import colorgram

rgb_colors=[]
colors = colorgram.extract("hirst_spot_image.jpg",30)
for color in colors:
    r=color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)
#output
color_list=[(198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205), (109, 67, 85), (39, 35, 34), (223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108), (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59), (193, 190, 192), (17, 78, 98), (215, 184, 172), (190, 190, 195), (78, 72, 31)]



