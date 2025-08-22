import os
from typing import Tuple, Optional
from PIL import Image, ImageDraw, ImageFont

def overlay_text_on_image(
    image_path: str,
    text: str,
    font_path: str = "arial.ttf",
    font_size: int = 40,
    text_color: Tuple[int, int, int] = (0, 0, 0),
    bg_color: Tuple[int, int, int, int] = (255, 255, 255, 230),
    with_bg: bool = False,
    align: str = "center",
    position: str = "center",
    output_path: Optional[str] = None
) -> str:
    """
    Overlay text on a single image and save the result.
    Returns the path to the saved image.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")
    folder_path = os.path.dirname(image_path)
    fname = os.path.basename(image_path)
    img = Image.open(image_path).convert("RGBA")
    txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_layer)
    # Font loading logic
    try:
        if os.path.isabs(font_path) and os.path.exists(font_path):
            font = ImageFont.truetype(font_path, font_size)
        elif os.path.exists(os.path.join("C:/Windows/Fonts/", font_path)):
            font = ImageFont.truetype(os.path.join("C:/Windows/Fonts/", font_path), font_size)
        else:
            arial_path = "C:/Windows/Fonts/arial.ttf"
            try:
                font = ImageFont.truetype(arial_path, font_size)
            except Exception:
                font = ImageFont.load_default()
    except Exception:
        try:
            font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", font_size)
        except Exception:
            font = ImageFont.load_default()
    margin_x = int(font_size * 1.0)
    max_text_width = img.width - 2 * margin_x
    def wrap_text(text, font, max_width):
        words = text.split()
        lines = []
        current_line = ''
        for word in words:
            test_line = current_line + (' ' if current_line else '') + word
            bbox = draw.textbbox((0, 0), test_line, font=font)
            line_width = bbox[2] - bbox[0]
            if line_width <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        return lines
    lines = wrap_text(text, font, max_text_width)
    radius = int(font_size * 0.45)
    margin = int(font_size * 0.5)
    line_spacing = int(font_size * 1.13)
    line_heights = []
    line_bboxes = []
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        line_heights.append(bbox[3] - bbox[1])
        line_bboxes.append(bbox)
    total_text_height = sum(line_heights) + (len(lines) - 1) * line_spacing
    if position in ["top_left", "top_center", "top_right"]:
        y = margin + margin
    elif position in ["center_left", "center", "center_right"]:
        y = (img.height - total_text_height) // 2
    elif position in ["bottom_left", "bottom_center", "bottom_right"]:
        y = img.height - total_text_height - margin - margin
    else:
        y = (img.height - total_text_height) // 2
    y_line = y
    def get_x(line_width, img_width, margin, align, position):
        if position in ["top_left", "center_left", "bottom_left"]:
            return margin + margin
        elif position in ["top_right", "center_right", "bottom_right"]:
            return img_width - line_width - margin - margin
        else:
            if align == "left":
                return margin + margin
            elif align == "right":
                return img_width - line_width - margin - margin
            else:
                return (img_width - line_width) // 2
    for i, line in enumerate(lines):
        bbox = line_bboxes[i]
        line_width = bbox[2] - bbox[0]
        line_height = bbox[3] - bbox[1]
        x = get_x(line_width, img.width, margin, align, position)
        top_padding = int(margin * 0.8)
        bottom_padding = int(margin * 1.4)
        bg_y1 = y_line - top_padding
        bg_y2 = y_line + line_height + bottom_padding
        if with_bg:
            bg_box = [
                x - margin,
                bg_y1,
                x + line_width + margin,
                bg_y2
            ]
            draw.rounded_rectangle(bg_box, fill=bg_color, radius=radius)
        draw.text((x, y_line), line, font=font, fill=text_color)
        y_line += line_height + line_spacing
    combined = Image.alpha_composite(img, txt_layer)
    if not output_path:
        output_path = os.path.join(folder_path, f"overlay_{fname}")
    combined.convert("RGB").save(output_path)
    return output_path 