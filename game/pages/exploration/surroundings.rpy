label exploration_surroundings:
    "Você começou a se preparar para explorar os arredores de seu acampamento"
    while True:
        if player.needs['sleep'] == 0:
            call camp_outside_faint
        menu:
            "O que fazer a seguir?"
            "Iniciar Exploração":
                $ world_state.advance_time(minutes=30)
                $ player.change_needs(hunger=-2, thirst=-4, sleep=-5)
                $ random_event = random.choice(world_situation.surrounding_events)
                $ renpy.call(random_event)

            "Cancelar a Exploração":
                "Você desistiu da ideia de explorar e permaneceu no acampamento"
                return