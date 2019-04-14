from PIL import Image, ImageDraw, ImageFont


def resize_image(image, new_w):
    orig_w, orig_h = image.size
    ratio = orig_w / orig_h
    #Spacing between lines is more than spacing between 
    #characters, so we take a percentage of it
    new_h = int((new_w / ratio) * 0.55)

    new_img = image.resize((new_w, new_h)).convert('L')

    return new_img


def map_to_ascii(image):
    grays = '@#%*=+-!:.'
    trans = []

    img_vals = list(image.getdata())

    for val in img_vals:
        tmp = 0
        tmp = int(val / 25.5)
        trans.append(grays[tmp-1])

    return trans


def draw_text(img, top_text, bottom_text):
    canvas = Image.new('L', img.size, 'black')
    draw = ImageDraw.Draw(canvas)

    w_img, h_img = img.size
    w_ttxt, h_ttxt = draw.textsize(top_text)
    w_btxt, h_btxt = draw.textsize(bottom_text)
    
    up_rect_size = (w_ttxt+4, h_ttxt)
    bottom_rect_size = (w_btxt+4, h_btxt)

    # Black wasn't working, #C2C2C2 is the darkest I could get
    urect = Image.new('L', up_rect_size, color='#C2C2C2')
    brect = Image.new('L', bottom_rect_size, color='#C2C2C2')

    rtx = int((w_img - up_rect_size[0]) / 2)
    rty = 1

    rbx = int((w_img - bottom_rect_size[0]) / 2)
    rby = int(h_img - bottom_rect_size[1])

    ux = int((up_rect_size[0] - w_ttxt) / 2)
    uy = -1

    bx = int((bottom_rect_size[0] - w_btxt) / 2)
    by = 0

    urect_draw = ImageDraw.Draw(urect)
    urect_draw.text((ux, uy), top_text, fill='#0000f0')
    brect_draw = ImageDraw.Draw(brect)
    brect_draw.text((bx, by), bottom_text, fill='#0000f0')

    canvas.paste(img)
    canvas.paste(urect, (rtx, rty))
    canvas.paste(brect, (rbx, rby))

    return canvas


def save_art(img_vals, width):
    try:
        with open('file.txt', 'w') as f:
            for i, val in enumerate(img_vals):
                if i % width == 0:
                    f.write('\n')
                else:
                    f.write(val)
    except FileNotFoundError:
        print('[-] File Not Found')


def main():
    img_name = 'pic.png'
    image = Image.open(img_name, mode='r')

    new_w = 120
    image = resize_image(image, new_w)

    top_text = input('Top Text : ')
    bottom_text = input('Bottom Text : ')

    canvas = draw_text(image, top_text, bottom_text)

    img_vals = map_to_ascii(canvas)

    
    for i, val in enumerate(img_vals):
        if i % new_w == 0:
            print()
        else:
            print(val, end='')

    print('\n')

    save_art(img_vals, new_w)


if __name__ == '__main__':
    main()