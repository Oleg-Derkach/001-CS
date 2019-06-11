# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:15:41 2019

@author: Pups
"""

import turtle
import math

###########################################################################

# Q1

def pythagorian_pair(a,b):
    """   
    (int, int) -> bool
    Returns True if the two numbers (a and b) are a pythagorean pair  """
    c = math.sqrt(a**2 + b**2)    
    return int(c) == c

#for i in range(1,100):
#    for y in range(1,100):     
#        if pythagorian_pair(i,y):
#            print("i...", i, "  y...", y)
  
##########################################################################   
    
# Q2
   
def mh2kh(s):
    """ (number) - > number
    cjnverts "s" given in miles/hour into the equivalent speed in kilometers/hour    
    """
    return 1.609344 * s 
    
##########################################################################    
    
# Q3   
   
def in_out(xs, ys, side):
    """(number number number) - > None
    Prompts the user to enter a (x,y) coordinates and checks if it is conteined
    inside of the square defined by the parameters(xs, ys, side) where (xs, ys)
    is the bottom left corner of the square, side is the length of one side of the
    square . If it is conteined in the square the function will print True, otherwise 
    it will print False"""
    
    x = float(input('Please enter x coordinate: '))
    y = float(input('Please enter y coordinate: '))
    
    check = y <= ys + side and x <= xs + side and x >= xs and y >= ys
    print(check)
    
##########################################################################    
    
# Q4

def safe(n):
    """
    (int) => bool
    return False if "n" conteins the digit 9 or can be divided by 9
    otherwise it returns True """
    
    first = n // 10
    last = n - (first*10)
    return first != 9 and last != n % 9 != 0

##########################################################################    
    
# Q5
    
def quote_maker(quote, name, year):
    """
    (string, string, int) -> string
    returns a string in the form : "in %s, a parson called %s said: "%s"" %(year, name, quote)    
    """
    return "in %s, a parson called %s said: \"%s\"" %(year, name, quote)
    
##########################################################################    
    
# Q6
    
def quote_displayer():
    """
    (None) => None
    Prompts the user to input a qoute, name and year and prints a string to the screen
    in the form: "in %s, a parson called %s said: "%s"" %(year, name, quote)    """
    
    quote = input('Give me a quote: ')
    name = input('Who said that? ')
    year = input('What year did she/he/THEM say that? ')
    print(quote_maker(quote, name, year))
    
##########################################################################    
    
# Q7

def rps_winner():
    """
    (None) => None
    Prompts the user for a player 1 decision of rock, paper or scissors. Then asks the
    user for player 2 decision with the same choices. It then determines the
    winner and display it to the screen. """
    
    print("What choice did player 1 make? ")
    choice1 = input('Type one of the following options: rock, paper, scissors: ')
    print("What choice did player 2 make? ")
    choice2 = input('Type one of the following options: rock, paper, scissors: ')
    
    player1Wins = ((choice1 == 'rock' and choice2 == 'scissors')
    or (choice1 == 'scissors' and choice2 == 'paper')
    or (choice1 == 'paper' and choice2 == 'scissors')
    or (choice1 == 'paper' and choice2 == 'rock'))
    tie = choice1 == choice2
    player2Wins = not (player1Wins) and not (tie)
    print("Player 1 wins? That is", player1Wins)
    print("Tie? That is", tie)
    print("Player 2 wins? That is", player2Wins)
    
##########################################################################    
    
# Q8
    
def fun(x):
    """
    (number) -> number
    Solves the equation 10^(4y) = x + 3 for y and returns the value of y """   
    return math.log10(x + 3)/4
           
##########################################################################    
    
# Q9
    
def ascii_name_plaque(name):
    """
    string > None
    Display to the screen a name plaque with the given name padded by 1 space
    inside a box of stars with underscores before and after the name """
    
    newStr = "* __" + name + "__ *"
    stars = len (newStr)
    
    print("*" * stars)
    print("* " + (stars-3) * ' ' + "*")
    print(newStr)
    print("* " + (stars-3) * ' ' + "*")
    print("*" * stars)
    
##########################################################################    
    
# Q10
    
def draw_car():
    

    t = turtle.Turtle()
    t.speed(50)
    t.pensize(3)
    t.penup()
    
    #Right Weel
    t.forward(200)
    t.pendown()
    t.begin_fill()
    t.color('grey')
    t.circle(5)
    t.color('black')
    t.right(90)
    t.penup()
    t.forward(25)
    t.pendown()
    t.left(90)
    t.circle(30)
    t.right(90)
    t.penup()
    t.forward(25)
    t.pendown()
    t.left(90)
    t.circle(55)
    t.penup()
    t.left(90)
    t.forward(55)
    mid = t.pos()
    
    t.color('grey')
    for x in range(5):
        t.penup()
        t.goto(mid)
        t.right(360/5)
        t.forward(5)
        t.pendown()
        t.forward(25)
    
    t.color('black')
    
    t.penup()
    t.goto(mid)
    t.right(90)
    t.backward(400)
    t.pendown()
    t.color('grey')
    t.circle(5)
    t.color('black')
    t.right(90)
    t.penup()
    t.forward(25)
    t.pendown()
    t.left(50) 
    t.circle(30)
    t.right(90)
    t.penup()
    t.forward(25)
    t.pendown()
    t.left(90)
    t.circle(55)
    
    t.penup()
    t.left(90)
    t.forward(55)
    mid = t.pos()
    

def cad_cashier(price, payment):
    """
    Calculates the change in Canadian dollars the user should receive.
    """
    
    change = float(payment - price)  # Здача = Сумма - цена 
    roundedChange = 0.05 * round(float(change)/0.05)
    return round(roundedChange,2)
     
def split_tester(N, d):
    """str, str > bool
    thefunction splits the given string N into a sequence of d length integers
    It then returns True if the sequence is strictly increasing """   

    lastNum = -1
    checkInc = True
    seq = ''
    d = int(d)
    
    for i in range(0,len(N), d):
        newNum = N[i:i+d]
        seq += newNum       
        if int(newNum) < lastNum:
            checkInc = False            
        lastNum = int(newNum)        
        if i < len(N) - d:
            seq += ', '
    print(seq)  
    return checkInc
    
 
def nonrepetitive(s):
    """str >bool 
    returns True if the given string in nonrepetitive and False otherwise. 
    A nonrepetitive string is one that does not contain any sobsting twice in a row.
    """
    
    for i in range(len(s)):
        for x in range(i,len(s)-1):
            lookFor = s[i:x+1]
            lookIn = s[x+1:x+1+len(lookFor)]
            if lookFor == lookIn:
                return False
    return True


def make_deck(n):
    """
    (int) > list of int
    Returns a list of inegers representing the strange deck with num ranks."""
    
    deck = []
    for x in range(1,5):
        for j in range(1,n+1):
            deck.append(100*x+j)
    return deck



ваитвар

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    