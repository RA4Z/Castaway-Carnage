init python:
    world_state = WorldState(8)
    world_situation = World()
    player = Player(name="Viajante")

label start:
    python:
        player_name = renpy.input("Qual é o seu nome?", default=player.name, length=20)
        player.name = player_name.strip() or player.name # Atualiza o nome no objeto, usa o anterior se vazio

    call camp_outside

    return
