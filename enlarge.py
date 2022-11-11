# мое решение
def enlarge(frame):
    new_frame = []
    for elem in frame:
        middle_frame = []
        for symbol in elem:
            middle_frame.append(symbol)
            middle_frame.append(symbol)
        middle_result = ''.join(middle_frame)
        new_frame.append(middle_result)
        new_frame.append(middle_result)
    return new_frame

# решение преподавателя


def enlarge_1(image):
    output = []
    for line in image:
        row = []
        for pixel in line:
            # expand horizontally
            row.extend([pixel, pixel])
        row = ''.join(row)
        # expand verticaly
        output.extend([
            row,
            row,
        ])
    return output

enlarge(frame = [''])