### Question 1

We all know that currently, we are going through a pandemic period. Several measures are now taken so that we can overcome this period and resume our daily activities like we did earlier. Educational institutions are trying to resume all activities and they are doing their best to do it successfully.

We know that this disease is contagious and anyone affected comes in contact with another person, then he or she needs to stay in quarantine. Suppose an educational institution “X” has hired you to design a system known as an “Infected tracker”. An infected tracker tries to figure out the region/number of surrounding people who can be affected by a single person. Then it prints the maximum region infected. Here you can consider Y being infected and N is not infected.

Your task is to find the maximum region with Y i.e. max people infected in a region so that strict measures can be taken in that region using DFS. Keep in mind that two people are said to be infected if two elements in the matrix are Y horizontally, vertically or diagonally. ================================================================== Sample Input 1

N N N Y Y N N

N Y N N Y Y N

Y Y N Y N N Y

N N N N N Y N

Y Y N N N N N

N N N Y N N N

==================================================================

Sample Output

7

==================================================================


Sample Input 2:

Y Y N N N

N Y Y N N

N N Y N N

Y N N N N

======================================================= 

Sample Output

5


### Question 2 

There is an Alien(Xenomorph) Apocalypse in XCITY and every minute Aliens are attacking human beings around them.

Imagine XCITY as a grid where "A" represents the position of an Alien, "H" represents the position of a human being and "T" represents heat traps set up by humans which the Aliens cannot cross. The regions of the Aliens will not overlap, i.e. two or more Aliens will never have a common human to prey on.

An Alien can attack human beings on it's north,south,east and west simultaneously using its deadly advanced physical attributes. A human being becomes a host after an attack and a new Alien spawns in that position.

Your task is to find out the minimum number of minutes it would take for the Aliens to attack all the humans around them using BFS. Also, print "No one survived" if no human beings survive the Apocalypse or "number_of_human_beings survived" otherwise.

================================================================== Sample Input 1:

5

4

A H T H

H H T A

T T H H

A H T H

H T H H

Sample Output 1:

Time: 4 minutes

No one survived

Explanation 1: There are 3 regions here marked with Red, Green and Blue borders. The attacking Aliens have Yellow background and the humans being attacked have Red background.

At Time=1, three Aliens in 3 different regions attack the humans around them simultaneously (north, south, east, west). New Aliens spawn in place of the attacked humans.

At Time=2, two Aliens in Red and Blue regions attack the humans around them simultaneously and new aliens spawn in place of the attacked humans. The Green region has no more humans left.

At Time=3, only one Alien in the Blue region attacks the human to the south of it and a new alien spawns in place of the attacked human. The Red region has no more humans left.

At Time=4, only one Alien in the Blue region attacks the last human to the west of it and so in the final grid, no humans are left.

Sample Input 2:

3

3

A H H

T H H

H T H

Sample Output 2:

Time: 4 minutes

1 survived

Explanation 2: In the 3x3 grid of XCITY, the Alien at (0,0) will attack the human at (0,1) at 1 minute and a new Alien will spawn at (0,1). Then this new Alien will attack the humans at (0,2) and (1,1) simultaneously and two new Aliens will spawn there. Either of these two will attack the human at (1,2) in the 3rd minute. And the newly spawned Alien will lastly attack the human at (2,2) in the 4th minute. However one human being at (2,0) will survive since no Aliens can get to him/her.

==================================================================
