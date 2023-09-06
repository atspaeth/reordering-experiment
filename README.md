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

# Results

Over 1000 runs of random reorderings of the items, the minimum number of
iterations to lose precision for a double-valued column is about 2000,
suggesting there's little reason to worry about this in practice. Even if
the colummn is only single-precision floating point, the minimum time to
failure over 1000 iterations is in the hundreds. 

Also, I don't have data to support this, but it seems to happen even later
for smaller numbers of items. Since 1000 is unrealistically many for our use
case (usually there will be more like 10), I expect this issue to crop up
extremely rarely, and I'm content to implement the naive version of this,
label it a "quirk" in the bug tracker, and move on.
