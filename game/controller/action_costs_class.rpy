python early:
    class Costs:
        def __init__(self):
            self.costs = {
                "surroundings_events_from_camp": {"hunger": -2, "thirst": -4, "sleep": -5, "sanity": 0},
                "surroundings_events_from_exploration": {"hunger": -1, "thirst": -2, "sleep": -2.5, "sanity": -1}
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
