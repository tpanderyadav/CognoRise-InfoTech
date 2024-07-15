import qrcode
from PIL import Image

# Function to generate and show QR code
def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    return img

data = "Hello Every one this is my code for QR-code generater"
filename = "qrcode.png"
img = generate_qr(data, filename)
print(f"QR code generated and saved as {filename}")

# Show the QR code image
img.show()






