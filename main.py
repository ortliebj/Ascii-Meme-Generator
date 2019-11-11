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

    img_w, img_h = img.size
    top_text_w, top_text_h = draw.textsize(top_text)
    bottom_text_w, h_btxt = draw.textsize(bottom_text)
    
    upper_rect_size = (top_text_w+4, top_text_h)
    bottom_rect_size = (bottom_text_w+4, h_btxt)

    # Black wasn't working, #C2C2C2 is the darkest I could get
    upper_rect = Image.new('L', upper_rect_size, color='#C2C2C2')
    bottom_rect = Image.new('L', bottom_rect_size, color='#C2C2C2')

    rect_top_x = int((img_w - upper_rect_size[0]) / 2)
    rect_top_y = 1

    rect_bottom_x = int((img_w - bottom_rect_size[0]) / 2)
    rect_bottom_y = int(img_h - bottom_rect_size[1])

    ux = int((upper_rect_size[0] - top_text_w) / 2)
    uy = -1

    bx = int((bottom_rect_size[0] - bottom_text_w) / 2)
    by = 0

    urect_draw = ImageDraw.Draw(upper_rect)
    urect_draw.text((ux, uy), top_text, fill='#0000f0')
    brect_draw = ImageDraw.Draw(bottom_rect)
    brect_draw.text((bx, by), bottom_text, fill='#0000f0')

    canvas.paste(img)
    canvas.paste(upper_rect, (rect_top_x, rect_top_y))
    canvas.paste(bottom_rect, (rect_bottom_x, rect_bottom_y))

    return canvas

def save_art(img_vals, width):
    try:
        with open('pic.txt', 'w') as f:
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