
# Solution of the challenge FindIntersection proposed on Coderbyte at https://coderbyte.com/challenges

"""
After converting the input into two lists of integers, we should convert these lists to sets. If the 
intersection of these sets is empty, we return false. Otherwise, we return all the elements of the 
intersection
"""

def FindIntersection(strArr):

    first = [int(item) for item in strArr[0].split(", ")]
    second = [int(item) for item in strArr[1].split(", ")]

    first_set = set(first)
    second_set = set(second)

    inter = first_set.intersection(second_set)
    inter = list(inter)

    if len(inter) == 0:
        return "false"
    else:
        return ','.join(str(x) for x in sorted(inter))

# keep this function call here
print(FindIntersection(input()))

