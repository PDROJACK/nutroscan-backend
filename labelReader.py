import os

import re

filename = './nut.txt'

def getNumbers(str): 
    array = re.findall(r'[0-9]+', str) 
    return array 


with open(filename) as f:
    content = f.readlines()
    
content = [x.strip() for x in content if len(x) > 1]

def findStartEnd(content):
    start = 0
    end = 0
    for i, val in enumerate(content):
        if val is "Nutrition Facts":
            start=i

        if val is "Dietary Fiber":
            end=i

    return content[start:end+1]

 

def makeDict(content):
    content = findStartEnd(content)

    def getNum(x,y):
        array = re.findall(r'[0-9]+', content[x])
        return array[y]
    res = {
            "Serving Size":  (getNum(2,0), "oz"),
            "Serving Per Container": (getNum(3,0)),
            "Calories": (getNum(6,0)),
            "Calories from Fat": (getNum(6,1)),
            "Total Fat": (getNum(10,0)),
            "Saturated Fat": (getNum(12,0)),
            "Trans Fat": (getNum(14,0)),
            "Cholesterol": (getNum(15,0)),
            "Sodium": (getNum(16,0)), 
            "Total Carbohydrate": (getNum(17,0)),
            "Dietary Fiber": (getNum(19,0)),
            "Sugars": (getNum(21,0)),
            "Protein": (getNum(23,0)),
            "Vitamin A": (getNum(26,0)),
            "Vitamin C": (getNum(26,1)),
            "Calcium": (getNum(28,0)),
            "Iron": (getNum(28,1),"%"),
            "Calories": (getNum(34,0)),
            "Total Fat Less than": (getNum(35,0), "g"),
            "Sat Fat": (getNum(36,0), "g"),
            "Cholesterol": (getNum(37,0), "mg"),
            "Sodium Less than": (getNum(38,0), "mg"),
            "Total Carbonhydrate": (getNum(39,0), "mg"),
            "Dietary Fiber": (getNum(40,0), "g")
            }

    return res;

 
# print(content)
print(findStartEnd(content))