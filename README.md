# testqr

test repo for embedding logo into QR image and color, format customization

## TODO

- remove dependency on rsvg-convert
- remove dependency on templates
- migrate method in template_test.py to svgwrite as in sample_code.py 

## how to run

rsvg-convert  -  to be deprecated, install unbuntu: 

```
sudo apt install librsvg2-bin
sudo apt-get rsvg-convert
```

Requires at least python3.8

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 template_test.py 
```

- change colors in template_test.py

- EDIT SVG TEMPLATE FILE to refer to qr_code, idnumber, expires and sats
with {{ }}, For example: 

```<image
         width="166.29921"
         height="166.51379"
         preserveAspectRatio="none"
         href={{qrcode}}
         id="image4277"
         x="811.72894"
         y="208.38103" />
```

## Result

Final image after QR code and background SVG image are merged together in a PNG should look like image below. 
IMPORTANT: The final image MUST be in PNG format, it cannot be in SVG. 

Example: 
https://user-images.githubusercontent.com/73979971/230754313-1fef33c2-37b9-4d6f-ba5d-ea0b0e6cef50.jpeg


