from calculator import plus

# print ( 1+1 );
# print( plus (1,2));

colors = ["red", "green", "blue","purble"]
# i = 0;

# while i < len(colors):
#     print(colors[i])
#     i = i+1

for color in colors:
    print(color)

# for i in range(len(colors)):
#     print(colors[i])
#     print("Colors {}: {}".format(i + 1, colors[i]))    

for num, color in enumerate(colors, start = 1):
    print("Colors {}: {}".format(num,color))    