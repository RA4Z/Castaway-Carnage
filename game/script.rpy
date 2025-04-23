# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

init python:
    player = Player(name="Viajante", hp=80, max_hp=100, gold=50)

# The game starts here.

label start:
    python:
        player_name = renpy.input("Qual é o seu nome?", default=player.name, length=20)
        player.name = player_name.strip() or player.name # Atualiza o nome no objeto, usa o anterior se vazio

    call camp_outside

    return
