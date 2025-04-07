import qrcode

# Data to be encoded
data = input("Enter the text or URL to encode in QR Code: ")

# Create QR Code
qr = qrcode.QRCode(
    version=1,  # controls size of the QR code
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qrcode.png")

print("✅ QR Code has been generated and saved as 'my_qrcode.png'")

# ===================================================

