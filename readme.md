# README
This README is intended to document this project.

## Introduction

This project is a job assessment and it is used to validate abilities using the Django framework as well as Front-End skills.
There are 3 main components:
- Items Selection
- Derivative
- UI Names

There is a section to document each feature and subsections to further explain decisions made in the project.

## How to deploy

Start the python Django server
```
 python manage.py runserver <port>
```
Access http://localhost:8085/login/ to start.
The test user is **samuel** with the password *jackson*


## Items Selection

### Problem Description

The problem is stated as follows, we have **n** people each rating **n** articles based on desireability.
We must assign each item to one and only one person each, trying to maximize the global desireability.

### Solution

The solution was implemented using a *Greedy* approach, that is we first order by ascending order all the people's valuations and then we  select the maximum; after that we place the item in a *selected items* list and continue selecting the highest value if and only if such item is not already in the *selected items* list or the person associated with the item hasn't had already an item selected.

### Worst-case Scenarios

The worst-case scenarios using this approach are for example say we have 3 items with 3 people each with the following valuations

- Person1 valuated Item1 100
- Person1 valuated Item2 90
- Person1 valuated Item3 0
- Person2 valuated Item1 80
- Person2 valuated Item2 20
- Person2 valuated Item3 20
- Person3 valuated Item1 20
- Person3 valuated Item2 20
- Person3 valuated Item3 20

Using the *Greedy* algorithm we select Item1 and give it to Person1, we then select whichever item to the rest, the global desireability is 140.If instead we select Item2 to Person1, Item1 to Person2 and Item3 to Person3 the global desireability is 190 that is far greater than using the algorithm.

## Derivative

### Problem Description

We suppose a polynomial expressed in the form of multiplications and additions, for example "2*x*x+2"
would be 2x^2+2; the program calculates its derivative and displays a graph plotting the function for both the function and its derivative.

### Solution

The solution was implemented using given that the derivative of **x^n** is **nx^(n-1)**.
So the algorithm parses each term separately and given the derivative of each term it calculates the derivative of the whole polynomial.

### Pending

This version does not group common terms nor does it remove zeroed terms.
Should not use eval() function to calculate the point value.


##  UI Names

This is a simple interface to change the names of the top nav menu.
