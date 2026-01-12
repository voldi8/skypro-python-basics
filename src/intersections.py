def intersections(a: list[int], b: list[int]) -> list[int]:
    """
    Возвращает список чисел, которые присутствуют в обоих списках.

    Порядок элементов сохраняется в соответствии со списком 'a`.
    """
    b_set = set(b)
    return [x for x in a if x in b_set]

def is_palyndrom_digit(a: list[int]) -> list[int]:

    
        