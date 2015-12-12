#Lesson 2.02: Data Types & Casting

##Learning Objectives
Students will be able to... 
* Define and identify: **string, casting, floating point number (float), integer**
* Describe different representations of data in Python 
* Convert from one data type to another data type

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

## Instructor's Notes
1. Lesson
  1. Ask students to define 'type'? Talk about types in the context as a way to represent data.(give example of string, int, float) 
  2. Ask students what they thought having str('12') did? Define this as casting. 
  3. Ask students what they did to cast an integer into a string? Define the int function if the students were unable to guess it from the lab.
  4. Break for a few minutes to have students write down how they would produce the following program using the input function:
    ```
    > 
    Give me a number you want to multiply by 2: 4
    8
    => None
    ```
  5. Have students write their answers on the board. Discuss what would happen if you put in 1.5 instead of 4? If input is a float, can cast with float(num)
  6. `type`: ask students what they think `type('a')` would return.  Why might you want to use `type`?
2. Lab
    1. Practice predicting what casting will do to inputs. 
    2. Create a halving program as well as program that halves to whole numbers. 
3. Opportunities for more
    1. If students are moving quickly, it is possible to introduce the concepts of booleans here. Discuss how students would represent binary (0s and 1s). In practice these translate to True and False. Convert numbers to boolean, and booleans to number.
  

[Do Now]:do_now.md
[Lab]:lab.md