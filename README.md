# FIA laboratory works
 
Hello, my name is Dumitru Cretu, I am a student of Technical University of Moldova, group FAF-172. This repo is a storage of my laboratory works for FIA. This repo will be updated over the time with new laboratory works and their realization information in the document. All code for laboratory works was written using Python 3.
 
# Table of contents

- [Laboratory work nr. 1](#laboratory-work-nr-1)
  * [OOP-based problem solution](#oop-based-problem-solution)
  * [Rule-based expert-like system](#rule-based-expert-like-system)
  * [Rule-based expert system (akinator prototype)](#rule-based-expert-system-as-akinator)
 
# Laboratory work nr. 1
 
The first laboratory work is about making a rule-based expert system that will be able to get a database of rules and basing on them to give answers to the user statements.

Conform conditions of the laboratory work expert system should be able to define type of tourist that is arriving a Luna-City (looks like Cyberpunk reference, my respect if it is so) basing on characteristics of that person. To implement this laboratory work, it was proposed to study the existing implementation of the expert system, but I decided to try to make my implementation from scratch for a deeper analysis of the interpretation of logical rules or statements.

To demonstrate the effectiveness of expert systems in comparison with other methods of determining the response to statements, which are based on simple if-then checks, an OOP-oriented approach to solving this problem was also implemented.

## OOP-based problem solution

From the point of view of OOP, the problem is solved quite easily: the parent class "Person" is set, which sets the characteristics that any tourist can have. Each type of tourist will be defined by a child class, which will inherit the properties and methods of the parent class, setting its own unique characteristics for this type of tourists. In the case when the user wants to check that a tourist belongs to a certain group, the system will create an object based on the user's statements and compare it with the types of tourists (children of the parent class). The program can give an answer both in full compliance of all characteristics, and partial compliance, determining which type the given set of statements most corresponds to.

To make the system a little more flexible, a second format was implemented.

In OOP approach parent class sets form of rule and the user statements, each child represents a rule. Class property represents fact/statement.

### Parent class (form for rules and user statements)

The parent class contains 8 characteristics: hair, eyes, ears, head shape, height, mouth size, communication language, skin color. Already at this stage, you can see the main problem of this approach - if it is necessary to add characteristics, it will be necessary to supplement the parent class, then supplement the child classes. This approach does not imply variation in the number of statements and the number of facts within the rule.

```python
class Person(object):
    
    def __init__(self, hair, eyes, ears, headshape, height, mouthSize, language, skinColor):
        self.hair = hair
        self.eyes = eyes
        self.ears = ears
        self.headshape = headshape
        self.height = height
        self.mouthSize = mouthSize
        self.language = language
        self.skinColor = skinColor
```

Considering that the set of characteristics for a person and for her types is always identical, the parent class also contains a function for checking the correspondence of statements to the rule (again, the type of a person is considered here as a rule).

```python
def compliance_degree(self, person):
        complianceDegree = 0
        
        if(isinstance(person, Person)):
            if self.hair == person.hair:
                complianceDegree += 1
                
            if self.eyes == person.eyes:
                complianceDegree += 1
                
            if self.ears == person.ears:
                complianceDegree += 1
                
            if self.headshape == person.headshape:
                complianceDegree += 1
                
            if self.height == person.height:
                complianceDegree += 1
                
            if self.mouthSize == person.mouthSize:
                complianceDegree += 1
                
            if self.language == person.language:
                complianceDegree += 1
                
            if self.skinColor == person.skinColor:
                complianceDegree += 1
                
            return complianceDegree
        
        else:
            raise TypeError("Incorrect type of object passed for person verification")
```

### Child class (rule and how rule can be declared in such a system)

The child class inherits all the fields and methods of the parent, having the ability to rewrite them for itself. In this situation, only the method for creating the object will be rewritten, specifying facts to match the rule, and an additional method will be specified that determines the answer when the rule matches.

This can be seen in the example of the Genie child class.

```python
class Genie(Person):
    def __init__(self):
        super().__init__(
            hair="none", 
            eyes="foggy", 
            ears="none", 
            headshape="round", 
            height="small", 
            mouthSize="none", 
            language="high elfian", 
            skinColor="blue foggy"
        )
        
    def show_class(self):
        return "genie"
```

In this example, fields are specified with their corresponding values. This is an optional implementation element and you can simply pass a set of arguments, and the system itself will pick up the argument to the corresponding field.

Each such rule must be recorded in the database to be able to check incoming claims with the rules entered into the database. In this implementation, this is done through the "list" structure in Python.

```python
class PersonalitiesDB:
    def __init__(self):
        self.listOfPersonalities = [Genie(), Mandalorian(), Jedi(), Tatoiner(), Loonie()]
```

### User interface and why filling forms can be annoying

The program initializes a set of "rules" and then listens for input from the user, who will enter data in a sequential manner.

```python
#   initialize a database of all possible personalities
personsDB = PersonalitiesDB()

#   input all characteristics of person (small letters)
print("Input characteristics of the person using words with small letters (if there is no concrete characteristic print 'unknown' or 'some'")
hair = input("Hair of the person (none, yellow, brown, black, white): ")
eyes = input("Eyes of the person (foggy, small green, brown, blue, black): ")
ears = input("Ears of the person (none, small round, small, small cubic): ")
headshape = input("Person shape of head (round, cubic): ")
height = input("Height of the person (small, medium, tall): ")
mouthSize = input("Person size of mouth (none, medium, small, big): ")
languages = input("Language that this person speaks the most (high elfian, universal, force, tatooinean, lunar, universal): ")
skinColor = input("Skin color of the person (blue foggy, white, brown, black): ")
```

After the user has indicated all the necessary statements, the program creates an object based on them and compares this object with the "rule objects", determining which of them is closest to the set of statements specified by the user.

```python
randomPerson = Person(hair, eyes, ears, headshape, height, mouthSize, languages, skinColor)
randomPerson.show_info()

bestComplianceValue = 0
bestComplianceType = None

for personalityType in personsDB.listOfPersonalities:
    complienceDegree = personalityType.compliance_degree(randomPerson)
    if complienceDegree > bestComplianceValue:
        bestComplianceValue = complienceDegree
        bestComplianceType = personalityType
    
print("it is a " + bestComplianceType.show_class())
```

Here you can see another problem with this approach: the system requires sequential input of information, which is inconvenient if the user does not have a sequential set of statements (imagine a person who is trying to remember what the last passer-by looks like - he will remember details in a random sequence). The algorithm can be improved either by specifying by the user what format of the statement he defines, which imposes an additional burden on the user and requires additional actions, or revision of the code for automatic picking up characteristics, which will make the code narrowly focused and to comply only with a certain scenario (if necessary, introduce new rules and the whole new verification system will have to rewrite most of the code).

In addition, the current implementation requires a complete rewriting if the statement format has additional conditions, such as matching a set of facts or matching at least one of the facts, which requires the implementation of a nested structure. And even with this improvement in the code, the system will be completely rewritten if the task of the system changes.

### Conclusion over OOP approach

This approach allows you to quickly implement a semblance of a smart system, make it efficient and fast for a specific task. The structure of such a system is primitive and easy to describe. If a programmer has to implement a system of answering only one question with a clear and uniform set of characteristics, then this is the best solution.

When new details are added to the question, new questions arise, and complex connections between facts are established, this system collapses and becomes ineffective. It is not an expert system, but an effective attempt to make it "visible" (or, as the English saying goes, "smoke and mirrors").

## Rule-based expert-like system

In the first approach, rules were viewed as a collection of facts. In fact, a rule is a collection of facts with complex relationships and even nested rules. A static implementation of such a system is impossible.

Let's start by looking at the basic logical relationships of facts.

Most often, logical statements "if-then" are used, where, if the fact "if" is observed, the answer is "then". The answer is uniform, but the conditions can be multilevel.

To get a positive answer in certain statements, you must match the full set of facts. In this case, the logical AND operand is used, specifying the following expression format:

***IF** first condition **AND** second condition **THEN** answer*

There are situations in which it is necessary to correspond to at least one fact in order to receive a positive answer. The logical OR operand will be used here, specifying the following format:

***IF** first condition **OR** second condition **THEN** answer*

The mathematical interpretation of logical expressions implies a positive answer as 1 or TRUE, and negative as 0 or FALSE. Expression logic implies a numeric interpretation, using OR as an addition operand and an AND operand as a multiplication operand.

In logical expressions, the operation NOT is also considered, which requires inconsistency with a certain statement, however, this operation is absent in this system (the reason will be highlighted below).

### Logical statement definition

For the correct implementation of the system, it is worth deciding on the structure of the entities used in it, their methods.

The above information indicates several important aspects:

- A rule consists of a set of facts and / or internal rules;
- The facts in the rule can be regulated by different logical relationships;
- A rule can check a statement for truth or falsity, having also a unique answer if the statement is true

Based on these aspects, the Statement class was built.

```python
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
```

The class consists of two fields:

- an array of facts and / or internal rules within the current rule;
- the answer given by the rule if all conditions are met.

Given the specifics of the rules, there are two methods:

- then sets the answer if all the conditions of the rule are met;
- conditions_matching is abstract and, depending on the logical relationship of facts / internal rules, specifies how to check the compliance of the statement with the specified rule.

As mentioned above, AND and OR are most often used. The logical operand does NOT actually require a discrepancy to a certain condition, which can be rephrased into another condition so as not to add separate logic of behavior just for the sake of such an operation. This is not the best solution if the system is limited in memory and all statements are thrown into a common heap without repetitions, where it would be beneficial to minimize the number of statements by using logical negation operands, but in the system without limitation on the number of statements, the possibility of their repetition and the unwillingness to make a system cumbersome, one can abandon the rarely used operand, which can be interpreted differently.

Therefore, it was decided to make three classes-children: IF, AND, OR.

The first class is used in a situation where the rule consists of one fact and it is necessary to comply only with it.

```python
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
```

Here you can see that the Statement class has already defined the most important parts of the rule. Still rule requires specification of conditions checking algorithm and to specify response that will be given if the rule is satisfied.

The IF and AND rules are more complex.

```python
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
```

Between the statements inside the OR rule, a relationship is established that if at least one statement was met, then the rule is considered satisfied. Nevertheless, OR implies the possibility of nested rules, and as mentioned earlier, in addition to the current one, there is an IF and an AND. IF sets only one condition, which would be wrong to consider separately within a set of conditions and this would violate the integrity of the logic. There can be no nested OR rule either due to the illogicality of such a structure and violation of the integrity of the statement. Therefore, the AND rule remains, which can be nested inside the current one, which requires an internal check for compliance with the nested AND rule.

Therefore, when implementing the AND rule, it is worth considering the same logic: inside the AND rule there cannot be a nested AND rule or a nested IF rule, but the nested OR rule is permissible, which is why this scenario of a possible rule must also be taken into account. Unlike OR, the interaction with conditions / internal rules is different.

Within the OR, even one condition is sufficient to comply with the rule. Inside AND, all conditions / nested rules must be met, which is why the program will summarize the successfully met statements and then check that the number of statements met is equal to the total number of statements / rules inside the current rule.

```python
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
```

### Rule manager

Algorithms of rules, their creation and functioning were indicated above. The system should not only check the user's claims for compliance with these rules, but also collect all the rules, check each one in turn. For this purpose, a rules manager has been defined.

```python
class RuleManager(object):
    def __init__(self, listOfRules):
        self.rulesList = listOfRules
        
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
```

At this point, the manager collects all the rules at launch, but it can be quickly modified to collect rules in real time during its life cycle. The manager checks that all the rules from the database are consistent and then addresses each rule by passing a user statement for verification and waiting for a response. If a positive response is received, it will indicate an output based on the rule response.

The algorithm can be improved by adding the ability to answer multiple responses if multiple rules are met.

### Rules DB

The peculiarity of this system consists in specifying the rules in the form of logical statements, which increases readability and understanding on the part of a person, and also makes the process simple for the possibility of further adding rules (it is even possible to receive rules from the user, given the ease of entering a new rule).

```python
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
```

### User interface

The user interface in this system is significantly superior to the previous approach due to flexibility: the user can enter claims in any order, and the system will build an assertion based on them for checking by rules. This approach makes the system simple for the user and convenient.

```python
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
```

### Example of interaction with user

![Example of work with expert system based on rules from Laboratory work nr. 1](https://github.com/filpatterson/python_fia_codes/blob/master/screenshot.PNG?raw=true)

## Rule-based expert system as akinator

The second implementation, despite the advantage over the first, has a disadvantage: it assumes that the user enters conditions on his own and the answer is determined based on them. It is more efficient for the user to answer the minimum set of questions to determine the answer to save time and system resources for processing all user conditions (there can be many of them). To accurately determine the answer, it was also necessary to enter the entire set of conditions, which is inconvenient for the user.

It was decided to create a third implementation with increased efficiency and minimized response time. This solution was inspired by the structure of the akinator programs.

The akinator program asks multiple-choice questions (yes, no, don’t know - the set of questions depends on the system), which are interpreted by the system to filter potential answers. The program gives an answer as soon as the number of answers is reduced to one.

Generation of questions based on conditions is carried out in several formats (the basis is the presence of an algorithm for discarding the conditions of violated rules):

* Generation of a question based on the frequency of a condition inside the rules that were not violated at the time. This format is convenient when there are many conditions and their intersections. The disadvantage of this approach is a large number of questions if the required answer is atypical (in the context of tourists, the program can ask many questions leading to incorrect answers before it gets to the right ones)
* Generation of a question based on a random selection from unbroken rules. In a worst-case scenario, it can ask as many questions as possible leading to incorrect answers before getting to the correct ones. Will mostly give the average sample time.
* Generation of a question depending on the "weight" of the condition. This approach is already closer to the field of artificial intelligence, since "weight" can be determined in several ways.
  * "Weight" is set by an expert or predefined. Non-adaptive option, requires significant analysis by a person or other system.
  * "Weight" is set on the basis of previously given answers, the coefficient of the effectiveness of the answer to the question for filtering answers.

The first and second methods are provided for the system. The first option was also modified to generate a question based on the last answer (the most frequent condition will be displayed according to the last answer). The implementation of the latter method would be maladaptive under the first subparagraph or too complex to implement under the second subparagraph.

### Changes comparing to the rule-based expert-like system

To begin with, the constructor of the manager is changed, since now the program will store two additional constructions: a dictionary of conditions with the corresponding answers and a list of answers available at this iteration. The constructor sets all conditions and answers to the dictionary in accordance with the rules, and sets the list of answers based on all the answers in the rules.

```python
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
```

A method of "zeroing" the system appears, since the system must update the list of acceptable answers after the procedure is completed and update the data (useful when adding new rules to the system dynamically).

```python
#   reset system if answer was given or appeared error
    def reset_system(self):
        self.possibleAnswers.clear()
        for rule in self.rulesList:
            if issubclass(type(rule), Statement):
                self.set_conditions_with_answer(rule, rule.response)
                self.possibleAnswers.append(rule.response)
            else:
                raise TypeError("Non rule object in database")
```

For the correct entry of information into the dictionary, a method was needed that allows you to enter new conditions with the corresponding answer or update existing ones by adding new answers, taking into account that the rule may contain sub-rules.

```python
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
```

One of the main functions of this implementation - filtration of potential responses. The system accepts the conditions positively answered by the user and, based on them, filters the set of possible answers, rejecting the answers of the violated rules.

If the system has one answer, then it issues it as its own guess. If there is more than one answer, then the program will return the current set of answers and proceed to the next iteration of filtering.

```python
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
```

If the user answers that this condition does not meet, the system will ignore it for the duration of the current search for an answer. It is impossible to remove answers, since a rule can have several variants of the current condition (for the example of personality types: if a personality type can have black or red hair, then when the user answers "he has no red hair", the type cannot be deleted, since there is still a black hair condition ). In addition, the system allows incomplete compliance with the rule, which is only possible with a given implementation of the ignore process.

```python
    #   remove condition that was not matched
    def del_incorrect_condition(self, condition):
        self.conditionSolutionDictionary.pop(condition)
```

The second important function in the implementation is implemented in two versions.

The first option makes it possible to generate the most frequent condition based on the available rules. Upon completion, the system does not unload the generated condition, which makes it possible to reuse it in the next search.

```python
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
```

The second option generates the question at random.

```python
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
```

The rest of the changes will only affect the user's interaction with the system.

### User interace

The system gives the manager the rules, and then listens for user input, reacting to various user responses and the results of internal system processes, informing the user about them.

```python
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
```

**Important detail**: if a programmer wants to change the method of generating questions, then only the call to the filtering method in the user interaction segment needs to be changed.

### Example of akinator-based program with "often-condition" principle

![Example of work with expert akinator system based on rules from Laboratory work nr. 1](https://github.com/filpatterson/python_fia_codes/blob/master/screenshot-2.PNG?raw=true)