list1 = (input())
list2 = (input())

def sum_of_products(list1, list2):
    sum = 0
    for i in range(len(list1)):
        sum += int(list1[i]) * int(list2[i])
    return sum

if __name__ == '__main__':
    if len(list1) != len(list2):
        print ("Error.")
        
    if len(list1) == len(list2):
        print(sum_of_products(list1, list2))