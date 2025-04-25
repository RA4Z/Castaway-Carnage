init python:
    # Style for the digital clock text elements
    style.digital_clock_base = Style(style.default) # Inherit from default text
    style.digital_clock_base.font = "fonts/DIGITALDREAMFAT.ttf"  # <-- IMPORTANT: Replace with your font file!
    style.digital_clock_base.color = "#33FF33" # Bright green
    style.digital_clock_base.outlines = [(1, "#003300", 0, 0)] # Optional: Darker outline for definition
    # style.digital_clock_base.outlines = [(2, "#66FF6699", 0, 0), (1, "#000000", 0, 0)] # Optional: Glow + black outline
    style.digital_clock_base.xalign = 0.5 # Center text horizontally

    # Style for the smaller top line (Date and Day)
    style.digital_clock_top = Style(style.digital_clock_base)
    style.digital_clock_top.size = 10 # Adjust size as needed

    # Style for the larger bottom line (Time)
    style.digital_clock_time = Style(style.digital_clock_base)
    style.digital_clock_time.size = 28 # Adjust size as needed


style stats_text is text:
    size 20                       # Adjust font size
    color "#E0E0E0"                 # Light grey text color
    outlines [(1, "#222", 0, 0)]   # Darker, subtle outline
    text_align 0.5                # Center align multi-line text
    xalign 0.5
    yalign 0.5
