init python:
    # --- Constants for UI elements ---
    STATS_SIZE = 64
    BACKPACK_SIZE = STATS_SIZE * 2
    INVENTORY_WIDTH = 800
    INVENTORY_HEIGHT = 600
    UI_PADDING = 10
    INVENTORY_VPADDING = 40 # Top/Bottom padding inside inventory
    INVENTORY_HPADDING = 30 # Left/Right padding inside inventory

    # --- Dynamic Image Definitions ---
    # Define status icons using a loop to avoid repetition
    status_needs = ["sleep", "hunger", "thirst", "sanity"]
    for need_name in status_needs:
        # Normal state icon
        renpy.image(f"status_frame_{need_name}", im.Scale(f"gui/player_stats/{need_name}.png", width=STATS_SIZE, height=STATS_SIZE))
        # Dark/Empty state icon
        renpy.image(f"status_frame_dark_{need_name}", im.Scale(f"gui/player_stats/dark_{need_name}.png", width=STATS_SIZE, height=STATS_SIZE))

    # Define backpack icon separately as it has a different size
    renpy.image("backpack_icon", im.Scale("gui/player_stats/backpack.png", width=BACKPACK_SIZE, height=BACKPACK_SIZE))

# --- Player Stats Display Screen ---
screen player_stats_display():
    tag game_ui
    zorder 10 # Ensure it's above basic layers if needed
    
    fixed:
        # --- Top Left Cluster (Time + Stats) ---
        hbox:
            xalign 0.0
            yalign 0.0
            xoffset UI_PADDING
            yoffset UI_PADDING
            spacing 20 # Space between clock and status bars

            # --- Digital Clock Frame ---
            frame:
                background None # No visual frame background
                padding (10, 5) # Internal padding
                vbox:
                    xalign 0.5
                    spacing 2
                    hbox: # Date and Day
                        xalign 0.5
                        spacing 15
                        text "[world_state.current_time.strftime('%Y/%m/%d')]" style "digital_clock_top"
                        text "[world_state.current_time.strftime('%a').upper()]" style "digital_clock_top"
                    # Time
                    text "[world_state.current_time.strftime('%H:%M:%S')]" style "digital_clock_time" xalign 0.5

            # --- Status Bars ---
            hbox:
                spacing 10 # Space between status icons
                # Loop through needs defined in init python
                for need_name in status_needs:
                    button:
                        xysize (STATS_SIZE, STATS_SIZE)
                        action NullAction() # Substitua pela sua ação
                        tooltip str(player.needs[need_name])
                        style "empty"
                        bar:
                            value player.needs[need_name] # Assumes player.needs dictionary exists
                            range 100
                            xysize (STATS_SIZE, STATS_SIZE)
                            left_bar f"status_frame_{need_name}"      # Use dynamic image name
                            right_bar f"status_frame_dark_{need_name}" # Use dynamic image name
                            thumb None
                            bar_invert False # Bar fills from left to right

        # --- Top Right (Backpack Icon) ---
        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -UI_PADDING # Use negative offset with xalign 1.0 for right padding
            yoffset UI_PADDING
            idle "backpack_icon"    # Use defined image name
            hover "backpack_icon"   # Same for hover (adjust if you have a hover version)
            tooltip "Inventário"
            action Show("inventory_popup")

    $ tooltip = GetTooltip()
    if tooltip:

        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                background None
                xalign 0.5
                text tooltip


# --- Inventory Popup Screen ---
screen inventory_popup():
    on "show" action Play("sound", "audio/sfx/ziper.mp3")
    modal True # Blocks interaction with underlying screens
    tag inventory
    zorder 100 # Ensure it's above the game UI

    frame:
        # --- Sizing and Positioning ---
        xalign 0.5 yalign 0.5
        # Force a fixed size using minimum and maximum
        minimum (INVENTORY_WIDTH, INVENTORY_HEIGHT)
        maximum (INVENTORY_WIDTH, INVENTORY_HEIGHT)

        # Internal padding
        padding (INVENTORY_HPADDING, INVENTORY_VPADDING, INVENTORY_HPADDING, INVENTORY_VPADDING - 10) # Adjust bottom padding if needed

        # --- Close Button ---
        textbutton "X" action Hide("inventory_popup"):
            style "close_button_style" # Make sure this style is defined
            xalign 1.0 yalign 0.0
            xoffset -15 yoffset 15 # Position relative to top-right corner of frame padding

        # --- Main Content ---
        vbox:
            xalign 0.5 # Center content horizontally within the frame
            spacing 15

            text "Inventário" size 24 xalign 0.5 # Title

            # Divider (optional visual separator)
            null height 15 # Space before divider
            frame:
                background "#444" # Example color
                xfill True
                ysize 2
            null height 5 # Space after divider

            # --- Item List Area ---
            if not player.inventory:
                # Display message if inventory is empty
                # Use a fixed height container or just text to maintain layout
                frame:
                    background "#00000040" # Subtle background for empty state
                    xfill True
                    yfill True # Let it fill the space allocated by the vbox
                    text "O inventário está vazio." xalign 0.5 yalign 0.5 size 20
            else:
                # Scrollable Viewport for items
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    side_yfill True # Let the viewport fill the available vertical space in the vbox

                    vbox:
                        xalign 0.5 # Center items if they don't fill width
                        spacing 8

                        # Loop through items in player's inventory (assumes player.inventory is a list of dicts like {'id': 'apple', 'quantity': 1})
                        for item_data in player.inventory:
                            $ item_id = item_data['id']
                            # Look up the item's display name from the main item list
                            # Fallback to item_id if not found
                            $ item_name = next((i['name'] for i in inventory_items if i['id'] == item_id), item_id.capitalize())
                            # Potentially add quantity: $ item_display = f"{item_name} (x{item_data.get('quantity', 1)})"

                            textbutton item_name: # Use item_display if you add quantity
                                action NullAction() # Define item interaction later (e.g., Show item details)
                                style "inventory_item_button" # Make sure this style is defined
                                xfill True # Make button fill viewport width
                                