from RuleSystem import If, And, Or, Statement
import random

"""
Class responsible for taking all rules and performing check if user conditions meet all requirements of any rule
"""
class RuleManager(object):
    
    #   constructor of rule manager, setting list of rules, dictionary for all conditions,
    # set list of available at the current iteration answers
    def __init__(self, listOfRules):
        self.rulesList = listOfRules
        self.conditionSolutionDictionary = dict()
        self.possibleAnswers = []
        
        #   get all conditions and answers from rules
        for rule in self.rulesList:
            if issubclass(type(rule), Statement):
                self.set_conditions_with_answer(rule, rule.response)
                self.possibleAnswers.append(rule.response)
            else:
                raise TypeError("Non rule object in database")
        
    #   reset system if answer was given or appeared error
    def reset_system(self):
        self.possibleAnswers.clear()
        for rule in self.rulesList:
            if issubclass(type(rule), Statement):
                self.set_conditions_with_answer(rule, rule.response)
                self.possibleAnswers.append(rule.response)
            else:
                raise TypeError("Non rule object in database")
    
    #   add all new conditions and answers to the system
    def set_conditions_with_answer(self, rule, answer):
        if issubclass(type(rule), Statement):
            for condition in rule.statementsList:
                
                #   if there is an inner rule call function recursively
                if issubclass(type(condition), Statement):
                    self.set_conditions_with_answer(condition, answer)
                #   otherwise, add conditions with answers to the dictionary
                else:
                    self.set_element_in_dictionary(self.conditionSolutionDictionary, condition, answer)
        else:
            raise TypeError("Non rule object was sent for processing to dictionary")
        
    #   filter possible answers and conditions basing on user input (here is considered an "yes" answer)
    def filter_possible_answer(self, condition):
        currentIterationAnswer = self.conditionSolutionDictionary.get(condition)
        
        #   prepare list for current filtration iteration
        newPossibleAnswers = []
        if isinstance(currentIterationAnswer, list) and len(currentIterationAnswer) > 0:
            
            #   check to which answer from list of available at the current iteration answers current condition
            # correlates and append it to the list of available answers
            for innerAnswer in currentIterationAnswer:
                for possibleAnswer in self.possibleAnswers:
                    if possibleAnswer == innerAnswer:
                        if possibleAnswer not in newPossibleAnswers:
                            newPossibleAnswers.append(possibleAnswer)
                        
            #   set available after current iteration answers
            self.possibleAnswers.clear()
            self.possibleAnswers = newPossibleAnswers
            
            return self.possibleAnswers
            
        #   if there is only one answer left            
        elif type(currentIterationAnswer) == str:
            self.possibleAnswers.clear()
            self.possibleAnswers = currentIterationAnswer
            return currentIterationAnswer
        
        #   raise error if there is no such condition
        else:
            raise ValueError("There is no such condition in the system")
        
    #   remove condition that was not matched
    def del_incorrect_condition(self, condition):
        self.conditionSolutionDictionary.pop(condition)
        
    #   pick condition for asking from list of available ones at the current iteration
    def pick_often_condition_to_ask(self):
        keysToPickFrom = []
        
        #   find available at the current iteration moment conditions
        for key in list(self.conditionSolutionDictionary.keys()):
            for possibleAnswer in self.possibleAnswers:
                if type(self.conditionSolutionDictionary.get(key)) == list:
                    for conditionAnswer in self.conditionSolutionDictionary.get(key):
                        if conditionAnswer == possibleAnswer:
                            keysToPickFrom.append(key)
                else:
                    if possibleAnswer == self.conditionSolutionDictionary.get(key):
                        keysToPickFrom.append(key)
                        
        if type(keysToPickFrom) == list and len(keysToPickFrom) == 0:
            return None
        
        
        #   choose such a condition that is most often met in the available rules
        theMostPopularKey = None
        amountOfUsage = 0
        for key in keysToPickFrom:
            answersWithCorrespondingCondition = self.conditionSolutionDictionary.get(key)
            if type(answersWithCorrespondingCondition) == list:
                if len(answersWithCorrespondingCondition) > amountOfUsage:
                    theMostPopularKey = key
                    amountOfUsage = len(answersWithCorrespondingCondition)
            
            elif type(answersWithCorrespondingCondition) == str:
                if 1 > amountOfUsage:
                    theMostPopularKey = key
                    amountOfUsage = 1
            
            else:
                raise TypeError("invalid answer type")
            
        keysToPickFrom.clear()

        return theMostPopularKey
    
    #   pick condition for asking from list of available ones at the current iteration
    def pick_random_condition_to_ask(self):
        keysToPickFrom = []
        
        #   find available at the current iteration moment conditions
        for key in list(self.conditionSolutionDictionary.keys()):
            for possibleAnswer in self.possibleAnswers:
                if type(self.conditionSolutionDictionary.get(key)) == list:
                    for conditionAnswer in self.conditionSolutionDictionary.get(key):
                        if conditionAnswer == possibleAnswer:
                            keysToPickFrom.append(key)
                else:
                    if possibleAnswer == self.conditionSolutionDictionary.get(key):
                        keysToPickFrom.append(key)
                        
        if type(keysToPickFrom) == list and len(keysToPickFrom) == 0:
            return None

        #   choose randomy condition to ask
        randomCondition = random.choice(keysToPickFrom)
        return randomCondition
        
    #   add condition and answer into the dictionary
    def set_element_in_dictionary(self, dictionary, key, value):
        if key not in dictionary:
            dictionary[key] = value
        elif type(dictionary[key]) == list:
            dictionary[key].append(value)
        else:
            dictionary[key] = [dictionary[key], value]