"""
Author: nviverosb@unal.edu.co

For educational purposes only,  check readme for instructions on how to use.
"""

import os
import re

#List of rules organized by input order
rulesList = []

#Dictionary containing all non-terminal as keys and it's values are a list with all the rules
rules = {}

#Dictionary containig the set of firsts for each non-terminal
firsts = {}

#Dictionary containig the set of nexts for each non-terminal
nexts = {}

#Dictionary containig the set of prediction for each non-terminal and each rule
prediction = {}

#Dictionary containing all the repeateds for any StopIteration
repeateds = {}

#Boolean that indicates if the grammar is LL1
isLL1 = True

EPSILON = "EPSILON"
EOF = "EOF"


#This function reads the whole input, whether it is by console or through a file
def begin_tree(route):
    
    global rulesList
    multiLineCommentary = False

    if route == "console":
        print("reading from console")
        while True:
            try:
                line = input()
                processline(line)
            except EOFError:
                break
    else:
        with open('inputs.txt') as fp:
            for line in fp:
                if multiLineCommentary:
                    if re.match(r'(.*?)\*/',line):
                        multiLineCommentary = False
                    else:
                        pass
                elif re.match(r'[ \t]*/\*.*$', line):#Turn on multiLineCommentary switch
                    multiLineCommentary = True
                else:
                    processline(line)

#Function to find the set of firsts of a given non-terminal
def findFirsts(nonTerminal,PATH):
    global rules
    global rulesList
    global firsts

    #If the nonTerminal already exists on firsts dictionary, start from there
    if nonTerminal in firsts:
        listOfFirsts = firsts[nonTerminal]
    else:
        listOfFirsts = []

    #This is an array containing al the rules of a given non-terminal
    rulesOfNonTerminal = rules[nonTerminal]

    #Looping through all the rules of a given non-terminal
    for i in range(len(rulesOfNonTerminal)):
        #List containing the set of 'instructions' of a given rule

        currentRule = rulesOfNonTerminal[i].split()

        #Iterate through all the sentences of the rule 
        for j in range(len(currentRule)):

            #Verify for epsilon or empty rule
            if currentRule[j] == EPSILON:
                if EPSILON in listOfFirsts:
                    pass
                else:
                    listOfFirsts.append(EPSILON)
                break
            elif re.match(r'[a-z_]+$', currentRule[j]):#If the current rule is made by lowercase letters, then it is a terminal, so it must be added to the firsts dictionary of that rule
                if nonTerminal in firsts and not currentRule[j] in listOfFirsts:
                    listOfFirsts.append(currentRule[j])
                break
            elif re.match(r'[A-Z_]+$', currentRule[j]):  #A non terminal, we must check for the firsts of that one
                newNonTerminalToFind = currentRule[j]
                #Verify that the non terminal actually exists
                if not newNonTerminalToFind in rules:
                    missingNonTerminalError(currentRule[j],currentRule,nonTerminal)
                    return
                #Verify if the non-terminal is calling itself
                if newNonTerminalToFind == nonTerminal:
                    if nonTerminal in firsts and EPSILON in firsts[nonTerminal]:
                        continue
                    else:
                        pass
                if not nonTerminal in PATH:
                    PATH.append(nonTerminal)
                #Verify if it has not been already in that non-terminal    
                if not newNonTerminalToFind in PATH:
                    firstsOfNewNonTerminal = findFirsts(newNonTerminalToFind,PATH)
                    #Iterate through all the list of firsts received
                    for k in range(len(firstsOfNewNonTerminal)):
                        #If they are not in the current list of firsts, add them
                        if not firstsOfNewNonTerminal[k] in listOfFirsts:
                            #Verify if it is EPSILON
                            if firstsOfNewNonTerminal[k] == EPSILON:
                                #If EPSILON is the last sentence of the rule
                                if j == len(currentRule)-1:
                                    #Add it
                                    listOfFirsts.append(firstsOfNewNonTerminal[k])
                                else:
                                    #Otherwise, evalueate the next rule
                                    pass
                            else:#If it is not EPSILON, add it
                                listOfFirsts.append(firstsOfNewNonTerminal[k])
                    #If EPSILON was not given in the list, end iterating through the rules
                    if not EPSILON in firstsOfNewNonTerminal:
                        break
                    #Remove this nonTerminal from the path
                    PATH = PATH[:len(PATH)-1]
                else:#If it has been, ommit it and keep going
                    break
            else:
                print("ERROR: sentences of a rule must be made of either lowercase or uppercase characters only, not both")
                print("Rule: ",currentRule[j])
                print("exiting...")
                exit()

    firsts[nonTerminal] = listOfFirsts
    return listOfFirsts
    
#Function to find the set of nexts of a given non-terminal
def findNexts(nonTerminal,PATH):
    global rules
    global rulesList
    global firsts
    global repeateds
    global nexts
    global isLL1

    #Iterate through all the non-terminals
    for i in range(len(rulesList)):
        #Array containing all the rules of the terminal at the ith position
        rulesOfTerminal = rules[rulesList[i]]
        #Iterate through the rules of that non-terminal
        for j in range(len(rulesOfTerminal)):
            #Array containing all the sentences of a given rule
            sentences = rulesOfTerminal[j].split()
            #Iterate through all the sentences of given rule
            for k in range(len(sentences)):
                #Found left recursion, not a LL1 grammar
                if k == 0 and sentences[k] == rulesList[i]:
                    isLL1 = False
                #Find if the nonTerminal is in this rule
                if sentences[k] == nonTerminal:
                    #FOUND IT!
                    #Verify if it is the last sentence of the rule
                    if k == len(sentences)-1:
                        repeateds[nonTerminal].append(rulesList[i])
                    elif re.match(r'[A-Z_]+$',sentences[k+1]):#Found a non-terminal
                        #Find out what's next
                        for m in range(k+1,len(sentences)):
                            #Is that a non terminal?
                            if re.match(r'[A-Z_]+$',sentences[m]):
                                #Verify if it exists
                                if not sentences[m] in rulesList:
                                    missingNonTerminalError(sentences[m],rules[rulesList[i]][j],nonTerminal)
                                #We will add the set of firsts of the given non terminal
                                sentencesToAdd = firsts[sentences[m]]
                                #If that non terminal has no EPSILON in it's firsts
                                if not EPSILON in sentencesToAdd:
                                    #We iterate and add the ones we don't have
                                    for n in range(len(sentencesToAdd)):
                                        if not sentencesToAdd[n] in nexts[nonTerminal]:
                                            nexts[nonTerminal].append(sentencesToAdd[n])
                                    #And end adding
                                    break
                                else:
                                    #Else, we iterate and add the ones we don't have minus EPSILON
                                    for n in range(len(sentencesToAdd)):
                                        if not sentencesToAdd[n] in nexts[nonTerminal] and sentencesToAdd[n] != EPSILON:
                                            nexts[nonTerminal].append(sentencesToAdd[n])
                                    #We found the last sentence and it has EPSILON
                                    if m == len(sentences)-1:
                                        repeateds[nonTerminal].append(rulesList[i])
                            else:#If not, then it must be a terminal
                                if not sentences[m] in nexts[nonTerminal]:
                                    nexts[nonTerminal].append(sentences[m])
                                    break
                        pass
                    else:#Found a terminal
                        nexts[nonTerminal].append(sentences[k+1])

def combineRepeateds(nonTerminal,PATH):

    global repeateds
    global nexts

    #List of repeateds to return
    listOfRepeateds = []
    if len(repeateds[nonTerminal]) == 0:
        return nexts[nonTerminal]

    #Verfy if we have already been there
    if not nonTerminal in PATH:
        #Unless there are no repeateds for that non Terminal
        if len(repeateds[nonTerminal]) != 0:
            #Iterate through the repeateds
            for i in range(len(repeateds[nonTerminal])):
                PATH.append(nonTerminal)
                #Append the nexts of the just visited non terminal and add the ones from this one
                arr = combineRepeateds(repeateds[nonTerminal][i],PATH) + nexts[nonTerminal]
                #Add the ones you don't currently have
                for j in range(len(arr)):
                    if not arr[j] in listOfRepeateds:
                        listOfRepeateds.append(arr[j])
                #Remove this non terminal from PATH to clean it up
                PATH.remove(nonTerminal)
    else:
        listOfRepeateds = nexts[nonTerminal]
    return listOfRepeateds

def findPredictions():

    global prediction
    global rulesList
    global rules
    global firsts
    global nexts

    #Iterate through all the non terminals
    for i in range(len(rulesList)):
        #Iterate through all the rules of the non terminal
        for j in range(len(rules[rulesList[i]])):
            #current rule
            rule = rules[rulesList[i]][j]
            #statements of that rule separated by spaces
            statements = rule.split()
            #Key to save in dictionary
            key = rulesList[i] + " -> " + rule
            #Initialize the dictionary for that rule with an empty array 
            prediction[key] = []
            listOfPredictions = []
            #Iterate thtough all the statements of that rules
            for k in range(len(statements)):
                #if we see epsilon, we must add the nexts of the current nonTerminal
                if statements[k] == EPSILON:
                    for m in range(len(nexts[rulesList[i]])):
                        if not nexts[rulesList[i]][m] in listOfPredictions:
                            listOfPredictions.append(nexts[rulesList[i]][m])
                    break
                elif re.match(r'[A-Z_]+$',statements[k]):#We found a non terminal
                    #Get the firsts of that non terminal
                    firstsOfNonTerminal = firsts[statements[k]]
                    for m in range(len(firstsOfNonTerminal)):
                        if not firstsOfNonTerminal[m] in listOfPredictions and firstsOfNonTerminal[m] != EPSILON:
                            listOfPredictions.append(firstsOfNonTerminal[m])
                    if not EPSILON in firstsOfNonTerminal:#If that non terminal has no epsilon, just break
                        break
                    elif k == len(statements)-1:#If it has epsilon, and is the last statement, add the nexts of the current terminal to the list of predictions
                        nextsOfNonTerminal = nexts[rulesList[i]]
                        #just add the ones you don't have tho
                        for m in range(len(nextsOfNonTerminal)):
                            if not nextsOfNonTerminal[m] in listOfPredictions:
                                listOfPredictions.append(nextsOfNonTerminal[m])
                elif not statements[k] in listOfPredictions:#We found a terminal, just verify it's not already and add it
                    listOfPredictions.append(statements[k])
                    break
                else:
                    break
                
            prediction[key] = listOfPredictions

def writeSyntax(file):

    global rulesList
    global prediction
    global isLL1

    f = open(file,"w")

    if len(rulesList) == 0:
        f.write("#Empty grammar, no syntax generated.")
        exit()

    #Write global variables
    f.write('token = ""\n')

    f.write('\norden = ["tk_mas","tk_menos","tk_mult","tk_div","tk_mod","tk_asig","tk_menor","tk_mayor","tk_menor_igual","tk_mayor_igual","tk_igual","tk_y","tk_o","tk_div","tk_neg","tk_dosp","tk_pyc","tk_coma","tk_punto","tk_par_izq","tk_par_der","id","tk_entero","tk_real","tk_caracter","tk_cadena","funcion_principal","fin_principal","leer","imprimir","booleano","caracter","entero","real","cadena","si","entonces","fin_si","si_no","mientras","hacer","fin_mientras","para","fin_para","seleccionar","entre","caso","romper","defecto","fin_seleccionar","estructura","fin_esctructura","funcion","fin_funcion","retornar","falso","verdadero","EOF"]\n')

    #This is going to save the current non terminal
    currentNonTerminal = ""
    #Prediction set for a given rule
    predictionSet = []
    #statements of that rule
    statements = []
    #Repeated predictionSet
    hasRepeateds = False

    #We're going to start iterating through all the predictions
    for key in prediction:

        statements = key.split()[2:]
        #Start by checking if it has changed
        nonTerminalToCheck = key.split()[0]
        if currentNonTerminal != nonTerminalToCheck:
            #write the else statement for the last declaration
            if currentNonTerminal != "":
                f.write("\telse:\n")
                syntaxErrorMessage = str(predictionSet)[1:-1]
                # syntaxErrorMessage = syntaxErrorMessage
                f.write("\t\tsyntaxErr( " + syntaxErrorMessage + " )\n")
                if hasRepeateds:
                    f.write("\t#WARNING: This non terminal has repeated no terminal across it's many rules\n")
                    repeatedPredictionsWarning(currentNonTerminal)
            hasRepeateds = False
            #Reset the prediction set for a non terminal
            predictionSet = prediction[key]
            currentNonTerminal = nonTerminalToCheck
            #Declaration of function
            declaration = "\ndef " + str(currentNonTerminal) + "():\n"
            f.write(declaration)
            f.write("\tglobal token\n")
            #Verify first rule of non terminal, write if statement and conditions
            f.write("\tif ")
        else:
            #if it has not changed, start with an elif
            f.write("\telif ")
            #Add the prediction set to the total prediction for a non termianl
            for i in range(len(prediction[key])):
                if not prediction[key][i] in predictionSet:
                    predictionSet.append(prediction[key][i])
                else:
                    hasRepeateds = True
                    isLL1 = False
        
        # print("Non terminal ",currentNonTerminal, " prediction: ",prediction[key])
        
        #Iterate through all the prediction set for that rule
        for i in range(len(prediction[key])):
            if i > 0:
                f.write(" or ")
            f.write("token == " + '"' + str(prediction[key][i]) + '"')
        f.write(" :")
        f.write("\n")
        #write what to do for that prediction set
        for i in range(len(statements)):
            if statements[i] == "EPSILON":
                f.write("\t\tpass\n")
            elif re.match(r'[A-Z_]+$', statements[i]): #Youn found a non-terminal
                f.write("\t\t" + str(statements[i]) + "()\n")
            elif re.match(r'[a-z_]+$', statements[i]):#You found a terminal
                f.write('\t\tmatch( "' + statements[i] + '" )\n')
    
    #Write the else statement for the last visited key
    f.write("\telse:\n")
    syntaxErrorMessage = str(predictionSet)[1:-1]
    # syntaxErrorMessage = syntaxErrorMessage
    f.write("\t\tsyntaxErr( " + syntaxErrorMessage + " )\n")
    if hasRepeateds:
        f.write("\t#WARNING: This non terminal has repeated no terminal across it's many rules\n")
        repeatedPredictionsWarning(currentNonTerminal)

    #Keep in mind that all this code can be reduced to one line
    #but i'm not gonna do it tho...
    #Write the match function
    f.write("\ndef match( expectedToken ):\n")
    f.write("\tglobal token\n")
    f.write("\tif token == expectedToken:\n")
    f.write("\t\ttoken = getNextToken(Control.estado, Control.token)\n")
    f.write("\telse:\n")
    f.write("\t\tsyntaxErr( expectedToken )\n")

    #Write the syntax error function
    f.write("\ndef syntaxErr(*args):\n")
    f.write("\tglobal token\n")
    f.write("\tglobal orden\n")
    f.write("\tpreds = []\n")
    f.write("\targuments = str(args)\n")
    f.write("\targs = list(args)\n")
    f.write("\tif arguments[1:-2] == \"'funcion_principal'\":\n")
    f.write("\t\tprint('Error sintactico: falta funcion_principal')\n")
    f.write("\t\texit()\n")
    f.write("\tprint('<' + str(Control.fila) + ',' + str(Control.columna)")
    f.write(" + '> Error sintactico: se encontro: \"' + str(token) +")
    f.write("'\"; se esperaba:',end=\"\")\n")
    f.write("\tfor i in range(len(orden)):\n")
    f.write("\t\tif orden[i] in arguments:\n")
    f.write("\t\t\tpreds.append(orden[i])\n")
    f.write("\tif len(preds) == 1:\n")
    f.write("\t\tprint(' \"' + preds[0] + '\".',end=\"\")\n")
    f.write("\telse:\n")
    f.write("\t\tfor i in range(len(preds)-1):\n")
    f.write("\t\t\tprint(' \"' + preds[i] + '\",',end=\"\")\n")
    f.write("\t\tprint(' \"' + preds[len(preds)-1] + '\"',end=\"\")\n")
    f.write("\t\tprint(\".\")\n")
    f.write("\n")
    f.write("\texit()\n")

    #Write the main function
    f.write("\ndef main():\n")
    f.write("\tglobal token\n")
    f.write("\treadAllLines()\n")
    f.write("\ttoken = getNextToken(Control.estado, Control.token)\n")
    f.write("\t" + rulesList[0] + "()\n")
    f.write("\tif token != 'EOF':\n")
    f.write("\t\tsyntaxErr('EOF')")
    f.write("\n\tprint('El analisis sintactico ha finalizado exitosamente.')")

    #write the final call to the main function
    f.write("\n\nmain()")

    if not isLL1:
        f.write("\n\n#WARNING: This grammar is not LL1 and will not be usable for a syntax analyzer. The cause is either because it has left recursion (which is easy to check) or beacuse it has common elements on differente predictions set for a given non terminal.\n#However, the code is still generated...")

            
# def argsprinter(*args):
#     arguments = str(args)
#     print(arguments[1:-1])


#Main function
def main():
    global rulesList
    global rules
    global firsts
    global repeateds
    global nexts
    global prediction

    if os.path.isfile("inputs.txt"):
        begin_tree("inputs.txt")
    else:
        begin_tree("console")

    # print(rules)

    #This process has to be repeated twice because of the recursion in some cases, PLEASE DON'T DELETE ANY OF THESE LINES
    for i in range(len(rulesList)):
        firsts[rulesList[i]] = findFirsts(rulesList[i],[])
    for i in range(len(rulesList)):
        firsts[rulesList[i]] = findFirsts(rulesList[i],[])

    for i in range(len(rulesList)):
        repeateds[rulesList[i]] = []
        nexts[rulesList[i]] = []
        findNexts(rulesList[i],[])
    if len(rulesList) > 0:
        nexts[rulesList[0]].append(EOF)

    # print("Primeros")
    # print(firsts)

    #The algorithm for fiding nexts is not recursive, so i had to come up with this recursive part to combine them
    #It ended up being recursive anyways...
    for i in range(len(rulesList)):
        arr = combineRepeateds(rulesList[i],[])
        for j in range(len(arr)):
            if not arr[j] in nexts[rulesList[i]]:
                nexts[rulesList[i]].append(arr[j]);

    # print("Siguientes:")
    # print(nexts)

    findPredictions()
    # print("Predictions:")
    # print(prediction)

    writeSyntax("syntax.py")

    print("Grammar succesfully generated!!!")
    print("Check the 'syntax.py' file located in this folder...")


#This function reads a line and separates the non-terminal, the arrow, and the rule itself
def processline(line):
    global rules
    rule = ""
    predicate = ""

    #Processing rule
    if re.match(r'[ \t]*[A-Z_]+', line):
        length = len(re.findall(r'[ \t]*', line)[0])#Find tabs in a line
        line = line[length:]
        length = len(re.findall(r'[A-Z_]+', line)[0])
        rule = re.findall(r'[A-Z_]+', line)[0]
        line = line[length:]
    elif re.match('[ \t]*//', line) or re.match(r'[ \t]*?$',line):#Commentaries or empty lines
        return
    else:
        print("ERROR: All rules must be composed by uppercase letters only")
        print("Rule: ", line)
        print("exiting...")
        exit()

    #Processing arrow
    if re.match(r' *\-\> *', line):
        line = line[len(re.findall(r' *\-\> *', line)[0]):]
    else:
        print("ERROR: missing arrow in rule ", line)
        print("Rule: ",line)
        print("exiting...")
        exit()

    #processing predicate
    if (len(line) == 0):
        print("ERROR: no predicate on rule")
        print("Rule: ",line)
        print("exiting...")
        exit()
    elif re.match(r'[a-zA-Z_ \t]+$', line):
        length = len(re.findall(r'[a-zA-Z_ \t]+$', line)[0])
        predicate = re.findall(r'[a-zA-Z_ \t]+$', line)[0]
    else:
        print("ERROR: invalid predicate, only alphabetic characters allowed on rules ", line)
        print("Rule ",line)
        print("exiting...")
        exit()

    #Add rule to dictionary
    if rule in rules:
        rules[rule].append(predicate)
    else:
        rulesList.append(rule)
        rules[rule] = [predicate]

def missingNonTerminalError(inexistentRule,rule,nonTerminal):
    print("ERROR: Inexistent Non Terminal ",inexistentRule,", on rule: ", nonTerminal, " -> ",rule)
    print("exiting...")
    exit()

def repeatedPredictionsWarning(nonterminal):
    print("WARNING: Non terminal ", nonterminal, " has at least two rules with one common element on the predictions set...")
    print("Check the 'syntax.py' file for further understanding\n")

main()