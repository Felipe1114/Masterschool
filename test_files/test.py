def second_occurrence(list_items, item):
    """returns the index of the second occurrence of the item."""
    first_found = False
    index_found = None
    for i in range(1,len(list_items)):
        if list_items[i] == item:
            if first_found:
                index_found = i
                break
            else:
                first_found = True
    return index_found

# ---- automated unit test ----

assert second_occurrence([1,2,3,2],2) == 3
assert second_occurrence([1,2,3,3,2,3,2], 2) == 4
assert second_occurrence((1,2,3,4,2), 2) == 4
assert second_occurrence([], 1) == None
assert second_occurrence({1:1,2:2,3:3,4:4}, 2) == None



print("All tests passed!")
