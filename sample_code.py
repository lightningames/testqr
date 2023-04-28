import qrcode
import svgwrite
# import io
# from PIL import Image

# Set the X and Y coordinates for the QR code
qr_x = 100
qr_y = 100

# Generate the QR code
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=10,
                   border=1)
qr.add_data("Hello, World!")
qr.make(fit=True)

# Create an SVG container
dwg = svgwrite.Drawing('output.svg', profile='full', size=('1500px', '1500px'))

# Load the background image and add it as an SVG element
bg_element = dwg.image(href="iceberg.svg")
dwg.add(bg_element)

# Draw the QR code onto the SVG canvas
qr_image = qr.make_image(fill_color="black", back_color="white")
qr_width, qr_height = qr_image.size
qr_canvas = dwg.add(dwg.g())

# Add annotations to the SVG canvas
qr_canvas.add(dwg.text("Hello, World!", insert=(qr_x, qr_y + qr_height + 50), font_size="50"))
qr_canvas.add(dwg.rect(insert=(qr_x - 10, qr_y - 10), size=(qr_width + 20, qr_height + 20), fill="white", stroke="#FF0000"))

for row in range(qr_width):
    for col in range(qr_height):
        if qr_image.getpixel((row, col)):
            x = qr_x + row
            y = qr_y + col
            qr_canvas.add(dwg.rect(insert=(x, y), size=(1, 1), fill='black', opacity=1.0))


# Save the SVG image
dwg.save()

# TODO here convert SVG to PNG as a datastream
# svg_bytes = dwg.tostring().encode('utf-8')

# Load SVG data from string
# im = Image.open(io.BytesIO(svg_bytes))

# Save as PNG
#im.save('output.png')
