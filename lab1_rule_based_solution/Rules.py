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

#   here is a list of characteristics as input for checking how program works and if all is in place. Order of characteristics plays is not important
possibleGenieConditions = ["has no hair", "has foggy eyes", "has no ears", "has round head", "speaks high elfian", "has blue foggy body"]
possibleMandalorianConditions = ["has brown hair", "has green eyes", "has small round ears", "has round head", "speaks universal", "has white skin body"]
possibleJediConditions = ["has brown hair", "has blue eyes", "has small round ears", "has round head", "speaks force", "has white skin body"]
possibleTatooinerConditions = ["has yellow hair", "has blue eyes", "has medium cubic ears", "has cubic head", "speaks tatooinean", "has black skin body"]
possibleLoonieConditions = ["has white hair", "has white eyes", "has medium cubic ears", "has round head", "speaks lunar", "has white skin body"]

#   rule manager show its suggestions over defined above characteristics and rules
print("Possible genie was considered by system as ", ruleManager.give_best_match(possibleGenieConditions))
print("Possible mandalorian was considered by system as ", ruleManager.give_best_match(possibleMandalorianConditions))
print("Possible jedi was considered by system as ", ruleManager.give_best_match(possibleJediConditions))
print("Possible tatooiner was considered by system as ", ruleManager.give_best_match(possibleTatooinerConditions))
print("Possible loonie was considered by system as ", ruleManager.give_best_match(possibleLoonieConditions))

#   here is command line interface for typing user conditions of new person and getting result from program.
print("\tIf you want to check program, then type in your conditions and then program will give response basing on your input and rules defined by experts.")
print("\tType your condition (if there is no new condition, then type 'none')")
answer = None
userConditions = []

#   always listen for input
while True:
    answer = input(">>>\t")
    
    #   this case means that user either does not know characteristics of person or ended their input
    if answer == "none" or answer == "no more":
        
        #   this means there are no characteristics from user
        if len(userConditions) == 0:
            print("\tWell, there is no condition from you, I can't even try to guess who this can be ¯\_(ツ)_/¯")
            answer = None
            continue
        
        #   try to give suggestion to user
        expertAnswer = ruleManager.give_best_match(userConditions)
        
        #   give some additional data to user if there is no match
        if expertAnswer == "no match":
            print("\tThere is no person with such characterstics, maybe there is an error in characteristics?")
            print("\tMaybe this type of person even was not introduced in system DB ¯\_(ツ)_/¯")
            answer = None
            userConditions = []
            continue
        
        #   if all is ok, then just show answer to user
        print("person with conditions that you typed is ", expertAnswer)
        userConditions = []
        answer = None
        
    #   in this case just stop program execution
    if answer == "stop program":
        print("\tOk, thanks for using this... code ( ᷇⁰ ͜U ᷇⁰ )")
        answer = None
        userConditions = None
        break
    
    #   if user has not finished typing new characteristics, then append current to the list of all characteristics
    userConditions.append(answer)
    answer = None
    