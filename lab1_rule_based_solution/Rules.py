from RuleHandler import RuleManager
from RuleSystem import If, And, Or, Statement

rulesDB = [
    And(["has no hair", "has foggy eyes", "has no ears", "has round head", "speaks high elfian"]).then("it is a genie")
]

ruleManager = RuleManager(rulesDB)

userConditions = [
    "has no hair", "has foggy eyes", "has no ears", "has round head", "speaks high elfian"
]

print(ruleManager.give_best_match(userConditions))