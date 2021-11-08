from collections import defaultdict, Counter
from itertools import combinations 

def solution(orders, course):
    answer = []
    orders_dic = defaultdict(int)
    for order in orders:
        order = sorted(order)
        orders_dic[tuple(order)] += 1 
        if len(order) > 2:
            for j in range(2, len(order)):
                for set_menu in combinations(order, j):
                    orders_dic[set_menu] += 1
   
    counter = Counter(orders_dic)
    menus = list(counter.items())
 
    for num in course:
        temp = []
        for menu in menus:
            if num == len(menu[0]) and counter[menu[0]] >= 2:
                temp.append(menu)
                
        temp.sort(key=lambda x: x[1], reverse=True)
        for menu in temp:
            if menu[1] == temp[0][1]:
                answer.append(''.join(menu[0]))

    return sorted(answer)

if __name__ == '__main__':

    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2, 3, 4]
    orders2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    course2 = [2, 3, 5]
    orders3 = ["XYZ", "XWY", "WXA"]
    course3 = [2, 3, 4]

    print(solution(orders, course))
    print(solution(orders2, course2))
    print(solution(orders3, course3))
