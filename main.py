from PIL import Image


"""
make this into an ascii meme generator
"""


def consume_image(target, new_w):
    image = Image.open(target, mode='r').convert('L')

    orig_w, orig_h = image.size
    ratio = orig_w / orig_h
    new_h = int(new_w / ratio)
    new_h = int(new_h * .75)

    new_img = image.resize((new_w, new_h))

    return new_img


def map_to_ascii(image):
    #grays = ['@', '#', '%', '*', '=', '+', '-', '!', ';', '.']
    #grays = ['@', '%', '#', '*', '+', '=', '(', '-', ':', '.']
    grays = '@#%*=+-!:.'
    #grays = '.:!-+=*%#@'
    trans = []

    img_vals = list(image.getdata())


    for i in range(len(img_vals)):
        tmp = 0
        
        tmp = int(img_vals[i] / 25.5)
        trans.append(grays[tmp-1])

    return trans
    


def main():
    
    image = 'pic.png'
    new_w = 160

    resized_img = consume_image(image, new_w)
    img_vals = map_to_ascii(resized_img)
    
    for i in range(len(img_vals)):
        if i % new_w == 0:
            print()
        else:
            print(img_vals[i], end='')





if __name__ == '__main__':
    main()

