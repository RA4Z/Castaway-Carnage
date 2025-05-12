label surroundings_event_day_mushroom:
    "Seus olhos são atraídos para um ponto de cor vibrante rompendo a monotonia verde e marrom do chão da floresta."
    "É um cogumelo, diferente de todos que você já viu. Seu chapéu tem um tom de roxo profundo, quase luminoso, com manchas irregulares de um amarelo doentio que parecem... pulsar levemente sob a luz filtrada."
    player.name "Que cores... É lindo, de uma forma perturbadora. Mas parece gritar 'perigo'. Ou... talvez seja especial?"
    "Ele cresce solitário, emanando um odor adocicado, quase enjoativo, que se mistura ao cheiro de terra úmida. Não há outros cogumelos parecidos por perto."
    "Uma parte de você sente uma forte curiosidade misturada com apreensão. Seria comestível? Teria algum efeito estranho?"
    player.name "Arriscar? A fome não está tão desesperadora ainda... mas se for algo bom? Ou algo... alucinógeno? Pode ser útil? Ou fatal?"
    menu:
        "O que fazer?"
        "Pegar Cogumelo":
            $ player.add_item("Suspect Mushroom", 1)
            "Você pondera por um momento antes de decidir colher cuidadosamente o cogumelo de aparência bizarra, sua haste liberando um líquido leitoso e espesso."

        "Ignorar":
            "Você deixa o medo tomar conta e ignora a existência do cogumelo"
            
    jump surroundings_return


label surroundings_event_day_rotten_fruits:
    "Você avista outro arbusto com frutas, semelhante aos que já encontrou antes, mas algo está diferente."
    "As frutas neste arbusto têm uma cor mais pálida, quase translúcida, como se a cor tivesse sido drenada delas. A pele parece fina e tem uma textura estranhamente oleosa ao toque."
    player.name "São parecidas com as outras... mas ao mesmo tempo, tão diferentes. Estão doentes? Ou são apenas... outra coisa?"
    "Elas não têm o mesmo aroma adocicado das frutas comuns, emitindo um cheiro fraco, quase metálico."
    player.name "Comida é comida... certo? Mas meu instinto está gritando que há algo errado aqui."
    menu:
        "O que fazer?"
        "Pegar Cogumelo":
            $ player.add_item("Rotten Fruit", random.randint(4, 6))
            "Hesitante, você colhe algumas. Elas parecem estranhamente pesadas e frias em sua mão."

        "Ignorar":
            "Com nojo, você ignora essas frutas"
            
    jump surroundings_return

label surroundings_event_day_branch_breaking:
    "Um galho estala alto, muito perto, logo atrás de você. Você se vira num sobressalto, o coração disparado."
    "Não há nada ali. Nada que você possa ver. Apenas as árvores imóveis e o silêncio que se segue ao som."
    player.name "O vento? Um animal pequeno? Ou...?"
    "A incerteza deixa um gosto amargo na boca."
    "A tensão drena um pouco da sua compostura."
    