def is_rect_in_rect(inner, outer):
    pass

def is_rect_intersect_rect(first, second):
    return not ((first.x + first.width) < second.x
        or first.x > (second.x + second.width)
        or (first.y + first.height) < second.y
        or first.y > (second.y + second.height))
