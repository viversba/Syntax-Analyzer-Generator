# Simple Syntax Analyzer Genrator

```
Nicolás Viveros 
nviverosb@unal.edu.co
```


The following, is a simple syntax analyxer generator written completely in python. It can currently be tested and used with the lexer file located at the `/Lexer ` folder. It works with **LL(1)** grammars ONLY.

## Usage with other Lexer Analyzers

For usage with other lexers, you will have the change the name of the tokens according to the names of your lexer tokens. Aditionally, your have to provide the `getNextToken()` method, and the Control class.

## How to use 

In order to use the generator, you have to specify the grammar in the `inputs.txt` file, which has the following format:

* All non terminals have to be in UPPECASE.

 ```
 E.g:  
 
 SUM is permitted
 Sum is NOT permitted
 ```
* Once you're done specifiyng the non termninal, you have to use an arrow `->` to specify the end of the left part of the rule.
* To specify the right part of the rule, you have to write a set of terminals and/or non terminals (terminals MUST be all lowercase)

```
E.g: 

abc is permitted
aBs is not permitted

```

* _Bot terminals and non terminals MUST be alphabetic characters only (a-z including \_ )_

```
Example grammars:

S -> A B C
S -> D E
A -> dos B tres
A -> EPSILON
B -> cuatro C cinco
B -> EPSILON
C -> seis
C -> EPSILON
D -> uno A E
D -> B
E -> tres A
```

### Commentaries

The program supports commenaties in the `inputs.txt` file, and they must be in one of the two formats:

`//Single line comments`


```
/*
Multi line comments
*/
```