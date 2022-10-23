from points import get_quadrant, get_x, get_y, make_decart_point


# BEGIN (write your solution here)
def make_rectangle(point, width, height):
    return {
        "point": point,
        "width": width,
        "height": height,
    }


def get_start_point(rectangle):
    return rectangle['point']


def get_width(rectangle):
    return rectangle['width']


def get_height(rectangle):
    return rectangle['height']


def contains_origin(rectangle):
    point1 = get_start_point(rectangle)
    point2 = make_decart_point(
        get_x(point1) + get_width(rectangle),
        get_y(point1) - get_height(rectangle),
    )

    return get_quadrant(point1) == 2 and get_quadrant(point2) == 4

# END
