from RuleHandler import RuleManager
from RuleSystem import If, And, Or, Statement

#   This is DB that Rule Manager will use to answer on questions following defined rules. Rules can be changed, added, removed and so on.
rulesDB = [
    
    #   Example of a rule defining which person is Genie. Object 'And()' consists of statements that must be met to consider match.
    # Object 'Or()' consists of statements where one or more must be satisfied to consider match. Function 'then()' consists of
    # answer that object must provide if all conditions match.
    And(
        ["has no hair", "has foggy eyes", "has no ears", "has round head", Or(["speaks force", "speaks high elfian"]), "has blue foggy body"]
    ).then("genie"),
    
    And(
        [Or(["has black hair", "has brown hair"]), Or(["has green eyes", "has brown eyes", "has gray eyes"]), "has small round ears", "has round head", "speaks universal", "has white skin body"]
    ).then("mandalorian"),
    
    And(
        [Or(["has black hair", "has brown hair"]), "has blue eyes", "has small round ears", "has round head", Or(["speaks universal", "speaks force"]), Or(["has white skin body", "has yellow skin body", "has black skin body"])]
    ).then("jedi"),
    
    And(
        ["has yellow hair", "has blue eyes", "has medium cubic ears", "has cubic head", Or(["speaks universal", "speaks tatooinean"]), "has black skin body"]
    ).then("tatooiner"),
    
    And(
        ["has white hair", Or(["has white eyes", "has black eyes"]), "has medium cubic ears", "has round head", Or(["speaks lunar", "speaks tatooinean", "speaks force"]), "has white skin body"]
    ).then("loonie")
]

#   rule manager take DB of rules for further work
ruleManager = RuleManager(rulesDB)

#   here is command line interface for typing user conditions of new person and getting result from program.
print("\tIf you want to check program, then type in your conditions and then program will give response basing on your input and rules defined by experts.")
print("\tChoose condition out of the following ones (type 'yes', 'no' or 'do not know')")
answer = None

#   loop listening for user input
while True:
    
    #   find condition to ask from user
    currentConditionToCheck = ruleManager.pick_often_condition_to_ask()
    
    #   make sure that there are still conditions left to iterate through
    if currentConditionToCheck == None:
        print("\tThere are no conditions left. I can not define the person, maybe you will try again?")
        ruleManager.reset_system()
        print("\t...\n\t...\n\t...\n\t...initializing new round...\n\t...\n")
        continue
    
    print("\tMaybe your person " + currentConditionToCheck + " ?")
    
    answer = input(">>>\t")
    
    #   if answer of the user is 'yes' then system removes all elements that do not have current condition
    # and prepares next question conform remaining variants or give answer if there is only one variant left
    if answer == "yes":
        answerFromSystem = ruleManager.filter_possible_answer(currentConditionToCheck)
        
        #   if there is answer basing on user answers
        if type(answerFromSystem) != list and answerFromSystem != None:
            print("\tSystem suggests that this is a " + answerFromSystem)
            ruleManager.reset_system()
            currentConditionToCheck = None
            print("\t...\n\t...\n\t...\n\t...initializing new round...\n\t...\n")
            continue
        
        #   if there is answer that is encapsulated inside list
        elif type(answerFromSystem) == list and len(answerFromSystem) == 1:
            print("\tSystem thinks that this is a " + answerFromSystem[0])
            ruleManager.reset_system()
            currentConditionToCheck = None
            print("\t...\n\t...\n\t...\n\t...initializing new round...\n\t...\n")
            continue
        
        #   if there is empty list or no answer at all
        elif (type(answerFromSystem) == list and len(answerFromSystem) == 0) or answerFromSystem == None:
            print("\tThere is no answer basing on your answers. Either there is no answer or you answered incorrect. Try again.")
            ruleManager.reset_system()
            currentConditionToCheck = None
            print("\t...\n\t...\n\t...\n\t...initializing new round...\n\t...\n")
            continue
        
        #   default case
        else:
            ruleManager.del_incorrect_condition(currentConditionToCheck)
            continue
        
    #   if the answer is no, then remove condition from list of possible next questions
    elif answer == "no":
        ruleManager.del_incorrect_condition(currentConditionToCheck)
        currentConditionToCheck = None
    
    #   pick another variant if current one is unknown for the user
    elif answer == "do not know":
        continue
   
    #   if there is some another input from the user 
    else:
        print("So you can not choose a variant out of mentioned ones? I guess i can ignore it ¯\_(ツ)_/¯")
        continue
    