Double Round Robin Tournment Scheduling 
=======================================

> This project aims to solve a constrained sports tournament scheduling problem using operations research methods. Here, we focus on solving the timetable for a regional Brazilian southern division commonly know as Gauchão.

## Introduction

The scheduling of round-robin tournaments is a challenging task which the operations research community is studying for quite some years. 

_Round robin tournaments_ are tournaments where each team plays against all other teams. The _double round-robin tournaments_ are the most common variant, where the teams play twice against each other. 

There are combinatory mathematical methods to schedule simple round-robin tournaments. The challenge starts when the scheduled timetable has to satisfy real-world constraints. For instance, it may be required by television networks that some matches occur on a specific date. Or two teams share a local venue and can't play a home game against different opponents on the same day, etc.

In professional sports, a timetable that satisfies these constraints can lead to huge cost savings or profit boosts for teams, TV networks, and so on.

## Terminology

There are a few common terms for the sports scheduling area:

- **_Time slots_:** dates or slots in which at least two teams are playing, and each team plays at most one game. 
    > An even number of teams requires at least (n-1) slots to schedule a single round-robin tournament. 
- **_Timetables_:** are the allocation of games to the slots and can be represented as a matrix.
     > Each row corresponds to a team and each column to a slot. The entry of row **i** and column **j** is the opponent of the team **i** on slot **j**.
- **_Break_:** a break means two consecutive home games or two consecutive away games.
- **_Balanced schedule_:** For single round-robin tournaments, a schedule is _balanced_ when the deviation between home and away games played by each team is no more than 1. 
- **_Equitable Pattern_:** a timetable with an equitable pattern is one where every team has the same amount of breaks.

## The Problem

Gauchão is the regional first division football tournament of Rio Grande do Sul, the southernmost state of Brazil. The tournament has **12** teams and in 2021 followed a **_single round-robin_** setup. Being a regional competition, each team returns to its hometown after an excursion to play in an opposite venue.

### 2021 Schedule:

|Slot               | 1   | 2   | 3     | 4     | 5     | 6     | 7     | 8     | 9     | 10    | 11    |
|:-----------------:|:---:|:---:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
1 Internacional     |+02  |-11  |+07    |+04 [B]|-09    |+03    |-08    |+05    |-12    |-06 [B]|+10    |
2 Juventude         |-01  |+07  |-09    |+11    |-04    |+12    |-05    |-02    |-03    |+02 [B]|+08    |
3 Caxias do Sul     |+12  |-05  |+06    |-08    |+10    |-01    |+07    |-09    |+02    |+04 [B]|-11    |
4 Ypiranga          |-07  |+09  |-11    |-01 [B]|+02    |+05 [B]|-06    |+08    |-10    |-03 [B]|+12    |
5 São José          |-10  |+03  |+12 [B]|-06    |+08    |-04    |+02    |-01    |+07    |+11 [B]|-09    |
6 Aimoré            |-08  |+10  |-03    |+05    |-12    |-11 [B]|+04    |-02    |+09    |+01 [B]|-07    | 
7 São Luiz          |+04  |-02  |-01 [B]|+09    |-11    |+10    |-03    |+12    |+07    |+07 [B]|+06    |
8 Brasil de Pelotas |+06  |-12  |-10 [B]|+03    |-05    |-09 [B]|+01    |-04    |+11    |+07 [B]|-02    |
9 Novo Hamburgo     |+11  |-04  |+02    |-07    |+01    |+08 [B]|-10    |+03    |+09    |+09 [B]|+05    |
10 Esportivo        |+05  |-06  |+08    |+12 [B]|-03    |-07    |+09    |-11    |+04    |+02 [B]|+10    |
11 Pelotas          |-09  |+01  |+04 [B]|-02    |+07    |+06 [B]|-12    |+10    |-08    |-05 [B]|+03    |
12 Grêmio           |-03  |+08  |-05    |-10 [B]|+06    |-02    |+11    |-07    |+01    |+09 [B]|-04    |


### Home-Away Pattern:

Team	          |Home |Away
------------------|-----|---
Internacional	  |6	|5
Juventude	      |5	|6
Caxias do Sul	  |6	|5
Ypiranga	      |5	|6
São José	      |6	|5
Aimoré	          |5	|6
São Luiz	      |5	|6
Brasil de Pelotas |5	|6
Novo Hamburgo	  |6	|5
Esportivo	      |6	|5
Pelotas	          |6	|5
Grêmio	          |5	|6

### Break Assessment:

Team	          |Breaks
------------------|-----
Internacional	  |2	
Juventude	      |1	
Caxias do Sul	  |1	
Ypiranga	      |3	
São José	      |2	
Aimoré	          |2	
São Luiz	      |2	
Brasil de Pelotas |3	
Novo Hamburgo	  |2	
Esportivo	      |3	
Pelotas	          |3	
Grêmio	          |2	
