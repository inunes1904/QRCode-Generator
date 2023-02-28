# 1 - install libraries
import qrcode

# 2 - create a function that collects text and converts it to a qrcode
def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10, border=4,
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

# 3 - save QRCode as an image
    img.save("qrimg.png")

# 4 - Run The Function
generate_qrcode("https://www.jeronimomartins.com")