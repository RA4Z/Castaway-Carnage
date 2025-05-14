python early:
    class Costs:
        def __init__(self):
            self.costs = {
                "long_rest": {"hunger": -12, "thirst": -22.5, "sleep": 45, "sanity": 2},
                "short_rest": {"hunger": -4, "thirst": -7.5, "sleep": 10, "sanity": 0},
                "physical_exercises_in_camp": {"hunger": -5, "thirst": -7, "sleep": -10, "sanity": 0},

                "surroundings_events_from_camp": {"hunger": -2, "thirst": -4, "sleep": -5, "sanity": 0},
                "distant_events_from_camp": {"hunger": -5, "thirst": -10, "sleep": -12, "sanity": 0},

                "surroundings_events_from_exploration": {"hunger": -1, "thirst": -2, "sleep": -2.5, "sanity": -1},

                "surroundings_event_day_branch_breaking": {"hunger": 0, "thirst": 0, "sleep": 0, "sanity": -5},
                "surroundings_event_day_complete_silence": {"hunger": 0, "thirst": 0, "sleep": 0, "sanity": -9},
                "surroundings_event_day_goodbird": {"hunger": 0, "thirst": 0, "sleep": 0, "sanity": 4},
                "surroundings_event_day_butterfly": {"hunger": 0, "thirst": 0, "sleep": 0, "sanity": 8}
            }

        def return_action_cost(self, event_name, extra_hunger=0, extra_thirst=0, extra_sleep=0, extra_sanity=0):
            daytime_consumption_multiplier = 1
            if world_state.daytime == 'Night':
                daytime_consumption_multiplier = 1.2

            hunger = (self.costs[event_name]["hunger"] + extra_hunger) * daytime_consumption_multiplier
            thirst = (self.costs[event_name]["thirst"] + extra_thirst) * daytime_consumption_multiplier
            sleep = (self.costs[event_name]["sleep"] + extra_sleep) * daytime_consumption_multiplier
            sanity = (self.costs[event_name]["sanity"] + extra_sanity) * daytime_consumption_multiplier

            return hunger, thirst, sleep, sanity
