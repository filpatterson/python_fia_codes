from RuleSystem import If, And, Or, Statement

"""
Class responsible for taking all rules and performing check if user conditions meet all requirements of any rule
"""
class RuleManager(object):
    def __init__(self, listOfRules):
        self.rulesList = listOfRules
        self.allAttributesDictionary = dict
        
    #   return answer basing on user conditions matching any of the available rules.
    def give_best_match(self, userConditions):
        response = None
        
        for rule in self.rulesList:
            if isinstance(rule, And) or isinstance(rule, Or) or isinstance(rule, If) or isinstance(rule, Statement):
                response = rule.give_response(userConditions)
            else:
                raise TypeError("rules db has a non-rule object")
            
            if response != "no match":
                return response
            
        return "no match"