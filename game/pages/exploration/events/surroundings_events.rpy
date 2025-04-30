
label surroundings_event_bird:
    "Você ouve um canto de pássaro melodioso."
    menu:
        "O que fazer?"
        "Observar o pássaro":
            "Você observa o pássaro por um tempo, apreciando seu canto."
            $ player.change_needs(sanity=+1)
        "Ignorar":
            "Você ignora o pássaro e continua caminhando."
    jump surroundings_return # Common return point

label surroundings_event_rabbit:
    "Um coelho pula na sua frente!"
    menu:
        "O que fazer?"
        "Tentar pegar o coelho":
            "Você tenta pegar o coelho, mas ele é muito rápido! Ele foge."

        "Observar o coelho":
            "Você observa o coelho se afastar."
            $ player.change_needs(sanity=+0.5)
    jump surroundings_return

label surroundings_event_squirrel:
    "Você vê um esquilo enterrando algo."
    menu:
        "O que fazer?"
        "Aproximar-se":
            "Você se aproxima, mas o esquilo foge, deixando para trás... uma noz!."
            $ player.add_item("Nut", 1)
        "Ignorar":
            "Você ignora o esquilo."
    jump surroundings_return

label surroundings_event_deer:
    "De repente, você se depara com um veado majestoso! Ele olha para você por um momento..."  # ...
    menu:
        "O que fazer?"
        "Admirar o veado":
            "Você admira o veado. Sua beleza acalma seus nervos."
            $ player.change_needs(sanity=+2)
        "Tentar se aproximar":
            "Você tenta se aproximar, mas o veado se assusta e foge para a floresta."
    jump surroundings_return

label surroundings_event_fallen_tree:
    "Enquanto você caminha aos seus arredores"
    "Você avista um tronco caído no chão"
    menu:
        "Como você irá agir?"
        "Aproximar-se":
            "Você se aproxima do tronco caído"
            "Ao chegar mais próximo você percebe que o mesmo está em estágios iniciais de decomposição"
            "É possível ver cogumelos vermelhos e marrons nesse tronco"
            menu:
                "O que fazer a seguir?"
                "Pegar os cogumelos marrons (+3 Cogumelos Marrons)":
                    $ player.add_item('Brown Mushroom', 3)
                    $ player.change_needs(sanity=-0.5)
                
                "Pegar os cogumelos vermelhos (+2 Cogumelos Vermelhos)":
                    $ player.add_item('Red Mushroom', 2)
                    $ player.change_needs(sanity=-0.5)
                
                "Pegar todos os cogumelos (+3 Cogumelos Marrons, +2 Cogumelos Vermelhos)":
                    $ player.add_item('Brown Mushroom', 3)
                    $ player.add_item('Red Mushroom', 2)
                    $ player.change_needs(sanity=-1)
                
                "Não pegar nada e afastar-se":
                    "Você decide não arriscar e se afasta do tronco"
                
        "Afastar-se":
            "Você se afasta do tronco tentando evitar possíveis problemas"

    jump surroundings_return

label surroundings_event_river:
    "Você encontra um rio de águas cristalinas."
    menu:
        "O que fazer?"
        "Beber água":
            $ player.change_needs(thirst=+100)
            "Você bebe a água fresca do rio."
            if random.random() < 0.2:
                $ player.change_needs(sanity=-10)
                "A água não estava tão limpa quanto parecia. Você se sente um pouco mal."

        "Lavar o rosto":
            "Você lava o rosto na água fria, sentindo-se revigorado."

        "Continuar explorando":
            "Você decide continuar explorando a área."

    jump surroundings_return

label surroundings_event_cave:
    "Você encontra a entrada de uma caverna."
    menu:
        "O que fazer?"
        "Entrar na caverna":
            call surroundings_cave_event_exploration
            
        "Ignorar a caverna":
            "Você não se sente à vontade para entrar na caverna agora e continua explorando."

    jump surroundings_return

label surroundings_event_bird_nest:
    "Você encontra um ninho de pássaro com ovos dentro."
    menu:
        "O que fazer?"
        "Pegar os ovos": # Consider adding the eggs to inventory?
            $ player.change_needs(sanity=-1)
            $ player.add_item("Eggs", 3)
            "Você pega os ovos, mas sente uma pontada de culpa por perturbar a natureza."

        "Observar o ninho":
            "Você observa o ninho com cuidado, sem tocar nos ovos."  # Positive effect
            $ player.change_needs(sanity=+1)

        "Deixar o ninho em paz":
            "Você decide deixar o ninho em paz e continua explorando."  # No effect

    jump surroundings_return

label surroundings_event_wildflowers:
    "Você encontra um campo de flores silvestres. O perfume é maravilhoso!"
    menu:
        "O que fazer?"
        "Colher algumas flores":
            $ player.add_item("Wildflowers", 5) # Could be a quantity or a single item
            "Você colhe algumas flores, elas trazem uma sensação de paz e alegria."

        "Apreciar a vista":
            "Você se senta por um momento e aprecia a beleza das flores."
            $ player.change_needs(sanity=+1) # Positive Effect

        "Ignorar as flores":
            "Você não é muito fã de flores e segue adiante."

    jump surroundings_return

label surroundings_event_loose_stones:
    "Você caminha por uma área com muitas pedras soltas."
    if random.random() < 0.3: # 30% chance of tripping
        "Você tropeça e cai!" # Negative event
        $ player.change_hp(-10)
        $ player.change_needs(sanity=-2)
    else:
        "Você caminha com cuidado, evitando as pedras."
    jump surroundings_return # Return even if nothing happened

# Ponto de retorno para todos os eventos aleatórios das redondezas
label surroundings_return:
    if player.needs['sleep'] == 0:
        call camp_outside_faint
    menu:
        "Você terminou a exploração na região atual"
        "Retornar ao Acampamento":
            "Você retorna ao acampamento"
            return

        "Continuar Explorando":
            $ world_state.advance_time(minutes=30)
            $ player.change_needs(*action_costs_player.return_action_cost("surroundings_events_from_exploration"))
            $ random_event = random.choice(world_situation.surrounding_events)
            $ renpy.jump(random_event)
