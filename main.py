"""Reversing list of food according to the amount of calories in it."""
class Food_item():
    food_name = ""
    calories = 0.0
    def __init__(self, afood_name, acalories):
        self.food_name = afood_name
        self.calories = acalories

    def setter_name(self, afood_name):
        self.food_name = afood_name

    def setter_cal(self, aCal):
        self.calories = aCal
def reverseTrough_slicing(list):
    list1 = list[:]
    return list1[::-1]


def reverseThrough_BuiltinFunc(list):
    list1 = list[:]
    list1.reverse()
    return list1

def reversingThrough_customFunc(list):
    list1 = list[:]
    temp = ""
    i = 0
    j = len(list) - 1
    while i < j:
       temp = list1[i]
       list1[i] = list1[j]
       list1[j] = temp
       i = i + 1
       j -= 1
    return list1

if __name__ == '__main__':
    lengthofList = int(input("Enter length of list you want to create of these objects : "))
    list = ["a", "b", "c"]
    # for i in range(lengthofList):
    #     foodName = input("Enter food name : ")
    #     cal = int(input("Enter amount of calories in entered food item : "))
    #     obj = Food_item(foodName, cal)
    #     list.append(obj)
    l1 = reverseThrough_BuiltinFunc(list)
    print(l1)
    l2 = reverseTrough_slicing(list)
    print(l2)
    l3 = reversingThrough_customFunc(list)
    print(l3)
    if l1 == l3 and l1 == l2:
        print("All list are equal after reversed.")
        print(l1)
        print(l2)
        print(l3)
    else :
        print("List are not equal after reversed.")
        print(l1)
        print(l2)
        print(l3)