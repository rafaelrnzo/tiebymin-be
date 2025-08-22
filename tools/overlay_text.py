
import argparse
from app.ai_tools.overlay_text import overlay_text_on_image

def main():
    parser = argparse.ArgumentParser(description="Overlay text to image.")
    parser.add_argument('--filename', type=str, required=True, help='Image filename to process (wajib, dengan folder path)')
    parser.add_argument('--text', type=str, required=True, help='Text to overlay')
    parser.add_argument('--font_path', type=str, default="arial.ttf", help='Path to font file')
    parser.add_argument('--font_size', type=int, default=40, help='Font size')
    parser.add_argument('--with_bg', action='store_true', help='Add background to text')
    parser.add_argument('--align', type=str, default='center', choices=['left','center','right'], help='Text alignment per baris')
    parser.add_argument('--position', type=str, default='center', choices=['top_left','top_center','top_right','center_left','center','center_right','bottom_left','bottom_center','bottom_right'], help='Template posisi blok text (9 posisi)')
    args = parser.parse_args()
    output_path = overlay_text_on_image(
        image_path=args.filename,
        text=args.text,
        font_path=args.font_path,
        font_size=args.font_size,
        with_bg=args.with_bg,
        align=args.align,
        position=args.position
    )
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    main()
