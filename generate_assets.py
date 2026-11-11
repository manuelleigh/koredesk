import os
from PIL import Image, ImageDraw, ImageFont

def get_base_emblem():
    if os.path.exists("kore_pe.png"):
        emblem = Image.open("kore_pe.png").convert("RGBA")
        print("Using transparent kore_pe.png (514x514)")
        return emblem
    
    if os.path.exists("LogoKoreFondoBlanco.jpg"):
        jpg = Image.open("LogoKoreFondoBlanco.jpg").convert("RGB")
        print("Processing LogoKoreFondoBlanco.jpg and removing white background...")
        rgba = Image.new("RGBA", jpg.size)
        data = jpg.getdata()
        new_data = []
        for item in data:
            # If near white, make transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append((item[0], item[1], item[2], 255))
        rgba.putdata(new_data)
        bbox = rgba.getbbox()
        if bbox:
            rgba = rgba.crop(bbox)
        # Pad to square
        max_dim = max(rgba.size)
        square = Image.new("RGBA", (max_dim, max_dim), (0, 0, 0, 0))
        offset = ((max_dim - rgba.size[0]) // 2, (max_dim - rgba.size[1]) // 2)
        square.paste(rgba, offset, rgba)
        return square

    raise FileNotFoundError("Neither kore_pe.png nor LogoKoreFondoBlanco.jpg found!")

def make_square_emblem(emblem, size):
    # Resize with aspect ratio preserved and centered on transparent canvas
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    emblem_copy = emblem.copy()
    emblem_copy.thumbnail((size, size), Image.LANCZOS)
    offset = ((size - emblem_copy.size[0]) // 2, (size - emblem_copy.size[1]) // 2)
    img.paste(emblem_copy, offset, emblem_copy)
    return img

def make_square_rounded_icon(emblem, size):
    # Desktop and app icon: rounded white squircle background with centered emblem
    s4 = size * 4
    mask = Image.new("L", (s4, s4), 0)
    draw = ImageDraw.Draw(mask)
    radius = int(s4 * 0.175)
    draw.rounded_rectangle((0, 0, s4 - 1, s4 - 1), radius=radius, fill=255)
    mask = mask.resize((size, size), Image.LANCZOS)

    bg = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(bg, (0, 0), mask)

    emblem_sz = int(size * 0.72)
    emblem_copy = emblem.copy()
    emblem_copy.thumbnail((emblem_sz, emblem_sz), Image.LANCZOS)
    offset = ((size - emblem_copy.size[0]) // 2, (size - emblem_copy.size[1]) // 2)
    result.paste(emblem_copy, offset, emblem_copy)
    return result

def create_logo_banner(emblem, is_dark=False):
    # Scale 2x for retina / hi-dpi (displayed at max 220x60 in UI)
    scale = 2
    w, h = 230 * scale, 60 * scale
    banner = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    
    emblem_size = int(48 * scale)
    emblem_resized = emblem.resize((emblem_size, emblem_size), Image.LANCZOS)
    
    emblem_x = int(6 * scale)
    emblem_y = (h - emblem_size) // 2
    banner.paste(emblem_resized, (emblem_x, emblem_y), emblem_resized)
    
    draw = ImageDraw.Draw(banner)
    font_path = "C:\\Windows\\Fonts\\segoeuib.ttf"
    if not os.path.exists(font_path):
        font_path = "C:\\Windows\\Fonts\\arialbd.ttf"
        
    font = ImageFont.truetype(font_path, int(29 * scale))
    
    text_x = emblem_x + emblem_size + int(10 * scale)
    text_y = (h - int(34 * scale)) // 2
    
    kore_color = (255, 255, 255, 255) if is_dark else (11, 58, 102, 255) # White or Navy #0B3A66
    desk_color = (14, 165, 233, 255) # Sky Blue #0EA5E9
    
    draw.text((text_x, text_y), "Kore", font=font, fill=kore_color)
    bbox_kore = draw.textbbox((text_x, text_y), "Kore", font=font)
    text_desk_x = bbox_kore[2]
    draw.text((text_desk_x, text_y), "Desk", font=font, fill=desk_color)
    
    return banner

def main():
    print("--- Generando assets gráficos de KoreDesk ---")
    emblem = get_base_emblem()
    
    # 1. Flutter app assets
    os.makedirs("flutter/assets", exist_ok=True)
    icon_512 = make_square_rounded_icon(emblem, 512)
    icon_512.save("flutter/assets/icon.png", "PNG")
    print("Guardado: flutter/assets/icon.png (512x512 con fondo blanco redondeado)")
    
    logo_light = create_logo_banner(emblem, is_dark=False)
    logo_light.save("flutter/assets/logo.png", "PNG")
    logo_light.save("flutter/assets/logo_light.png", "PNG")
    print("Guardado: flutter/assets/logo.png y logo_light.png (modo claro)")
    
    logo_dark = create_logo_banner(emblem, is_dark=True)
    logo_dark.save("flutter/assets/logo_dark.png", "PNG")
    print("Guardado: flutter/assets/logo_dark.png (modo oscuro)")
    
    # 2. Windows Executable Icon (flutter/windows/runner/resources/app_icon.ico)
    ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    ico_imgs = [make_square_rounded_icon(emblem, s[0]) for s in ico_sizes]
    
    os.makedirs("flutter/windows/runner/resources", exist_ok=True)
    app_ico_path = "flutter/windows/runner/resources/app_icon.ico"
    ico_imgs[-1].save(app_ico_path, format="ICO", sizes=ico_sizes)
    print(f"Guardado: {app_ico_path} con tamaños {ico_sizes}")
    
    # 3. Rust core assets (res/)
    os.makedirs("res", exist_ok=True)
    res_ico_path = "res/icon.ico"
    ico_imgs[-1].save(res_ico_path, format="ICO", sizes=ico_sizes)
    print(f"Guardado: {res_ico_path}")
    
    tray_sizes = [(16, 16), (32, 32)]
    tray_imgs = [make_square_rounded_icon(emblem, s[0]) for s in tray_sizes]
    tray_ico_path = "res/tray-icon.ico"
    tray_imgs[-1].save(tray_ico_path, format="ICO", sizes=tray_sizes)
    print(f"Guardado: {tray_ico_path}")
    
    icon_512.save("res/icon.png", "PNG")
    icon_512.save("res/mac-icon.png", "PNG")
    make_square_rounded_icon(emblem, 32).save("res/32x32.png", "PNG")
    make_square_rounded_icon(emblem, 64).save("res/64x64.png", "PNG")
    make_square_rounded_icon(emblem, 128).save("res/128x128.png", "PNG")
    make_square_rounded_icon(emblem, 256).save("res/128x128@2x.png", "PNG")
    print("Guardados: res/ (32x32, 64x64, 128x128, 128x128@2x, icon.png, mac-icon.png)")

    # 4. Android App Icons (flutter/android/app/src/main/res/mipmap-*)
    android_res_base = "flutter/android/app/src/main/res"
    densities = {
        "mipmap-mdpi": {"launcher": 48, "fg": 108, "stat": 24},
        "mipmap-hdpi": {"launcher": 72, "fg": 162, "stat": 36},
        "mipmap-xhdpi": {"launcher": 96, "fg": 216, "stat": 48},
        "mipmap-xxhdpi": {"launcher": 144, "fg": 324, "stat": 72},
        "mipmap-xxxhdpi": {"launcher": 192, "fg": 432, "stat": 96},
    }

    for folder, dims in densities.items():
        folder_path = os.path.join(android_res_base, folder)
        os.makedirs(folder_path, exist_ok=True)
        launcher_sz = dims["launcher"]
        fg_sz = dims["fg"]
        stat_sz = dims["stat"]

        # ic_launcher_foreground.png (adaptive icon safe zone: ~65% centered on transparent)
        fg_img = Image.new("RGBA", (fg_sz, fg_sz), (0, 0, 0, 0))
        emblem_fg_sz = int(fg_sz * 0.66)
        emblem_fg = emblem.copy()
        emblem_fg.thumbnail((emblem_fg_sz, emblem_fg_sz), Image.LANCZOS)
        offset_fg = ((fg_sz - emblem_fg.size[0]) // 2, (fg_sz - emblem_fg.size[1]) // 2)
        fg_img.paste(emblem_fg, offset_fg, emblem_fg)
        fg_img.save(os.path.join(folder_path, "ic_launcher_foreground.png"), "PNG")

        # ic_launcher.png (rounded square white background with centered emblem)
        launcher_img = Image.new("RGBA", (launcher_sz, launcher_sz), (255, 255, 255, 255))
        emblem_l_sz = int(launcher_sz * 0.72)
        emblem_l = emblem.copy()
        emblem_l.thumbnail((emblem_l_sz, emblem_l_sz), Image.LANCZOS)
        offset_l = ((launcher_sz - emblem_l.size[0]) // 2, (launcher_sz - emblem_l.size[1]) // 2)
        launcher_img.paste(emblem_l, offset_l, emblem_l)
        launcher_img.save(os.path.join(folder_path, "ic_launcher.png"), "PNG")

        # ic_launcher_round.png (circular white background)
        round_mask = Image.new("L", (launcher_sz, launcher_sz), 0)
        draw_mask = ImageDraw.Draw(round_mask)
        draw_mask.ellipse((0, 0, launcher_sz - 1, launcher_sz - 1), fill=255)
        round_img = Image.new("RGBA", (launcher_sz, launcher_sz), (0, 0, 0, 0))
        round_white = Image.new("RGBA", (launcher_sz, launcher_sz), (255, 255, 255, 255))
        round_white.paste(emblem_l, offset_l, emblem_l)
        round_img.paste(round_white, (0, 0), round_mask)
        round_img.save(os.path.join(folder_path, "ic_launcher_round.png"), "PNG")

        # ic_stat_logo.png (notification emblem)
        stat_img = make_square_emblem(emblem, stat_sz)
        stat_img.save(os.path.join(folder_path, "ic_stat_logo.png"), "PNG")

        print(f"Guardado Android {folder}: ic_launcher ({launcher_sz}x{launcher_sz}), foreground ({fg_sz}x{fg_sz}), round, stat ({stat_sz}x{stat_sz})")

    print("\n¡Todos los iconos y logos de KoreDesk han sido generados exitosamente!")

if __name__ == "__main__":
    main()

