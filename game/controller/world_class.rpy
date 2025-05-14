# STATUS ATUAL DO MUNDO DO JOGO
python early:
    class World:
        def __init__(self):
            self.stats = {
                "Bear Friend": False
            }

            self.surrounding_events = [
                "surroundings_event_lake",
                "surroundings_event_roots",
                "surroundings_event_bugs",
                "surroundings_event_moss",
                "surroundings_event_nut",
                "surroundings_event_egg",
                "surroundings_event_fruits"
            ]

            self.surrounding_events_day = [
                "surroundings_event_day_branch_breaking",
                "surroundings_event_day_complete_silence",
                "surroundings_event_day_goodbird",
                "surroundings_event_day_butterfly"
            ]

            self.surroundings_cave_events = [
                "surroundings_cave_event_exploration_empty_cave",
                "surroundings_cave_event_exploration_bear_cave"
            ]

            self.distant_events = [
                "distant_event_far_away_stranger"
            ]

        def remove_event(self, event_type, event_name):
            if event_type == "surrounding_events":
                self.surrounding_events.remove(event_name)
            if event_type == "distant_events":
                self.distant_events.remove(event_name)

            if event_type == "surroundings_cave_events":
                self.surroundings_cave_events.remove(event_name)


        def add_event(self, event_type, event_name):
            if event_type == "surrounding_events":
                self.surrounding_events.add(event_name)
            if event_type == "distant_events":
                self.distant_events.add(event_name)

            if event_type == "surroundings_cave_events":
                self.surroundings_cave_events.add(event_name)
                