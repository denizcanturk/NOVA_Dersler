import qrcode

# Define the string you want to encode in the QR code
data = "Adı : Aydan\nSoyadı : Geçer \n Acil Durum No.: 05316774317\n Mersin\\Mezitli"

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
    box_size=20,  # controls how many pixels each “box” of the QR code is
    border=10,  # controls how many boxes thick the border should be
)

# Add the data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'")