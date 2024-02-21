def reverseList(lists):

    reversed_list = []
    for i in range(len(lists) - 1, -1, -1):
        reversed_list.append(lists[i])
    return reversed_list


def main():

    list1 = [1, 2, 3, 4]
    list2 = ["Buzz", "Bing Bong", "Mr. Incredible", "Crush"]
    list3 = [1.345, "CS110", 54, "is", 2130, "Awesome"]

    reversed_list1 = reverseList(list1)
    print("The input list is ", list1, "the reversed list is :", reversed_list1, "\n")


    reversed_list2 = reverseList(list2)
    print("The input list is ", list2, "the reversed list is :", reversed_list2,"\n")


    reversed_list3 = reverseList(list3)
    print("The input list is ", list3, "the reversed list is :", reversed_list3,"\n")

main()