# Lab 3.02 - Birthday Song & Random Cards

1) Create a function, `birthday_song`, that prints out the happy birthday song to whatever name is input as an argument. The contract should be: 

```python
#Input: name, string 
#birthday_song prints out a personalized birthday song.  
def birthday_song(name): 
	#your code goes here 
```

2) Create a function that randomly picks 5 cards from a deck. The cards can repeat. Instead of creating a string for each card it might be useful to have two lists and pick randomly from both the lists. Write out the contract for this function:

```python
number = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
```

###Bonus!
Practice passing in lists as an argument to a function. What is different about passing in a list as an argument? Read in the associated reading about list aliasing and write down what is happening in this case.