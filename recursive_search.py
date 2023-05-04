def _search(numbers_list, target):
    if not numbers_list:
        return False
    else:
        middle_index = len(numbers_list) // 2
        middle_number = numbers_list[middle_index]
        if target == middle_number:
            return True
        elif target < middle_number:
            return _search(numbers_list[:middle_index], target)
        else:
            return _search(numbers_list[middle_index + 1:], target)
