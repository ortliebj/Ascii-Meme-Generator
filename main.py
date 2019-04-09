from PIL import Image, ImageDraw, ImageFont


def resize_image(image, new_w):
    orig_w, orig_h = image.size
    ratio = orig_w / orig_h
    new_h = int((new_w / ratio)*0.55)
    #new_h = int(new_h * 0.5)

    new_img = image.resize((new_w, new_h))

    return new_img


def map_to_ascii(image):
    grays = '@#%*=+-!:.'
    trans = []

    img_vals = list(image.getdata())

    for i in range(len(img_vals)):
        tmp = 0
        
        tmp = int(img_vals[i] / 25.5)
        trans.append(grays[tmp-1])

    return trans


def draw_text(img, top_text, bottom_text):
    draw = ImageDraw.Draw(img)
    w_img, h_img = img.size

    w_ttxt, h_ttxt = draw.textsize(top_text)

    ux = (w_img - w_ttxt) / 2
    uy = h_img * 0.02

    #uborder = [(ux-1, uy-1), (ux+w_ttxt, uy+h_ttxt)]

    #draw.rectangle(uborder, fill='black')
    draw.text((ux, uy), top_text, fill='white')

    w_btxt, h_btxt = draw.textsize(bottom_text)

    bx = (w_img - w_btxt) / 2
    by = h_img * 0.8

  #  draw.rectangle(bborder, fill='black')
    draw.text((bx, by), bottom_text, fill='white')


"""
def save_art(img_vals, width):
    try:
        with open('file.txt', 'w') as f:
            for i in range(len(img_vals)):
                if i % width == 0:
                    f.write('\n')
                else:
                    f.write(img_vals[i])
    except FileNotFoundError:
        print('[-] File Not Found')
"""

def main():
    img_name = 'picc.png'
    image = Image.open(img_name, mode='r').convert('L')

    new_w = 120
    image = resize_image(image, new_w)

    top_text = 'top text'
    bottom_text = 'bottom text'

    draw_text(image, top_text, bottom_text)

    img_vals = map_to_ascii(image)

    
    for i in range(len(img_vals)):
        if i % new_w == 0:
            print()
        else:
            print(img_vals[i], end='')

#    save_art(img_vals, new_w)




if __name__ == '__main__':
    main()
