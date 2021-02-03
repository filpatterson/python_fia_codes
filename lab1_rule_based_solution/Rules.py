from RuleHandler import RuleManager
from RuleSystem import If, And, Or, Statement

rulesDB = [
    And(["has no hair", "has foggy eyes", "has no ears", "has round head", Or(["speaks universal", "speaks high elfian"])]).then("it is a genie"),
    Or([And(["no human", "no man"]), And(["no hair", "no eyes"])]).then("monster")
]

ruleManager = RuleManager(rulesDB)

userConditions = [
    "has no hair", "has foggy eyes", "has no ears", "has round head", "speaks universal", "no man", "no human"
]

userAnotherConditions = [
    "no human", "no man"
]

print(ruleManager.give_best_match(userConditions))
print(ruleManager.give_best_match(userAnotherConditions))