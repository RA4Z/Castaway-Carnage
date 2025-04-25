init python:
    def show_only_image(image_tag_to_show):
        renpy.scene(layer='master')
        renpy.show(image_tag_to_show, layer='master')