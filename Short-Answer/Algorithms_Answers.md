#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) `O(n)` -- `a` is zero, and even if it weren't, it's constant, so the process is basically asking "How many times can n squared go into n cubed? You can express this mathematically as `n^3 / n^2`, which evaluates to `n`.


b) `O(nlog(n))` -- Because `j` keeps being doubled, it will take log time to reach its target, which is on average `n/2`, a constant factor of `n`. That is being done `n` times, so you gotta tack an `n` on there too.


c) `O(n)` -- The function will recur `n` times, performing a constant check and addition each step.

## Exercise II

My best understanding of the wording of the problem has `O(1)` implementation, because the answer is always zero. Drop the eggs from the smallest distance to minimize breaking -- this always works.

But that seems too simple!

Other factors to consider:
- Egg speed grows exponentially with `n` until air resistance starts leveling things off. Those numbers are unknown.
- We don't know the distribution of egg durability.
- We only know whether an egg breaks or not, not anything quantifiable about how close it was to surviving or breaking.

If we assume all eggs have equal durability and that the prompt wants the biggest `f` given a type of egg, the above means we can't do any better than a binary search, starting in the middle, then repeating the test in the upper or lower half depending on the outcome for the egg. That would be `O(log(n))` time.

If we knew air resistance was not a problem, we might do better to skew our notion of "middle" exponentially to account for the constant acceleration of gravity. I think an exponentially/logarithmically skewed binary search would still happen in log time, but I'd have to do a lot of math to be condifent.
