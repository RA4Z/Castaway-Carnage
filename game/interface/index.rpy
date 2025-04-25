init python:
    stats_size= 64

image status_frame_sleep = im.Scale("gui/player_stats/sleep.png", width=stats_size, height=stats_size)
image status_frame_hunger = im.Scale("gui/player_stats/hunger.png", width=stats_size, height=stats_size)
image status_frame_thirst = im.Scale("gui/player_stats/thirst.png", width=stats_size, height=stats_size)
image status_frame_sanity = im.Scale("gui/player_stats/sanity.png", width=stats_size, height=stats_size)

image status_frame_dark_sleep = im.Scale("gui/player_stats/dark_sleep.png", width=stats_size, height=stats_size)
image status_frame_dark_hunger = im.Scale("gui/player_stats/dark_hunger.png", width=stats_size, height=stats_size)
image status_frame_dark_thirst = im.Scale("gui/player_stats/dark_thirst.png", width=stats_size, height=stats_size)
image status_frame_dark_sanity = im.Scale("gui/player_stats/dark_sanity.png", width=stats_size, height=stats_size)

image backpack = im.Scale("gui/player_stats/backpack.png", width=stats_size*2, height=stats_size*2)

screen player_stats_display():
    tag game_ui
    fixed:
        hbox:
            xalign 0.0
            yalign 0.0
            xoffset 10 # Adjust padding from left edge
            yoffset 10 # Adjust padding from top edge
            spacing 20 # Space between clock and status bars

            # --- Bloco de Tempo (Digital Style) ---
            frame:
                background None
                padding (10, 5)
                vbox:
                    xalign 0.5
                    spacing 2
                    hbox:
                        xalign 0.5
                        spacing 15
                        text "[world_state.current_time.strftime('%Y/%m/%d')]" style "digital_clock_top"
                        text "[world_state.current_time.strftime('%a').upper()]" style "digital_clock_top"
                    text "[world_state.current_time.strftime('%H:%M:%S')]" style "digital_clock_time" xalign 0.5

            # --- Bloco de Status (com efeito de sobreposição) ---
            hbox: # Container for the status icons
                spacing 10 # Space between status icons

                for need in ["hunger", "thirst", "sleep", "sanity"]:
                    bar:
                        value player.needs[need]  # Current need value
                        range 100                 # Max value (0-100)
                        xysize (stats_size, stats_size) # Define the exact size
                        left_bar f"status_frame_{need}" # Make sure these paths are correct
                        right_bar f"status_frame_dark_{need}" # Make sure these paths are correct
                        thumb None
                        bar_invert False

        # --- Right Aligned Block (Backpack Icon) ---
        imagebutton:
            # Position this button at the top-right corner
            xalign 1.0
            yalign 0.0
            xoffset -10 # Adjust padding from right edge (negative moves left)
            yoffset 10  # Adjust padding from top edge
            idle "backpack"    # Image when not hovered/clicked
            hover "backpack"   # Image when hovered (optional)
            action Show("inventory_popup")


screen inventory_popup():
    on "show" action Play("sound", "audio/sfx/ziper.mp3")
    modal True

    # 'tag' helps ensure only one instance of this screen is shown
    tag inventory

    # Use a 'frame' as container for the popup.
    frame:
        # Center the frame on the screen
        xalign 0.5
        yalign 0.5

        xminimum 1250
        # 5 * item_height + 4 * grid_spacing + 2 * frame_padding_y + title_height + spacing...
        # Example: 5*50 + 4*10 + 2*20 + 30 + 20 + 15 + button_height = 250+40+40+30+20+15+30 = 425
        yminimum 750

        # Add internal padding (space between the frame border and content)
        xpadding 30
        ypadding 20

        # Use a 'vbox' to stack title, grid, and close button vertically
        vbox:
            # Spacing between elements in the vbox
            spacing 10
            # Align the content of the vbox horizontally within the frame
            xalign 0.5

            # Popup Title
            text "Inventário" size 22 xalign 0.5 # Adjust size and alignment

            # Add a dividing line (optional)
            null height 5 # Small space
            add "gui/line.png" xalign 0.5 # Use a line image or remove
            null height 5 # Small space

            # --- Item Grid ---
            # Check if inventory is empty
            if not player.inventory:
                # Keep the frame size consistent even when empty
                frame style "empty_slot": # Use a styled frame or null for size
                    xysize (5 * 100 + 4 * 10, 5 * 50 + 4 * 10) # Calculate grid area size
                    # This assumes item size (100, 50) and grid spacing 10
                    text "O inventário está vazio." xalign 0.5 yalign 0.5 # Center text
            else:
                # Use a grid with 5 columns and 5 rows
                grid 5 5:
                    # Spacing between grid cells
                    spacing 10
                    # Align the grid itself within its allocated space (usually centered by vbox's xalign)
                    xalign 0.5
                    yalign 0.5

                    # Iterate through items in the player's inventory
                    for item in player.inventory:
                        # Add a button for each item. Apply the style.
                        # You might want NullAction() if items aren't clickable yet,
                        # or a specific action like UseItem(item_name)
                        $ item_id = item['id']
                        $ item_name = next((item['name'] for item in inventory_items if item['id'] == item_id), item_id)
                        textbutton item_name action NullAction() style "inventory_item_button"

                    # OPTIONAL: Fill remaining grid slots if less than 25 items
                    # This ensures the grid structure is visually consistent
                    $ items_shown = len(player.inventory)
                    $ slots_to_fill = 25 - items_shown
                    if slots_to_fill > 0:
                        for i in range(slots_to_fill):
                            # Add an empty, non-interactive frame or button
                            # Use the same size as item slots for alignment
                            frame style "inventory_item_button": # Use the same style for size
                                background None # Make it visually empty if needed
                                # Or use: button style "inventory_item_button": action NullAction() sensitive False

            # --- End of Item Grid ---
            null height 15 # Space before the close button
            textbutton "Fechar" action Hide("inventory_popup") xalign 0.5
            