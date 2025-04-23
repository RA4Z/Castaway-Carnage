label camp_outside:
    "[player.name], bem-vindo ao seu acampamento!"

    while True:
        menu:
            "Você está no lado de fora de seu acampamento."
            "Entrar no abrigo":
                jump camp_inside
            
            "Explorar os arredores":
                ""
            
            "Realizar Exercícios físicos":
                if player.needs['sleep'] > 30:
                    "Você realizou exercícios físicos!"
                    $ player.lvl_up_skills("strength", player.stats['strength'])
                    $ player.change_needs(hunger=-2, thirst=-3, sleep=-7)
                    $ remaining = player.experience_points['strength_next_level'] - player.experience_points['strength_xp']
                    "Pontos de experiência nessessários para o próximo nível de força: [remaining]"
                    "Nível de força atual: [player.stats['strength']]"
                else:
                    "Você se sente cansado demais para se exercitar no momento"