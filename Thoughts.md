#Thoughts
Here are some experience I found or realized during or after successfully generated or fail in doing so.

##Effect of some variables:
###In dimer system:
1. Maximum Population
    - Affects not only amplitude of the graph, but a suitable range will lead to a periodical graph.
    - Bigger value will let the plants[^1] grows carzy initially, and die out very fast.
    - Small value will not allow plants to recover in time, thus the population will tends to a constant finally.
    - Value depends on scale of initial population, increasing and removing (including death and eaten) coefficient.

[^1]: In the records on 28 Sep 2015, word 'plant' refer to term 'bottom level species'.

2. Growth Rate
    - Higher rate will allow plants to recover super fast, affect the delay of recover after the population of predators decreases to a low level.
    - Big value will reduce time needed for recovering, but sudden growth may leads to a sudden growth of predators and kill themselves in a short time.
    - Small value will limits the highest population, lead to difficulty even disablity for plants to recover.
    - Need to consider death rate.
    - Value >= 1 may raise error.

3. Death Rate
    - Only method to limit maximum population of predators.
    - High rate will kill predators and population will approach to 0. For preys is like setting a small growth rate.
    - Low rate will not limits predators effectively and directly cause crash of the system, killing all the plants.
    - Death Rate should remain in a same scale as (preys' population * predation coefficient)
    
- Add-on. Diff: (2, 3):
    - Low growth rate will be influence more when the population is very low, i.e, recovering state. Death rate affect more in higher level.

4. Conversion Rate:
    - Increasing population without damaging plants too much.
    - (Conversion Rate * Predation Coefficient) working depends on population of preys.
    - High rate will lead to fast recovery and press the preys.
    - Low rate will lead to slow recovery and cannot effectively regulate preys, then sudden growth will wipe out preys.
    - Sensitivity to population of preys

5. Predation Efficiency:
    - Tool to regulate both predator and prey.
    - Be careful to change it.
    - Closeness of relation.

- Add-on. Using 4, 5 together with 2, 3 to regulate.
    - All high will lead to high amplitude, or, crash.
    - All low will lead to constant system.

(28 Sep 2015 by Joey Teng)
