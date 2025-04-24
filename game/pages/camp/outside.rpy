label camp_outside:
    "[player.name], bem-vindo ao seu acampamento!"

    while True:
        menu:
            "Você está no lado de fora de seu acampamento."
            "Entrar no abrigo":
                jump camp_inside
            
            "Explorar os arredores":
                call exploration_surroundings

            "Explorar regiões distantes":
                call exploration_distant
            
            "Realizar Exercícios físicos":
                if player.needs['sleep'] > 30:
                    $ world_state.advance_time(minutes=30)
                    $ player.lvl_up_skills("strength", player.stats['strength'])
                    $ player.change_needs(hunger=-5, thirst=-7, sleep=-10)
                    "Você realizou exercícios físicos!"
                else:
                    "Você se sente cansado demais para se exercitar no momento"
