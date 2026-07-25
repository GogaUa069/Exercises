from PIL import Image

def image_to_ascii(path, width=150):
    img = Image.open(path)
    img = img.convert("L")
    w_percent = (width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((width, h_size))

    chars = "@%#*+=-:. "
    ascii_str = ""
    for pixel in img.getdata():
        ascii_str += chars[pixel // 25]
    ascii_img = [ascii_str[index: index + width] for index in range(0, len(ascii_str), width)]
    print("\n".join(ascii_img))

image_to_ascii(r"C:\Users\Егор\Downloads\TournamentProductionLogo.png")
# C:\Users\Егор\Downloads\MyFace.jpg
