image image_exercise_visual = "images/camp_exercises.png"
image image_camp_outside = "images/camp_outside.png"

label camp_outside:
    while True:
        $ show_only_image("image_camp_outside")
        menu:
            "Entrar no abrigo":
                jump camp_inside
            
            "Explorar os arredores":
                call exploration_surroundings

            "Explorar regiões distantes":
                call exploration_distant
            
            "Realizar Exercícios físicos":
                if player.needs['sleep'] > 30:
                    $ show_only_image("image_exercise_visual")
                    $ world_state.advance_time(minutes=30)
                    $ player.lvl_up_skills("strength", player.stats['strength'])
                    $ player.change_needs(*action_costs_player.return_action_cost("distant_events_from_camp"))
                    "Você realizou exercícios físicos!"
                else:
                    "Você se sente cansado demais para se exercitar no momento"
