Round Robin Tournment Scheduling: A Case Study
==============================================
By: [Henrique Rosset](mailto:henriquerosset@hotmail.com)

> This project describes the _constrained sports tournament scheduling problem_ and solves it with operations research (OR) methods. Here, we focus on scheduling a timetable for the Brazilian football tournament known as [Gauchão](https://fgf.com.br/competicoes/profissional/23/2021/726).

## Introduction

The scheduling of round-robin tournaments is a challenging task which the operations research community is studying for quite some years.

_Round robin tournaments_ are tournaments where each team plays against each other at least once. The _double round-robin tournaments_ are the most common variant, where the teams play twice against each other. Here, we will focus on **_single round-robin tournaments_** (i.e., the teams play against each other only one time).

There are combinatory mathematical methods to schedule simple round-robin tournaments. The challenge starts when the scheduled timetable has to satisfy real-world constraints. For instance, it may be required by television networks that some matches occur on a specific date. Or two teams share a local venue and can't play a home game against different opponents on the same day, etc.

In professional sports, a timetable that satisfies these constraints can lead to huge cost savings or profit boosts for teams, TV networks, and so on. 

## Terminology

There are a few terms for the sports scheduling area that come in handy in this case study:

- **_Time slots_:** dates or slots in which at least two teams are playing, and each team plays at most one game. 
    > An even number of teams requires at least (n-1) slots to schedule a single round-robin tournament[¹](#references).
- **_Timetables_:** are the allocation of games to the slots and can be represented as a matrix.
    > Each row corresponds to a team and each column to a slot. The entry of row **i** and column **j** is the opponent of the team **i** on slot **j**[¹](#references).
- **_Break_:** a break means two consecutive home games or two consecutive away games.
    > In any home-away assignment of 2n teams that is consistent with a timetable, the number of breaks is at least 2n-2[²](#references).
- **_Balanced schedule_:** For single round-robin tournaments, a schedule is _balanced_ when the deviation between home and away games played by each team is no more than 1[¹](#references).
- **_Equitable Pattern_:** a timetable with an equitable pattern is one where every team has the same amount of breaks[¹](#references).

## The Problem

A usual single round-robin tournament configuration is: 
* Each game is played at the home venue of one of the competing teams. 
* Every team plays one game in each slot of the tournament timetable.
* Each team returns to its home venue after an away game.

This configuration is usual for a tournament where the teams represent a city or region, the competition length is a few months, and the geographical area covered by the competition is not too large. 

For these cases, a home-away-home pattern is desired. A timetable with too many breaks, on the other hand, isn't. Too many breaks can lead to a schedule that assigns an uneven amount of breaks for a team, resulting in an unfair advantage or disadvantage in the competition.

Then, we want to find a schedule that minimizes the number of breaks and at the same time takes additional constraints into account. 

> Problem known as the _constrained minimum break problem_.

### Constrained minimum number of breaks problem

    Problem Pmin:
        Instance: A timetable T of 2n teams.
        Task: Find a feasible home–away assignment 
        consistent with T, which minimizes the number 
        of breaks while respecting additional 
        home–away pattern constraints.

## Case Study

Gauchão is the regional football tournament of Rio Grande do Sul, the southernmost state of Brazil. The tournament has **12** teams and in 2021 followed a **_single round-robin_** setup. Being a regional competition, each team returns to its hometown after an excursion to play in an opposite venue.

The 2021 timetable with the home-away assignment was:

> Where `+` represents home games and `-` away games. `[B]` signals slots with a break.

|Slot                 | 1   | 2   | 3      | 4      | 5      | 6      | 7      | 8      | 9      | 10    | 11    |
|:-------------------:|:---:|:---:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
INT Internacional     |+ECJ  |-PLT|+SNL    |+YFC [B]|-NHA    |+CAX    |-GEB    |+SAJ    |-GRE    |-CEA [B]|+ESP    |
ECJ Juventude         |-INT  |+SNL|-NHA    |+PLT    |-YFC    |+GRE    |-SAJ    |-CEA    |-CAX    |+ESP [B]|+GEB    |
CAX Caxias do Sul     |+GRE  |-SAJ|+CEA    |-GEB    |+ESP    |-INT    |+SNL    |-NHA    |+ECJ    |+YFC [B]|-PLT    |
YFC Ypiranga          |-SNL  |+NHA|-PLT    |-INT [B]|+ECJ    |+SAJ [B]|-CEA    |+GEB    |-ESP    |-CAX [B]|+GRE    |
SAJ São José          |-ESP  |+CAX|+GRE [B]|-CEA    |+GEB    |-YFC    |+ECJ    |-INT    |+SNL    |+PLT [B]|-NHA    |
CEA Aimoré            |-GEB  |+ESP|-CAX    |+SAJ    |-GRE    |-PLT [B]|+YFC    |-ECJ    |+NHA    |+INT [B]|-SNL    | 
SNL São Luiz          |+YFC  |-ECJ|-INT [B]|+NHA    |-PLT    |+ESP    |-CAX    |+GRE    |+SAJ    |+GEB [B]|+CEA    |
GEB Brasil de Pelotas |+CEA  |-GRE|-ESP [B]|+CAX    |-SAJ    |-NHA [B]|+INT    |-YFC    |+PLT    |+SNL [B]|-ECJ    |
NHA Novo Hamburgo     |+PLT  |-YFC|+ECJ    |-SNL    |+INT    |+GEB [B]|-ESP    |+CAX    |+CEA    |+GRE [B]|+SAJ    |
ESP Esportivo         |+SAJ  |-CEA|+GEB    |+GRE [B]|-CAX    |-SNL    |+NHA    |-PLT    |+YFC    |+ECJ [B]|+INT    |
PLT Pelotas           |-NHA  |+INT|+YFC [B]|-ECJ    |+SNL    |+CEA [B]|-GRE    |+ESP    |-GEB    |-SAJ [B]|+CAX    |
GRE Grêmio            |-CAX  |+GEB|-SAJ    |-ESP [B]|+CEA    |-ECJ    |+PLT    |-SNL    |+INT    |+NHA [B]|-YFC    |

#### Home-Away Pattern:

The 2021 timetable was balanced given that the deviation between home and away games was 1 for every team.

Team  |INT|ECJ|CAX|YFC|SAJ|CEA|SNL|GEB|NHA|ESP|PLT|GRE|
------|---|---|---|---|---|---|---|---|---|---|---|---|
Home  |	6 |	5 | 6 |	5 |	6 |	5 |	5 |	5 |	6 |	6 |	6 |	5 |
Away  |	5 |	6 | 5 |	6 |	5 |	6 |	6 |	6 |	5 |	5 |	5 |	6 |

#### Break Assessment:

The number of breaks in the 2021 timetable was 26 (sub-optimal).

> For any 2n (n ∈ N), there exists a timetable of 2n teams that has a consistent home–away assignment with 2n − 2 breaks.[²](#references)

Team  |INT|ECJ|CAX|YFC|SAJ|CEA|SNL|GEB|NHA|ESP|PLT|GRE|
------|---|---|---|---|---|---|---|---|---|---|---|---|
Breaks|	2 |	1 | 1 |	3 |	2 |	2 |	2 |	3 |	2 |	3 |	3 |	2 |

Also, the distribution of these breaks was not fair. There was teams with 2 breaks advantage on its opponents. 

## Method

A two-phase approach can be employed to solve a general constrained minimum break problem[³](#references):

1) **Schedule Phase**: Find a feasible schedule compatible with the required match constraints (i.e., two specific teams have to play on slot x). In this phase, home/away patterns are ignored. 

1) **Break Phase**: Find a feasible home–away assing for each game that minimizes the number of breaks while respecting additional constraints.

In this project, we solved only the _Break Phase_. The goal was to identify if the home-away assignment for the 2021 timetable was sub-optimal.

We used the AMPL modeling language to model the constrained minimum break problem. The problem is an integer programming problem and the solver employed was the [CBC Solver](https://github.com/coin-or/Cbc). Also, an auxiliary python script was written to handle the model outputs.

The project structure is:

    .
    ├── ampl                     
    |   ├── homeawaypattern.mod  # constrained minimum break problem AMPL model
    |   └── slots_2021fgf.dat    # 2021 timetable 
    └── main.R                   # auxiliary python script

## Results

Applying the OR methods, we were able to find a feasible home-away pattern (HAP) with fewer breaks than the proposed pattern for the 2021 schedule, proving that the HAP assignment for the 2021 schedule was sub-optimal.

Pros of our schedule:
* has fewer breaks (18 against the original 26);
* doesn't have an equitable pattern but distributes fairly the breaks between the teams;
> In the original assignment, some teams had two breaks advantage on their opponents.
* takes local derbys into account when assigning the patterns;
> The original assignment allowed two teams from the same city to play home games (ECJ/CAX, slot 10)

Cons:
* the HA assignment is not balanced.

The proposed 2021 timetable with the new home-away assignment is:

|Slot                 | 1    | 2      | 3      | 4      | 5      | 6      | 7      | 8      | 9      | 10     | 11     |
|:-------------------:|:----:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
INT Internacional     |+ECJ  |-PLT    |-SNL [B]|+YFC    |-NHA    |-CAX [B]|+GEB    |-SAJ    |+GRE    |-CEA    |+ESP    |
ECJ Juventude         |-INT  |+SNL    |-NHA    |+PLT    |-YFC    |-GRE [B]|+SAJ    |-CEA    |+CAX    |-ESP    |+GEB    |
CAX Caxias do Sul     |+GRE  |-SAJ    |+CEA    |-GEB    |+ESP    |+INT [B]|-SNL    |+NHA    |-ECJ    |+YFC    |-PLT    |
YFC Ypiranga          |-SNL  |-NHA [B]|+PLT    |-INT [B]|+ECJ    |-SAJ    |+CEA    |-GEB    |+ESP    |-CAX    |+GRE    |
SAJ São José          |-ESP  |+CAX    |-GRE    |-CEA [B]|+GEB    |+YFC [B]|-ECJ    |+INT    |-SNL    |+PLT    |-NHA    |
CEA Aimoré            |-GEB  |-ESP [B]|-CAX [B]|+SAJ    |-GRE    |+PLT    |-YFC    |+ECJ    |-NHA    |+INT    |-SNL    | 
SNL São Luiz          |+YFC  |-ECJ    |+INT    |+NHA [B]|-PLT    |-ESP [B]|+CAX    |-GRE    |+SAJ    |-GEB    |+CEA    |
GEB Brasil de Pelotas |+CEA  |-GRE    |+ESP    |+CAX [B]|-SAJ    |+NHA    |-INT    |+YFC    |-PLT    |+SNL    |-ECJ    |
NHA Novo Hamburgo     |+PLT  |+YFC [B]|+ECJ [B]|-SNL    |+INT    |-GEB    |+ESP    |-CAX    |+CEA    |-GRE    |+SAJ    |
ESP Esportivo         |+SAJ  |+CEA [B]|-GEB    |+GRE    |-CAX    |+SNL    |-NHA    |+PLT    |-YFC    |+ECJ    |-ESP    |
PLT Pelotas           |-NHA  |+INT    |-YFC    |-ECJ [B]|+SNL    |-CEA    |+GRE    |-ESP    |+GEB    |-SAJ    |+CAX    |
GRE Grêmio            |-CAX  |+GEB    |+SAJ [B]|-ESP    |+CEA    |+ECJ [B]|-PLT    |+SNL    |-INT    |+NHA    |-YFC    |

With a total of 18 breaks, distributed as follow.

Team  |INT|ECJ|CAX|YFC|SAJ|CEA|SNL|GEB|NHA|ESP|PLT|GRE|
------|---|---|---|---|---|---|---|---|---|---|---|---|
Breaks|	2 |	1 | 1 |	1 |	2 |	2 |	2 |	1 |	2 |	1 |	1 |	2 |

The number of home/away games for each teams is:

Team  |INT|ECJ|CAX|YFC|SAJ|CEA|SNL|GEB|NHA|ESP|PLT|GRE|
------|---|---|---|---|---|---|---|---|---|---|---|---|
Home  |	6 |	6 | 5 |	6 |	6 |	7 |	5 |	5 |	4 |	5 |	6 |	5 |
Away  |	5 |	5 | 6 |	5 |	5 |	4 |	6 |	6 |	7 |	6 |	5 |	6 |

## References 

¹ [Rasmussen & Trick, 2008](https://www.sciencedirect.com/science/article/pii/S0377221707005309)

² [Miyashiro & Matsui, 2005](https://www.sciencedirect.com/science/article/pii/S0167637704000951)

³ [Trick, 2000](https://link.springer.com/chapter/10.1007/3-540-44629-X_15)
