# Interview Cake: Rectangular Love
# https://www.interviewcake.com/question/python/rectangular-love
# Miguel Aroca-Ouellette
# 08/09/2016

def love_intersection(rec1, rec2):
    """
    Finds the rectangular intersection of two love rectangles.
    """

    love_rec = {
        'left_x': None,
        'bottom_y': None,
        'width': None,
        'height': None,
    }

    # Step 1: Store vertical and horizontal line information.
    lines1 = {'bot': rec1['bottom_y'], 'top': rec1['bottom_y'] + rec1['height'],
              'left': rec1['left_x'], 'right': rec1['left_x'] + rec1['width']}
    lines2 = {'bot': rec2['bottom_y'], 'top': rec2['bottom_y'] + rec2['height'],
              'left': rec2['left_x'], 'right': rec2['left_x'] + rec2['width']}

    # Step 2: Get overlap
    x_over = {'right': min(lines1['right'], lines2['right']), 'left': max(lines1['left'], lines2['left'])}
    y_over = {'top': min(lines1['top'], lines2['top']), 'bot': max(lines1['bot'], lines2['bot'])}
    width = x_over['right'] - x_over['left']
    height = y_over['top'] - y_over['bot']

    # Step 3: Return rectangle
    if width > 0 and height > 0:
        love_rec['left_x'] = x_over['left']
        love_rec['bottom_y'] = y_over['bot']
        love_rec['width'] = width
        love_rec['height'] = height

    return love_rec


# Some test rectangles
rec1 = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 1,

    # width and height
    'width': 6,
    'height': 4,
}

rec2 = {
    # coordinates of bottom-left corner
    'left_x': 6,
    'bottom_y': 4,

    # width and height
    'width': 2,
    'height': 3,
}

rec3 = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 3,

    # width and height
    'width': 6,
    'height': 2,
}

rec4 = {
    # coordinates of bottom-left corner
    'left_x': 4,
    'bottom_y': 4,

    # width and height
    'width': 1,
    'height': 1,
}

print love_intersection(rec3, rec4)
