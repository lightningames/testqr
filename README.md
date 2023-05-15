# QRimgtest

test repo for embedding logo into QR image and color, format customization
- This repository is a sub repo of a larger project, called https://laisee.org


## README:

- Update your Template background and colors in the **config.yml file**
- The old method is using template_test.py (ignore this, its in the 2021 folder)


## New method (2023) - how to run

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 template_refactor_2023.py
```

Requires at least python3.8

## Result

Final image after QR code and background SVG image are merged together in a PNG should look like this image below. 
IMPORTANT: The final image MUST be in PNG format, it cannot be in SVG. 

![finalimage](https://github.com/bitkarrot/QRimgtest/blob/main/outputf7bsdfoijlijljs.png)


