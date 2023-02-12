#install all the libraries needed
#create a function that collects a text and convert it to a qrcode
#save yhe qrcode as an image
#create a function that takes the image and converts ito to a text
#run the function

import qrcode

def generate_qrcode(text):

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=  qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )

        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qr-img.png")

        print("QR Code generate successfully")
    except Exception as e:
        print("Error. Is not possible to complete your request")

url = input("Enter your URL: ")

generate_qrcode(url)