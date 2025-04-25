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
    # Use a fixed layout to position elements independently in corners
    fixed:

        # --- Left Aligned Block (Clock and Status) ---
        hbox:
            # Position this hbox at the top-left corner
            xalign 0.0
            yalign 0.0
            # Add some padding from the screen edges
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

                # Ensure stats_size is defined, e.g., default stats_size = 40
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
            # Add some padding from the screen edges
            xoffset -10 # Adjust padding from right edge (negative moves left)
            yoffset 10  # Adjust padding from top edge

            # --- Define your backpack images ---
            # Replace with your actual image file paths
            idle "backpack"    # Image when not hovered/clicked
            hover "backpack"   # Image when hovered (optional)
            # focus_mask True # Uncomment if your image has transparency and you want precise hovering

            # --- Action to perform when clicked ---
            # This will show the screen named "inventory_popup"
            action Show("inventory_popup")


screen inventory_popup():
    on "show" action Play("sound", "audio/ziper.mp3")
    # 'modal True' impede que o jogador clique em elementos atrás do popup
    modal True

    # 'tag' ajuda a garantir que apenas uma instância desta tela seja mostrada
    tag inventory

    # Use um 'frame' como container para o popup.
    # 'frame' geralmente tem um fundo e bordas definidos no seu tema (gui.rpy)
    frame:
        # Centraliza o frame na tela
        xalign 0.5
        yalign 0.5

        # Define um tamanho mínimo (opcional, ajuste conforme necessário)
        xminimum 300
        yminimum 200

        # Adiciona preenchimento interno (espaço entre a borda do frame e o conteúdo)
        xpadding 30
        ypadding 20

        # Use um 'vbox' para empilhar os elementos verticalmente
        vbox:
            # Espaçamento entre os elementos na vbox
            spacing 10
            # Alinha o conteúdo da vbox ao centro horizontalmente dentro do frame
            xalign 0.5

            # Título do Popup
            text "Inventário" size 22 xalign 0.5 # Ajuste o tamanho e alinhamento

            # Adiciona uma linha divisória (opcional)
            null height 5 # Pequeno espaço
            add "gui/line.png" xalign 0.5 # Use uma imagem de linha ou remova
            null height 5 # Pequeno espaço

            # --- Lista de Itens ---
            # Verifica se o inventário está vazio
            if not player.inventory:
                text "O inventário está vazio." align (0.5, 0.5) # Centraliza o texto
            else:
                # Cria uma área rolável se a lista for muito grande
                viewport:
                    # Mostra a barra de rolagem vertical apenas se necessário
                    scrollbars "vertical"
                    # Permite rolar com a roda do mouse
                    mousewheel True
                    # Define uma altura máxima para a área rolável
                    # O conteúdo dentro dela poderá ser maior
                    ymaximum 300 # Ajuste a altura máxima conforme necessário

                    # Vbox interna para listar os itens dentro da área rolável
                    vbox:
                        spacing 5 # Espaçamento menor entre os itens da lista
                        # Itera sobre cada 'item' na lista 'player.inventory'
                        for item_name in player.inventory:
                            # Mostra o nome de cada item como texto
                            text item_name

            # --- Fim da Lista de Itens ---

            # Espaço antes do botão de fechar (opcional)
            null height 15

            # Botão para fechar o popup
            textbutton "Fechar" action Hide("inventory_popup") xalign 0.5
