label exploration_surroundings:
    "Você começou a se preparar para explorar os arredores de seu acampamento"
    while True:
        menu:
            "O que fazer a seguir?"
            "Iniciar Exploração":
                $ world_state.advance_time(minutes=30)
                $ player.change_needs(*action_costs_player.return_action_cost("surroundings_events_from_camp"))
                $ random_event = random.choice(world_situation.surrounding_events)
                $ renpy.call(random_event)

            "Cancelar a Exploração":
                "Você desistiu da ideia de explorar e permaneceu no acampamento"
                return