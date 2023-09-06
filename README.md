# Reordering Experiment

Working on a web service backend, I need items which can be arbitrarily
drag-and-drop reordered by the user. The obvious way to implement this
without having to change all the other rows is to have an `order` column
which gets set to the average of its value for the two rows which it's being
inserted between.

However, it's easy to imagine a pathological case where user behavior could
exhaust available precision (e.g. "braiding" three different items, or just
repeatedly toggling between the orders ABC and ACB).

So I'm interested in the question of how quickly the necessary precision
expands under _random_ shuffling behavior, which I'm guessing is a
reasonable approximation to actual user behavior given that the items will
originally be in an effectively random order and the users will want to
reorder them in some meaningful way. This test script runs Monte Carlo
experiments to try to figure that out.
