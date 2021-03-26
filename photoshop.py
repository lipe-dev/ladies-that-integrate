import os
import random
import re

from PIL import ImageFont, Image, ImageDraw

from argparser import parse_args

MAX_LINE_WIDTH = 1000
X_50_PERCENT = 540

Y_MIDDLE_OF_TEXT_AREA = 1130
Y_MIDDLE_OF_LINK_AREA = 1540

FONT_SIZE = 80

SAMPLE_TEXT = "Reject your humanity, return to monkey. " \
              "Apes together strong! Because of a single reason: diamond hands go to the moon."

IMAGES = [os.path.join("backgrounds", "black.png"), os.path.join("backgrounds", "purple.png")]

bariol = ImageFont.truetype('bariol.ttf', FONT_SIZE)


def has_punctuation(text):
    return re.match(r"^.*[.,:;].*", text) is not None


def fits_in_line(draw, font, text):
    return draw.textlength(text=text, font=font) < MAX_LINE_WIDTH


def break_text(draw, font, text):
    parts = text.split(' ')

    lines = []

    line = ""
    for part in parts:
        if part == "<<special_token>>":
            lines.append(line)
            lines.append("na")
            line = ""
        # If there is a punctiation and the word fits in current line, add it to line and end line after punctuation
        elif has_punctuation(part) and fits_in_line(draw, font, " ".join([line, part])):
            line = " ".join([line, part])
            lines.append(line)
            line = ""
        # If word does not fit in current line, end current line and start a new one beginning with current word
        elif not fits_in_line(draw, font, " ".join([line, part])):
            lines.append(line)
            line = part
        # Otherwise, add the current word to the line and continue
        else:
            line = " ".join([line, part])

    lines.append(line)

    return "\n".join(lines)


def draw_reference_lines(draw):
    draw.line(((0, 880), (1080, 880)), "red", width=3)
    draw.line(((0, 1380), (1080, 1380)), "red", width=3)
    draw.line(((0, 1544), (1080, 1544)), "red", width=3)
    draw.rectangle([(40, 880), (1040, 1380)], outline="red", width=3)


def open_image(image):
    image_path = ""

    if image == "random":
        image_path = IMAGES[random.randint(0, len(IMAGES) - 1)]
    else:
        image_path = image + ".png"

    return Image.open(image_path)


def job_to_image(job):
    args = parse_args()

    img = open_image(args.background_image)
    dl = ImageDraw.Draw(img)

    job_opening = job.get("fields").get("Vaga")
    job_company = job.get("fields").get("Empresa")

    job_description = f"{job_opening} <<special_token>> {job_company}"
    text = break_text(dl, bariol, job_description)

    link = str(job.get("fields").get("Bitly")).replace("https://", "").replace("http://", "")

    dl.multiline_text((X_50_PERCENT, Y_MIDDLE_OF_TEXT_AREA), text=text,
                      font=bariol, fill=(255, 255, 255), align="center", anchor="mm")
    dl.text((X_50_PERCENT, Y_MIDDLE_OF_LINK_AREA), text=link, font=bariol, fill=(255, 255, 255), align="center",
            anchor="mm")

    job_id = job.get("id")
    filename = f"{job_id}.png"

    file = os.path.join(args.output_directory, filename)

    img.show()
    img.save(file)