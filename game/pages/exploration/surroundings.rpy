init python:
    import random

    random_events = [
        "surroundings_event_bird",
        "surroundings_event_rabbit",
        "surroundings_event_squirrel",
        "surroundings_event_deer",
        "surroundings_event_fallen_tree",
        "surroundings_event_river",
        "surroundings_event_cave_1",
        "surroundings_event_bird_nest",
        "surroundings_event_wildflowers",
        "surroundings_event_loose_stones"
    ]

label exploration_surroundings:
    "Você começou a se preparar para explorar os arredores de seu acampamento"
    while True:
        menu:
            "O que fazer a seguir?"
            "Iniciar Exploração":
                $ world_state.advance_time(minutes=30)
                $ player.change_needs(hunger=-2, thirst=-4, sleep=-5)
                $ random_event = random.choice(random_events)
                $ renpy.call(random_event)

            "Cancelar a Exploração":
                "Você desistiu da ideia de explorar e permaneceu no acampamento"
                return