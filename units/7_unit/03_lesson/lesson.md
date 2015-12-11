# Lesson: Methods

##Learning Objectives
Students will be able to... 
* Define and identify: **method**, **`__str__`**, **`__add__`**, **operator overloading**
* Create a class with an init method
* Understand and use the self 
* Instantiate a class with an argument

##Materials/Preparation
* [Do Now]
* [Lab]
* Read through the handout, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 30 Minutes | Lab         |
| 10 Minutes | Discussion  |

## Instructor's Note

1. **Do Now**
    * Display the Do Now on the board.
2. **Lesson**
	* Discuss Do Now
		* **method**: functions inside a class. First argument is always self. What is a method we have seen? (init)
		* Ask students how they would distinguish between the two time variable
		* **`__string__`**: Need a method called `__str__`. This will get called when you print an object. It returns a string
			* Have the students practice writing `__str__` for time for 5 minutes
			* Have a student write up their string method on the board. 
		* **`__add__`**: add is another method that gets called when the plus sign is used. Takes in another time object and returns a time object that is the sum of both 
			* overwriting add is called **operator overloading** because you are re-writing the code used to make the + work  
			* work together with students to come up with the add time algorithm
3. **Lab**	
	* Have students finish up the time adding method
	* Have students work on manga too lab from book
4. **Debrief**
	* Go over students' questions. Ask what an instance is versus an object vs a class. Ask difference between method and attribute.

  
[Do Now]:do_now.md
[Lab]:lab.md