# Trying out the backtracker algorithm
def permute (list, a):
    if list == 1:
        return a
    else:
        return[
            y+x
            for y in permute(1,a)
            for x in permute(list - 1, a)
        ]

# print(permute(1, ["a", "b", "c"]))
print(permute(2, ["a", "b", "c", "d"]))
# print(permute(3, ["a", "b", "c"]))