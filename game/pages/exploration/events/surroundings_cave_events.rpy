label surroundings_cave_event_exploration:
    "Você adentra a caverna"
    $ random_event = random.choice(world_situation.surroundings_cave_events)
    $ renpy.call(random_event)

    return

label surroundings_cave_event_exploration_empty_cave:
    "Mas não consegue avistar nada de interessante"
    "É apenas um espaço vazio sem nada para se coletar ou fazer"
    return

label surroundings_cave_event_exploration_bear_cave:
    "Caminhando dentro da caverna, você percebe uma presença grande no centro dela.  A escuridão dificulta a visão, mas você sente o cheiro de musgo úmido e... algo mais selvagem."
    "Seus olhos se ajustam lentamente à penumbra. Uma forma enorme se materializa: um urso. Ele dorme profundamente, sua respiração pesada ecoando pelas paredes da caverna."
    $ world_situation.remove_event('surroundings_cave_events', 'surroundings_cave_event_exploration_bear_cave')
    $ has_honey = player.has_item("Honey", 1)
    menu:
        "O que você faz?"
        "Tentar sair de fininho":
            if random.random() < 0.7:
                "Você pisa em um galho seco. O som quebra o silêncio da caverna. O urso se mexe, mas não acorda. Você aproveita a chance e sai da caverna o mais rápido que consegue, sem fazer barulho."
                jump surroundings_return

            else:
                "Você pisa em um galho seco. O som ecoa pela caverna, acordando o urso. Ele se levanta, rosnando. Você se prepara para o pior..."
                # CRIAR SISTEMA DE ATAQUE DE URSO

        "Atirar uma pedra no urso":
            $ player.change_needs(sanity=-10)
            "Você atira uma pedra no urso. Ele acorda com um rugido furioso e avança em sua direção!"
            # CRIAR SISTEMA DE ATAQUE DE URSO

        "Deixar o mel perto do urso e sair de fininho" if has_honey == True:
            $ world_situation.stats["Bear Friend"] = True
            $ player.remove_item("Honey", 1)
            "Você cuidadosamente deixa o pote de mel perto do urso e sai da caverna em silêncio. Talvez ele aprecie o presente quando acordar."
            jump surroundings_return
