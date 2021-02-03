from RuleHandler import RuleManager
from RuleSystem import If, And, Or, Statement

rulesDB = [
    
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

ruleManager = RuleManager(rulesDB)

possibleGenieConditions = ["has no hair", "has foggy eyes", "has no ears", "has round head", "speaks high elfian", "has blue foggy body"]
possibleMandalorianConditions = ["has brown hair", "has green eyes", "has small round ears", "has round head", "speaks universal", "has white skin body"]
possibleJediConditions = ["has brown hair", "has blue eyes", "has small round ears", "has round head", "speaks force", "has white skin body"]
possibleTatooinerConditions = ["has yellow hair", "has blue eyes", "has medium cubic ears", "has cubic head", "speaks tatooinean", "has black skin body"]
possibleLoonieConditions = ["has white hair", "has white eyes", "has medium cubic ears", "has round head", "speaks lunar", "has white skin body"]

print("Possible genie was considered by system as ", ruleManager.give_best_match(possibleGenieConditions))
print("Possible mandalorian was considered by system as ", ruleManager.give_best_match(possibleMandalorianConditions))
print("Possible jedi was considered by system as ", ruleManager.give_best_match(possibleJediConditions))
print("Possible tatooiner was considered by system as ", ruleManager.give_best_match(possibleTatooinerConditions))
print("Possible loonie was considered by system as ", ruleManager.give_best_match(possibleLoonieConditions))

print("\tIf you want to check program, then type in your conditions and then program will give response basing on your input and rules defined by experts.")
print("\tType your condition (if there is no new condition, then type 'none')")
answer = None
userConditions = []
while True:
    answer = input(">>>\t")
    if answer == "none" or answer == "no more":
        if len(userConditions) == 0:
            print("\tWell, there is no condition from you, I can't even try to guess who this can be ¯\_(ツ)_/¯")
            answer = None
            continue
        expertAnswer = ruleManager.give_best_match(userConditions)
        if expertAnswer == "no match":
            print("\tThere is no person with such characterstics, maybe there is an error in characteristics?")
            print("\tMaybe this type of person even can be not introduced in system DB ¯\_(ツ)_/¯")
            answer = None
            userConditions = []
            continue
        print("person with conditions that you typed is ", expertAnswer)
        userConditions = []
        answer = None
        
    if answer == "stop program":
        print("\tOk, thanks for using this... code ( ᷇⁰ ͜U ᷇⁰ )")
        answer = None
        userConditions = None
        break
    
    userConditions.append(answer)
    answer = None
    