init python:
    import random

    random_surroundings_cave_events = [
        "surroudings_cave_event_exploration_empty_cave"
    ]

label surroudings_cave_event_exploration:
    "Você adentra a caverna"
    $ random_event = random.choice(random_surroundings_cave_events)
    $ renpy.call(random_event)

    return

label surroudings_cave_event_exploration_empty_cave:
    "Mas não consegue avistar nada de interessante"
    "É apenas um espaço vazio sem nada para se coletar ou fazer"
    return