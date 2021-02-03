def get_shape():
    """
    certain names of shapes are valid
    if user input is the right shape break from this function
    if user input is the wrong shape, keep asking till the correct one is given
    """
    valid = ['square', 'triangle', 'pyramid', 'proper square', 'rectangle', "paralellogram"]
    while True:
        shape = input("Shape?: ").lower()
        if shape in valid: 
            break
        else:
            continue
    return shape


def get_height():
    """
    user input asks for a number
    function checks if it is a number/int
    function also checks is it in the range of 0(inclusive) and 81(exclusive)
    if they are not met, it will continue asking
    """
    while True:
        height = input("Height?: ")
        if height.isnumeric() and height:
            height = int(height)
            if height in range(0, 81):
                break
    return height


def draw_pyramid(height, outline):  
    space =  height - 1 
    stars = 1
    if outline is True:
        #i = 0
        j = 1 
        height -= 2
        h = height #actually the height
        print(" "*(height+1)+ "*")
        while 0 < (height):
            print(" " * (height) + "*" + " " * j + "*")
            j += 2 #space counter
            height -= 1 #controls the 'x'
 
        if height == 0:
            print("*" * (h * 2 + 3))
    
    else: 
        for x in range(0, height):
            print(" " * space + "*" * stars)
            space = space - 1
            stars = stars + 2
        

def draw_triangle(height, outline):
    if outline is True:
        print("*")
        print("**")
        i = 3
        j = 1
        while i < height:
            print("*" + (" " * j) + "*")
            i += 1
            j += 1
        print("*" * height, end= '')
        print()
    else:
        for x in range(0, height):
            for y in range(0, x + 1):
                    print("*", end = '')
            print()


def draw_square(height, outline):
    if outline is True:
        print("*" * height)
        for i in range (height-2):
            print('*' + ' ' * (height - 2) + "*")
        print("*" * height)
    else:
        for i in range (height):
            print('*'*height)


def draw_rectangle(height, outline):
    if outline is True:
        i = 0 
        print("*" * height)
        while i < (height - 2):
            print("*" + " " * (height - 2) + "*")
            i += 1
        print("*" * height)
    else:
        for row in range(0, height):
            print("*" * height)
        

def draw_paralellogram(height, outline):
    if outline is True:
        print(" " * (height - 1) + "*" * height) 
        for row in range(0, height-2):
            print(" " * (int(height) - row - 2) + "*" + " "* (int(height)-2) + '*')
        print("*" * height) 
            
    else:
        for row in range(0, height):
            print(" " * (height - row - 1) + "*" * height)   
        
        
def draw_proper_square(height, outline):
    if outline is True:
        print("* " * height)
        for i in range (height-2):
            print('* ' + '  ' * (height - 2) + "* ")
        print("* " * height)
    else:
        for i in range (height):
            print('* '*height)


def draw(shape, height, outline):
    """
    compares the user input shape name to a particular name
    if the name is equal to the given shape name, it goes to that specific function
    """
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    elif shape == 'square':
        draw_square(height, outline)
    elif shape == 'triangle':
        draw_triangle(height, outline)
    elif shape == 'rectangle':
        draw_rectangle(height, outline)
    elif shape == 'proper square':
        draw_proper_square(height, outline)
    elif shape == "paralellogram":
        draw_paralellogram(height, outline)


def get_outline():
    """
    user input is asked whether it should an outline or not
    y returns true ... an outline
    n returns false ... a full shape
    """
    outline = input("Outline only? (Y/N)").lower()
    if outline == "y":
        return True
    else:
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw (shape_param, height_param, outline_param)
