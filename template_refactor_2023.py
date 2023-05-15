from PIL import Image, ImageDraw, ImageFont
import qrcode
import yaml

def get_config(config_file: str):
    # fixed variables in config.yml
    try:
        with open(config_file, 'rb') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error loading {config_file}: {e}")
        config = {}
    return config


def create_laisee_qrcode(lnurl: str, idnumber: str, expires: str, sats: str,  config: dict):
    try:

        qr_x = int(config['qr_x'])
        qr_y = int(config['qr_y'])
        width = int(config['width'])
        height= int(config['height'])
        qr_offset = int(config['qr_offset'])
        qr_fill_color = config['qr_fill_color']
        qr_back_color = config['qr_back_color']
        box_stroke_color = config['box_stroke_color']
        box_fill_color = config['box_fill_color']
        template_name = config['template_name']
        qr_box_size = config['qr_box_size']
        qr_border = config['qr_border']
        
        #text_stroke_color = config['text_stroke_color']
        text_fill_color = config['text_fill_color']
        sats_font = config['sats_font']
        sats_font_size = config['sats_font_size']
        sats_vertical_offset = config['sats_vertical_offset']
        other_font = config['other_font']
        other_font_size = config['other_font_size']
        other_vertical_offset = config['other_vertical_offset']

        output_filename = "output" + idnumber + ".png"

        # get a font
        sfnt = ImageFont.truetype(sats_font, sats_font_size)
        fnt = ImageFont.truetype(other_font,other_font_size )

        with Image.open(template_name) as im:

            draw = ImageDraw.Draw(im)

            draw.rectangle([(qr_x, qr_y), (qr_x+width, qr_y+height)], fill=box_fill_color, outline=box_stroke_color, width=2)

            sats_content = sats + " sats"
            draw.multiline_text((qr_x+qr_offset, qr_y+sats_vertical_offset), sats_content, font=sfnt, fill=text_fill_color)
            # draw multiline text
            data_content = "Expires: " + expires + "\n" + "ID:" + idnumber
            draw.multiline_text((qr_x+qr_offset, qr_y+other_vertical_offset), data_content, font=fnt, fill=text_fill_color)

            # Generate the QR code
            pos = (qr_x+qr_offset, qr_y+qr_offset)
            qr = qrcode.QRCode(version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_L,
                            box_size=qr_box_size,
                            border=qr_border)
            qr.add_data(lnurl)
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color=qr_fill_color, back_color=qr_back_color)

            im.paste(qr_image, pos)

            im.show()
            im.save(output_filename)
            return output_filename
    except Exception as e:
        return e.tostring()


if __name__ == '__main__':
    """
    README:  run this command on the cli to test:
    $ rm out* ; python3 template_refactor_2023.py; open output.svg; open output.png
    """

    print("inside template_refactor 2023")
    # these datapoints will come from another method in the bigger repository
    lnurl = "LNURL1DP68GURN8GHJ7MR9VAJKUEPWD3HXY6T5WVHXXMMD9AKXUATJD3CZ7CTSDYHHVVF0D3H82UNV9UUNWVCE4EM6P"
    idnumber = "f7bsdfoijlijljs"
    expires = "2023-05-15"
    sats = "2500"

    path  = "./"
    config_file = path + 'config.yml'
    config = get_config(config_file)
    print(config)

    result = create_laisee_qrcode(lnurl, idnumber, expires, sats, config)
    print(f'Output svg created: {result}')