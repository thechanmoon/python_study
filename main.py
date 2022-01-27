from calculator import plus

# print ( 1+1 );
# print( plus (1,2));

colors = ["red", "green", "blue","purble"]
dates = ["sun", "mon", "tue","wed","fri","sat"]
# i = 0;

# while i < len(colors):
#     print(colors[i])
#     i = i+1

# for color in colors:
    # print(color)

# for i in range(len(colors)):
#     print(colors[i])
#     print("Colors {}: {}".format(i + 1, colors[i]))    

# for num, color in enumerate(colors, start = 1):
#     print("Colors {}: {}".format(num,color))    


for num, color in enumerate(colors):
    print("Colors {}: {}".format(num,color))    

for color,date in zip(colors,dates):
    print("{}: {}".format(color, ",".join(date)))     

import requests
indeed_result = requests.get("https://www.indeed.com/q-python-jobs.html?vjk=05e890ee7c4d20c7");
print(indeed_result);
