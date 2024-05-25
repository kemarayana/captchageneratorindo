import random
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

default_color_red = 228
default_color_green = 150
default_color_blue = 150

#list of possible word , can be a DB connector
indonesian_words = [
    'nasi_goreng', 'sate', 'rendang', 'gudeg', 'soto', 'bakso', 'tempe', 'gado-gado', 'mie_goreng', 'pempek',
    'soekarno', 'hatta', 'sukarno', 'megawati', 'jokowi', 'sby', 'gusdur', 'prabowo', 'anwar', 'rizal',
    'diponegoro', 'kartini', 'sudirman', 'bung_tomo', 'pattimura', 'cut_nyak_dien', 'ki_hajar_dewantara', 'imam_bonjol', 'tan_malaka', 'ahmad_dahlan',
    'borobudur', 'prambanan', 'bali', 'komodo', 'toba', 'bromo', 'toraja', 'yogyakarta', 'jakarta', 'surabaya',
    'bandung', 'medan', 'makassar', 'lombok', 'raja_ampat', 'semarang', 'solo', 'palembang', 'pontianak', 'manado'
]

def generate_random_string():
    return random.choice(indonesian_words)

def draw_random_rectangle(draw):
    # A random rectangle on the image
    a = random.randrange(10, 300, 1)
    b = random.randrange(10, 275, 1)
    c = a + random.randrange(10, 90, 1)
    d = b + random.randrange(10, 90, 1)
    draw.rectangle((a, b, c, d), fill=(
        default_color_red + random.randrange(-100, 100, 1),
        default_color_green + random.randrange(-100, 100, 1),
        default_color_blue + random.randrange(-100, 100, 1), 255),
        outline="black")

def generate_captcha():
    '''
    Generate a captcha
    :return: A tuple (image, captcha string that encoded in the image)
    '''
    captcha_string = generate_random_string()
    captcha_image = Image.new("RGBA", (400, 200), (255, 255, 255))  # White background
    draw = ImageDraw.Draw(captcha_image, "RGBA")
    for i in range(1, 20):
        draw_random_rectangle(draw)

    fontStyle = ImageFont.truetype("/content/BebasNeue-Regular.ttf", 48)  # font is in the specified path

    # Arbitrary starting co-ordinates for the text we will write
    x = 10 + random.randrange(0, 100, 1)
    y = 79 + random.randrange(-10, 10, 1)

    draw.text((x, y), captcha_string, (0, 0, 0), font=fontStyle)  # Write in black

    return captcha_image, captcha_string  # return a heterogeneous tuple

# Main
result = generate_captcha()
myCaptcha = result[0]
captcha_string = result[1]
print(">" + captcha_string + "<")

# Display the image in Colab
myCaptcha.show()

# To display in Colab
plt.imshow(myCaptcha)
plt.axis('off')
plt.show()

