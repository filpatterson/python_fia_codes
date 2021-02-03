class Statement(object):
    def __init__(self):
        self.statementsList = []
        self.response = None
        
    def then(self, statement):
        self.response = statement
        return self
        
    def conditions_matching(self):
        raise NotImplementedError("Please Implement this method")
     
"""
    Logical class IF that contains logic of how to check match of user condition with simple
one-statement rule
"""   
class If(Statement):
    def __init__(self, condition):
        super().__init__()
        self.statementsList.append(condition)
        
    def conditions_matching(self, userConditions):
        for userCondition in userConditions:
            if userCondition == self.statementsList[0]:
                return True
            
        return False
    
    def give_response(self, userConditions):
        if self.conditions_matching(userConditions):
            return self.response
        else:
            return "no match"
  
"""
    Logical class AND that contains logic of how to handle matching of user conditions with
statements
"""      
class And(Statement):
    def __init__(self, conditions):
        super().__init__()
        self.statementsList.append(conditions)
        
    def conditions_matching(self, userConditions):
        #   shows how many matchings to rule statements are found
        matching_value = 0
        
        #   check all conditions from user to have matches with rule statements
        for userCondition in userConditions:
            for statement in self.statementsList:
                
                #   in case if there is an inner OR perform check conform OR logical algorithm
                if isinstance(statement, Or):
                    
                    #   if user condition meets OR requirements then increment matching by one
                    if statement.conditions_matching(userCondition):
                        matching_value += 1
                
                #   is user condition is matching rule statement then increment matching value
                if userCondition == statement:
                    matching_value += 1
                    
        #   check if all rule statements have been matched
        if matching_value == len(self.statementsList):
            return True
        
        return False
    
    def give_response(self, userConditions):
        if self.conditions_matching(userConditions):
            return self.response
        else:
            return "no match"
                            
"""
    Logical class OR that contains logic of how to handle matching of user conditions with
statements
"""
class Or(Statement):
    def __init__(self, conditions):
        super().__init__()
        self.statementsList.append(conditions)
        
    def conditions_matching(self, userConditions):
        
        #   iterate through all user conditions and all rule statements
        for userCondition in userConditions:
            for statement in self.statementsList:
                
                #   check if there is inner AND statement
                if isinstance(statement, And):
                    
                    #   if user conditions match AND statement
                    if statement.conditions_matching(userConditions):
                        return True
                
                #   if user condition match any of statements
                if userCondition == statement:
                    return True
                
        return False
    
    def give_response(self, userConditions):
        if self.conditions_matching(userConditions):
            return self.response
        else:
            return "no match"
