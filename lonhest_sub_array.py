
def longest_sub_array(list):
    n = len(list)
    res = 0
    count = 0
    add = 0
    j = 0
    for i in range(n):
        if list[i] < 0:
            temp = list[i] * -1
            while add > temp:
                add -= list[j]
                count -= 1
                j += 1
            if count > 0:
                res += count+1
            add = 0
            count = 0
        else:
            add += list[i]
            count += 1
    return res

list = [2, 2, 1, -3, 4, 3, 1, -8, 6, -2, -1]
# list = [1,-1,1,0,0,-1,1,-1]
# list = [15,-2,2,-8,1,7,10,23]
print(longest_sub_array(list))
# print(sum(list))