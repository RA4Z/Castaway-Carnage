﻿image image_game_over = "images/game_over.png"

init python:
    world_state = WorldState(8)
    world_items = World_Items()
    world_situation = World()
    action_costs_player = Costs()
    player = Player(name="Viajante")
    camp = Camp()

label start:
    # python:
        # player_name = renpy.input("Qual é o seu nome?", default=player.name, length=20)
        # player.name = player_name.strip() or player.name # Atualiza o nome no objeto, usa o anterior se vazio
    show screen player_stats_display
    $ world_state.advance_time()
    call camp_outside

    return

label gameover:
    hide screen player_stats_display
    stop music
    stop sound
    play sound "audio/sfx/game_over.mp3"
    $ show_only_image("image_game_over")
    "Fim de Jogo"
    return