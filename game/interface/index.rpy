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

# Mantenha seu bloco init python com as definições de imagem e stats_size

screen player_stats_display():
    tag game_ui

    # Seu hbox principal (pode precisar ajustar o layout geral)
    hbox:
        xalign 0.0
        yalign 0.0
        spacing 20 # Espaço entre o relógio e os status, ajuste conforme necessário

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
        hbox: # Container para os ícones de status
            spacing 10 # Espaço entre os ícones de status

            for need in ["hunger", "thirst", "sleep", "sanity"]:
                # Substitua o frame e text por um bar configurado
                bar:
                    value player.needs[need]  # O valor atual da necessidade
                    range 100                 # O valor máximo (0-100)
                    xysize (stats_size, stats_size) # Define o tamanho exato da barra/ícone

                    # --- Definição das imagens da barra ---
                    # 'left_bar' é a parte "cheia" (valor atual) -> imagem clara
                    left_bar f"status_frame_{need}"

                    # 'right_bar' é a parte "vazia" (o que falta para 100) -> imagem escura
                    right_bar f"status_frame_dark_{need}"

                    # A barra preenche da esquerda para a direita por padrão.
                    # Quando value=100, mostra 100% left_bar (clara).
                    # Quando value=50, mostra 50% left_bar (clara) à esquerda e 50% right_bar (escura) à direita.
                    # Quando value=0, mostra 100% right_bar (escura).
                    # Isso cria o efeito da imagem escura "cobrindo" da direita para a esquerda.

                    # Remove a "alça" padrão da barra
                    thumb None

                    # Garante que a barra não inverta o preenchimento
                    bar_invert False

                    # Opcional: Remove qualquer padding interno padrão da barra, se houver
                    # left_padding 0
                    # right_padding 0
                    # top_padding 0
                    # bottom_padding 0

