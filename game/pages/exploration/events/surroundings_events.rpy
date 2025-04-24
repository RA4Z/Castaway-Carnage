
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
            $ player.add_item("Noz", 1)
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

label surroundings_return:  # Common return point for all random events
    "Você retorna ao acampamento."
    return