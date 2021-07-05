# number of teams
param n > 0 integer;

# set of teams
set Teams ordered := {1..n by 1}; 

# number of slots/rounds
set Rounds ordered := {1..n-1 by 1};

# auxiliary set
set TweenTime ordered := {1 ..n-2 by 1};

# slot[i,j] is the slot when i plays j
param Slot{Teams,Teams}; 

### VARIABLES ###

var start{Teams} binary;
var to_away{Teams,TweenTime} binary;
var to_home{Teams,TweenTime} binary;

### OBJECTIVE ###

maximize Nonbreaks: 
sum{i in Teams, t in TweenTime}(to_away[i,t] + to_home[i,t]);

### CONSTRAINTS ###
subject to c0:
start[1] = 1;

subject to homeawaypattern {i in Teams, j in Teams: i<>j}:
# only one team can play at home when two teams are playing each other in a slot.
start[i]+sum{t in 1..(Slot[i,j]-1)}(to_home[i,t]-
	to_away[i,t]) + start[j]+sum{t in 1..(Slot[i,j]-1)}(to_home[j,t]-
	to_away[j,t])=1;

subject to continuity {i in Teams, t in TweenTime}: 
# a team can't head to both a away and a home game
0 <= to_away[i,t] + to_home[i,t] <= 1;

subject to homebreak {i in Teams, t in 2..n-1}:
# a team can't head to a home game from a home game
start[i]+sum{t1 in 1..t-2}(to_home[i,t1]-
	to_away[i,t1])+to_home[i,t-1] <= 1;
	
subject to awaybreak {i in Teams, t in 2..n-1}:
# a team can't head to a away game from a away game
0 <= start[i]+sum{t1 in 1..t-2}(to_home[i,t1]-
	to_away[i,t1])-to_away[i,t-1];