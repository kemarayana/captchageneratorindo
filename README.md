# captchageneratorindo
CAPTCHA Generator with Indonesian Word 
his project is a customizable CAPTCHA generator that creates images with random text and geometric shapes to prevent automated interactions. The primary feature of this CAPTCHA generator is its use of Indonesian words, emphasizing local culture and language. Additionally, the generator offers customization options for the background and shapes.
Features:

    Indonesian Words: The CAPTCHA text is randomly selected from a predefined list of Indonesian words, including names of foods, political figures, historical heroes, and famous places.
    Customizable Shapes: The background includes random geometric shapes (rectangles) to add complexity and make it harder for automated systems to decipher the text.
    Flexible Integration: Designed to be integrated easily into web applications using Flask.

Installation:

    Clone the Repository:

    sh

git clone https://github.com/your-username/captcha-generator.git
cd captcha-generator

Install Dependencies:
Ensure you have Pillow and Flask installed. You can install them using:

sh

    pip install pillow flask

    Download and Place the Font:
        Download the Bebas Neue font file (BebasNeue-Regular.ttf).
        Place the font file in the project directory.

Usage:

    Run the Flask Application:

    sh

    python captcha_app.py

    Access the CAPTCHA Image:
        Open your browser and navigate to http://127.0.0.1:5000/captcha to see the generated CAPTCHA image.
        The CAPTCHA string can be accessed at http://127.0.0.1:5000/captcha-string for testing or integration purposes.

Customization:

    Text Source: The text is generated from a list of Indonesian words. You can modify the indonesian_words list in the CaptchaGenerator class to include any words you prefer.
    Shapes and Background: Customize the type, color, and number of shapes drawn on the CAPTCHA by modifying the draw_random_rectangle method.
    Text Appearance: Change the font and size by adjusting the ImageFont.truetype parameters in the generate_captcha method
