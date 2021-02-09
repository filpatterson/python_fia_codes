"""
Parent class with basic methods, fields and abstract method that must be implemented by children
"""
class Statement(object):
    #   create object of the class
    def __init__(self):
        self.statementsList = []
        self.response = None
        
    #   set response field and return object
    def then(self, statement):
        self.response = statement
        return self
        
    #   abstract method that must be implemented by child
    def conditions_matching(self):
        raise NotImplementedError("Please Implement this method")
     
"""
Logical IF class that contains one-statement-rule principle of work (WAS NOT TESTED, USE WITH CAUTION)
"""   
class If(Statement):
    def __init__(self, condition):
        super().__init__()
        self.statementsList.append(condition)
      
    #   function checks if user characteristics meet statement of the rule  
    def conditions_matching(self, userConditions):
        for userCondition in userConditions:
            if userCondition == self.statementsList[0]:
                return True
            
        return False
    
    #   give response basing on user characteristics and matching to the rule
    def give_response(self, userConditions):
        if self.conditions_matching(userConditions):
            return self.response
        else:
            return "no match"
  
"""
Logical AND class that contains multi-statement-rule with possible inner OR-rules (this class was mainly used in work)
"""      
class And(Statement):
    def __init__(self, conditions):
        super().__init__()
        for condition in conditions:
            self.statementsList.append(condition)
        
    #   function checks is user characteristics meet statements of the rule
    def conditions_matching(self, userConditions):
        #   shows how many matchings to rule statements are found
        matching_value = 0
        
        #   check if there is list of user characteristics or only one user characteristic
        if isinstance(userConditions, list):
            
            #   come through all charactestics from user and all statements of rule
            for userCondition in userConditions:
                for statement in self.statementsList:
                    
                    #   if statement is an inner OR-rule then perform check
                    if isinstance(statement, Or):
                        if statement.conditions_matching(userCondition):
                            matching_value += 1
                    
                    #   increment matching value if statement meets user condition
                    if userCondition == statement:
                        matching_value += 1
                        
            #   check if all rule statements have been matched
            statementsAmount = len(self.statementsList)
            if matching_value == statementsAmount:
                return True
        
        #   else if there is only one user characteristic
        else:
            
            #   come through all statements
            for statement in self.statementsList:
                if isinstance(statement, Or):
                    if statement.conditions_matching(userConditions):
                        matching_value += 1
                    
                    if userConditions == statement:
                        matching_value += 1
            
            #   check if all rule statements have been matched
            statementsAmount = len(self.statementsList)
            if matching_value == statementsAmount:
                return True
            
        return False
    
    #   give response basing on meeting statements
    def give_response(self, userConditions):
        if self.conditions_matching(userConditions):
            return self.response
        else:
            return "no match"
                            
"""
Logical OR class with multi-statement-rule principle of work, where user conditions must meet even one statement to match all rule
"""
class Or(Statement):
    def __init__(self, conditions):
        super().__init__()
        for condition in conditions:
            self.statementsList.append(condition)
       
    #   check how user conditions match all statements of rule 
    def conditions_matching(self, userConditions):
        
        #   check if there is a list of user conditions
        if isinstance(userConditions, list):
            
            #   iterate through all statements and user conditions
            for userCondition in userConditions:
                for statement in self.statementsList:
                    
                    #   check if there is inner AND rule and check matching this rule
                    if isinstance(statement, And):
                        if statement.conditions_matching(userConditions):
                            return True
                    
                    #   if user condition matches any of statements
                    if userCondition == statement:
                        return True
        
        #   check if one user characteristic is meeting even one statement                   
        else:
            for statement in self.statementsList:
                if isinstance(statement, And):
                    if statement.conditions_matching(userConditions):
                        return True
                
                if userConditions == statement:
                    return True
        
        return False
    
    #   give response basing on matching result
    def give_response(self, userConditions):
        if self.conditions_matching(userConditions):
            return self.response
        else:
            return "no match"
