# STATUS ATUAL DO MUNDO DO JOGO
python early:
    class World:
        def __init__(self):
            self.stats = {
                "Bear Friend": False
            }

            self.surrounding_events = [
                "surroundings_event_bird",
                "surroundings_event_rabbit",
                "surroundings_event_squirrel",
                "surroundings_event_deer",
                "surroundings_event_fallen_tree",
                "surroundings_event_river",
                "surroundings_event_cave",
                "surroundings_event_bird_nest",
                "surroundings_event_wildflowers",
                "surroundings_event_loose_stones"
            ]

            self.surroundings_cave_events = [
                "surroundings_cave_event_exploration_empty_cave",
                "surroundings_cave_event_exploration_bear_cave"
            ]

        def remove_event(self, event_type, event_name):
            if event_type == "surrounding_events":
                self.surrounding_events.remove(event_name)

            if event_type == "surroundings_cave_events":
                self.surroundings_cave_events.remove(event_name)


        def add_event(self, event_type, event_name):
            if event_type == "surrounding_events":
                self.surrounding_events.add(event_name)

            if event_type == "surroundings_cave_events":
                self.surroundings_cave_events.add(event_name)
                