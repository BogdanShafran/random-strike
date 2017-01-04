def is_rect_in_rect(inner, outer):
    pass

def is_rect_intersect_rect(first, second):
    return not (int(first.x + first.width) <= int(second.x)
        or int(first.x) >= (int(second.x) + second.width)
        or (int(first.y) + first.height) <= int(second.y)
        or int(first.y) >= (int(second.y) + second.height))
