# FIA laboratory works
 
Hello, my name is Dumitru Cretu, I am a student of Technical University of Moldova, group FAF-172. This repo is a storage of my laboratory works for FIA. This repo will be updated over the time with new laboratory works and their realization information in the document. All code for laboratory works was written using Python 3.
 
# Table of contents

- [Laboratory work nr. 1](#laboratory-work-nr-1)
  * [OOP-based problem solution](#oop-based-problem-solution)
  * [Rule-based expert-like system](#rule-based-expert-like-system)
  * [Rule-based expert system (akinator prototype)](#rule-based-expert-system-as-akinator)
  * [Rule-based expert system (strict akinator prototype)](#rule-based-akinator-with-strict-attribute-characteristic-relation)
- [Laboratory work nr. 2](#laboratory-work-nr-2)
 
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

The last two implementations, including the current one, were carried out together with my colleague Mihai Scebec from the FAF-172 group. The work was carried out separately in the cooperation of solutions for the implementation of the task (the code was written separately, but the ways of solving certain problems were stipulated).

The second implementation, despite the advantage over the first, has a disadvantage: it assumes that the user enters conditions on his own and the answer is determined based on them. It is more efficient for the user to answer the minimum set of questions to determine the answer to save time and system resources for processing all user conditions (there can be many of them). To accurately determine the answer, it was also necessary to enter the entire set of conditions, which is inconvenient for the user.

It was decided to create a third implementation with increased efficiency and minimized response time. This solution was inspired by the structure of the akinator programs.

The akinator program asks multiple-choice questions (yes, no, don’t know - the set of questions depends on the system), which are interpreted by the system to filter potential answers. The program gives an answer as soon as the number of answers is reduced to one.

Generation of questions based on conditions is carried out in several formats (the basis is the presence of an algorithm for discarding the conditions of violated rules):

* Generation of a question based on the frequency of a condition inside the rules that were not violated at the time (idea and approximate algorithm of was provided by Scebec Mihai). This format is convenient when there are many conditions and their intersections. The disadvantage of this approach is a large number of questions if the required answer is atypical (in the context of tourists, the program can ask many questions leading to incorrect answers before it gets to the right ones)
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

## Rule-based akinator with strict attribute-characteristic relation

The latest version of the implementation of this algorithm was conceived with the aim of making the akinator more efficient. In the previous version of the akinator, which I implemented, the drawback was the impossibility of passing through the specific attributes of the rule, since their number could change, the order of the attributes was not fixed, which is why the system could not systematize the information received. Akinator in such an implementation is forced to ask specific questions about the presence of a certain characteristic in the user statement.

The latest implementation removes this limitation of the akinator, allowing him to ask questions based on the attributes and characteristics assigned to these attributes. Thus, the number of questions to determine the answers is minimal, but the system makes several compromises:

* Rules should follow a clear structure in which rules can be represented in a table, where the attribute is a column and the rule itself is a table row.
* All characteristics in the rule follow a strictly defined sequence: first, the value is set for the first attribute, then for the second, and so on.
* Variations of one rule (for example, when a rule may contain either one characteristic or another for a certain attribute) will be indicated as separate records with the same answer.

Already from here you can see that this implementation is perfect for situations in which the expert system works with strictly defined areas or objects of consideration. The rules in the system are strictly defined and structured.

This implementation belongs to Mihai Scebec. My contribution was to think through the idea of ​​attributes.

### Rules estimation

To begin with, the system accepts rules in the form of a strictly defined structure of values with a certain sequence. At the end of each rule, the rule index is indicated, which determines the system's response to the compliance with this rule in a response dictionary.

```python
race1 = ['nose',    'common skin',  'common eyes',    'common body',  'common hair',  0]
race2 = ['nose',    'common skin',  'red eyes',       'tall body',    'red hair',     1]
race3 = ['gills',   'scaly skin',   'wide eyes',      'low body',     'n/a hair',     2]
race4 = ['nose',    'scaly skin',   'dark eyes',      'common body',  'dark hair',    3]
race5 = ['nose',    'common skin',  'offended eyes',  'common body',  'common hair',  4]
race6 = ['nose',    'common skin',  'common eyes',    'common body',  'white hair',   5]
```

After defintion of all rules or their import from database system appends all of them to the local list for addressing.

```python
#   define list of all rules and append all rules to that list
allSpeciesList=[]
allSpeciesList.append(race1)
allSpeciesList.append(race2)
allSpeciesList.append(race3)
allSpeciesList.append(race4)
allSpeciesList.append(race5)
allSpeciesList.append(race6)
```

As was previously mentioned, the last parameter of the rule is the index that addresses to the answer from the response dictionary. The following code shows the creation of the dictionary.

```python
speciesDict = {
  race1[-1]: "dirts",
  race2[-1]: "marsmen",
  race3[-1]: "neptunes",
  race4[-1]: "jews",
  race5[-1]: "tolerasts",
  race6[-1]: "lunies"
}
```

### Question generator, filter for unmatched rules

The system should analyze the user's response, removing rules that do not match the already specified user responses. For this purpose, the following function has been implemented.

```python
#   remove elements (conditions) that are not matching with user answer
def removeFromAllSpecies(redactedAnsw):
    for x in allSpeciesList:
        if redactedAnsw not in x:
            allSpeciesList.remove(x)
    for x in allSpeciesList:
        if redactedAnsw not in x:
            removeFromAllSpecies(redactedAnsw)
```

The generation of questions and possible answers to a question occurs due to the reference system, which decomposes the rules into components for analysis. To begin with, it is worth pointing out how the system sets benchmarks based on the available (not yet excluded) rules.

The landmarks will just decompose the rules into a "tabular" structure, making it possible for the system to further analyze the required questions and generate answers to these questions.

```python
#   set orientirs for work
def createOrientirs():

    #   reinitialize (clear) orientirs to work with
    print('Starting to create orientirs...')
    orientirs.clear()

    #   attributes iterator
    xind = 0

    #   rules iterator
    yind = 0
    
    #   show how many species are at the moment
    print('length of allSpecies: ' + str(len(allSpeciesList)))
    
    #   iterate through all attributes of the rule (considered that all rules have the 
    # same amount of attributes defined in specific manner)
    for x in range(len(allSpeciesList[0])):
        temp = []

        #   iterate through all rules
        for y in range(len(allSpeciesList)):
            if isinstance(allSpeciesList[xind][yind], str):
                temp.append(allSpeciesList[xind][yind])
            
            #   make sure that system will not come out of amount of columns
            if (xind < len(allSpeciesList)):    
                xind +=1

        #   reload attributes iterator
        xind = 0

        #   come to the next rule
        if (yind < len(allSpeciesList[0])-1):    
            yind +=1

        #   append orientir if there is one
        if len(temp) > 0:
            orientirs.append(temp)

    print('Orientirs created.')
```

The question generation system works quite simply: the program looks at the attributes of the rules and selects the option with the smallest number of answer options, thus filtering out the largest number of rules. The attribute acts as a question, and its values as answer options. A previously asked question (previously used attribute) cannot be applied again.

```python
#   function that picks question from remaining ones that has the least amount of possible variants
# and best of all separates types (ensures that system will take the least amount of questions
# to answer to the user). All possible conditions that are not matching with given answers are removed
def findMostFittingQuestion():
    #   index for listing questions with possible answers
    i = 0

    #   set a dictionary that will take orientirs and append them to keys
    allQualities = {}
    
    #   take all remaining orientirs for iteration
    for x in orientirs:
        allQualities.update({i: len(list(set(x)))})        
        i += 1
    
    #   find such question that has the least amount of possible variants
    lowest = 999999999999
    for x in allQualities.values():
        if x < lowest and x > 1:
            lowest = x

    return list(allQualities.keys())[list(allQualities.values()).index(lowest)]
```

### Interaction with user

The last piece of implementation is user interaction. After each successful answer or after starting the program, the system creates a set of landmarks. Analyzing it, the system generates a question for the user, giving answer options. The user answers the question, the system, based on the answer, removes already violated rules from the landmarks and leaves only those that are followed. Then, based on the remaining landmarks, the system generates the next question with subsequent answer options. The system will ask questions until there is only one answer left.

```python
#   user interface. This is the function for interation with user. 
def processDialog():
    print('Welcome to Akinator, Luna City edition!')
    print('Let me walk you through several questions about the person you want to identify.')

    #   perform iteration until error appears or user closes the program
    whileBool = True
    while whileBool == True:

        #   set orientirs to work with
        createOrientirs()
        print('Please select one of options by index. Does that person have...')

        #   give to the user such a question that has the least amount of variants (answers)
        optionIndex = findMostFittingQuestion()
        
        #   iterate through all variants of the given question to inform user
        printInd = 1
        printList = list(set(orientirs[optionIndex]))
        for x in printList:
            print(str(printInd)+'. '+x)
            printInd += 1
        
        #   listen for the user answer
        rawAnswer = input('<< ')
        redactedAnsw = printList[int(rawAnswer)-1]
        
        #   remove elements that do not match with the user answer
        removeFromAllSpecies(redactedAnsw)

        #   if there is only one answer (rule) remaining, then return as answer
        if len(allSpeciesList) <= 1:
            print('Your race is: '+speciesDict[allSpeciesList[0][-1]])
            whileBool = False
```

### Example of work with strict akinator

![Example of work with expert strict akinator system based on rules with "table" structure orientirs from Laboratory work nr. 1](https://github.com/filpatterson/python_fia_codes/blob/master/screenshot-3.PNG?raw=true)

# Laboratory work nr. 2

This laboratory work consisted in the creation of artificial intelligence of opponents in the game based on the behavior of the boids developed by Craig Reynolds. The principle of this behavior is based on the implementation of 3 simple laws below. For the game to work properly, it is also worth adding the player's ship pursuit rule.

**Important note**: the original code of the game is not attached due to the presence of a corser license, only the code written in the framework of laboratory work is attached here.

## Boid general description

Boid is a life simulation program written by Craig Reynolds to simulate bird behavior. A feature is not the task of the behavior algorithm for the entire flock, but for each subject (bird) based on a set of simple rules.

This behavior allows each part of the flock to be self-sufficient in terms of behavior and make this simulation realistic. Those simple rules are alignment, cohesion, and separation. For further simplicity each subject of the flock will be called a “bird”.

## Alignment

Alignment means that each bird will try to change its position or velocity to correspond to the medium velocity and medium direction of movement of either all birds in the flock or nearby birds. 

*alignment = sum(velocity) / n*

Alignment is the result of division of all velocities by the amount of birds. Alignment calculation can be applied either to all birds in the flock or to birds located nearby (best approach for nearby check: collect the data from birds located in a small rectangle around current bird). Alignment in the best case should be an acceleration vector that will be applied for smooth change of velocity for birds in the flock. The same moment about the acceleration vector is applicable to all laws of the flock behavior.
All laws applications in the current system are realized via velocity vectors, making movements of meteors a little abrupt.

## Cohesion

Cohesion means that each bird will try to change its position or velocity to move toward the center of the mass of either all birds or nearby birds.

*center_of_mass = sum(position) / n*

Conform formula center of mass is division for sum of all elements by amount of all elements. The problem is that cohesion estimates direction where the bird should move, but there is no estimation of how vector values should be calculated. Vector values for the bird are calculated conform formula:

*vector = (birdPosition - center_of_mass) / absolute_distance*

The vector can describe either acceleration or velocity for the bird. In the current system this is the velocity vector.

## Separation

Separation means that each bird will try to keep safe distance in order to evade collision with another bird in the flock. If previous laws can be calculated based on the data about all birds in the flock, this one can be calculated only for nearby birds. 

Conform visualization and description can be estimated that vector (velocity or acceleration) can be defined by the same principle as cohesion, but this is applied only to nearby birds and the vector will be reversed to move out from the center of mass for nearby birds to evade collision, meaning that only the last formula will be changed from cohesion formulas: 

*vector = (center_of_mass - birdPosition) / absolute_distance*

## Chasing ship

If aggressive behavior of meteors has been called then they must chase after a user’s ship. Task can be completed by using cohesion law, replacing the center of mass by coordinates of the ship.

## Code examples with explanations

```python
def update(self):
        self.vel = BoidBehavior.apply_all_flock_laws(self, rock_group, my_ship)
 
        for i in range(DIMENSIONS):
            self.pos[i] %= CANVAS_RES[i]
            self.pos[i] += self.vel[i]
 
        self.angle += self.angle_vel
        self.age += 1
 
        # return True if the sprite is old and needs to be destroyed
        if self.age < self.lifespan:
            return False
        else:
            return True
```

The first line of this method integrates the main part of the library (task of the second lab) ignoring part of switching behavior of meteors between aggressive one and passive one.

```python
    def start_being_chased(self, shoot):
        if shoot > 0:
            if self.is_chased:
                self.is_chased = False
            elif not self.is_chased:
                self.is_chased = True
 
            print(self.is_chased)
```

This part of code switches behavior of the meteors if “space” key has been pressed.

```python
class VectorsMath:
 
    #   get vector with sum of dimension elements
    @staticmethod
    def sum_of_vectors(first_vector, second_vector):
        resulting_vector = [0] * len(first_vector)
 
        #   iterate through each vector dimension
        for i in range(len(first_vector)):
            resulting_vector[i] = first_vector[i] + second_vector[i]
 
        return resulting_vector
 
    #   get vector with negation of dimension elements
    @staticmethod
    def negation_of_vectors(first_vector, second_vector):
        resulting_vector = [0] * len(first_vector)
        for i in range(len(first_vector)):
            resulting_vector[i] = first_vector[i] - second_vector[i]
 
        return resulting_vector
 
    #   get vector with multiplication of dimension elements
    @staticmethod
    def multiplication_of_vectors(first_vector, second_vector):
        resulting_vector = [0] * len(first_vector)
        for i in range(len(first_vector)):
            resulting_vector[i] = first_vector[i] * second_vector[i]
 
        return resulting_vector
 
    #   get vector with division of dimension elements by value
    @staticmethod
    def dividing_vector_by_value(vector, value):
        if value == 0:
            return vector
 
        resulting_vector = [0] * len(vector)
        for i in range(len(vector)):
            resulting_vector[i] = vector[i] / value
 
        return resulting_vector
 
    #   get vector with multiplication of dimension elements by value
    @staticmethod
    def multiply_vector_by_value(vector, value):
        resulting_vector = [0] * len(vector)
        for i in range(len(vector)):
            resulting_vector[i] = vector[i] * value
 
        return resulting_vector
```

All arithmetic operations have commentaries defining what each method does and all variables contain clear names that show what operations over what data is performed. All methods are set as static for evading the need of creating objects of this type.

```python
class PointMath:
 
    #   transform angle to the vector
    @staticmethod
    def angle_to_vector(ang):
        return [math.cos(ang), math.sin(ang)]
 
    #   get distance between two points
    @staticmethod
    def distance(first_point, second_point):
        return math.sqrt((first_point[0] - second_point[0]) ** 2 + (first_point[1] - second_point[1]) ** 2)
```

This is a very small class considering that the amount of required operations for making boids behavior is small.

```python
class BoidBehavior:
    #   define center of mass for all boids and move boid to this center
    @staticmethod
    def cohesion(boid: Sprite, boids_group: set[Sprite]):
        #   if there is less than two boids then do not work
        if len(boids_group) < 2:
            return 0
 
        #   init array for center of mass
        center_of_mass = [0] * len(boid.pos)
        total = 0
 
        #   iterate through all boids
        for anotherBoid in boids_group:
            #   accumulate positions to find center of mass and count boids
            center_of_mass = VectorsMath.sum_of_vectors(center_of_mass, anotherBoid.pos)
            total += 1
 
        #   if amount of boids is bigger than one boid
        if total > 1:
            #   find arithmetical average of all positions
            center_of_mass = VectorsMath.dividing_vector_by_value(center_of_mass, total)
 
            #   find difference of coordinates between center of mass and current boid
            differential_coordinate = VectorsMath.negation_of_vectors(center_of_mass, boid.pos)
 
            #   transform difference of coordinates into velocity vector
            differential_coordinate = VectorsMath.dividing_vector_by_value(
                differential_coordinate, PointMath.distance(center_of_mass, boid.pos)
            )
 
            #   normalize values of the vector to be applicable
            differential_coordinate = BoidBehavior.normalize_velocity_vector(differential_coordinate)
            return differential_coordinate
        #   if there is only one boid or none, then there is nothing to change
        else:
            return 0
 
    #   return vector for chasing ship
    @staticmethod
    def chase(boid: Sprite, ship_to_be_chased: Ship):
        #   define difference of coordinates between boid and ship
        differential_coordinate = VectorsMath.negation_of_vectors(ship_to_be_chased.pos, boid.pos)
 
        #   transform difference of coordinates into velocity vector
        differential_coordinate = VectorsMath.dividing_vector_by_value(
            differential_coordinate, PointMath.distance(ship_to_be_chased.pos, boid.pos) / 1.5
        )
 
        #   normalize velocity vector to be applicable
        differential_coordinate = BoidBehavior.normalize_velocity_vector(differential_coordinate)
        return differential_coordinate
 
    #   return vector for pushing away from boids (keeping minimal possible distance)
    @staticmethod
    def separation(boid: Sprite, boids_group: set[Sprite]):
        #   if there is less than two boids then do not make calculation
        if len(boids_group) < 2:
            return 0
 
        #   init vector for movement
        avg_counter_movement = [0] * len(boid.pos)
        total = 0
 
        #   iterate through all boids
        for another_boid in boids_group:
            #   find distance between boid and boid for list of all boids
            distance = PointMath.distance(boid.pos, another_boid.pos)
 
            #   if distance is less than 3 radii
            if distance < boid.get_radius() * 3:
                #   algorithm is similar to the "chase" principle
                differential_coordinate = VectorsMath.negation_of_vectors(boid.pos, another_boid.pos)
                differential_coordinate = VectorsMath.dividing_vector_by_value(differential_coordinate, distance / 6)
                avg_counter_movement = VectorsMath.sum_of_vectors(avg_counter_movement, differential_coordinate)
                total += 1
 
        if total > 1:
            avg_counter_movement = VectorsMath.dividing_vector_by_value(avg_counter_movement, total)
            return avg_counter_movement
        else:
            return 0
 
    #   return average velocity vector of all movement vectors of all boids
    @staticmethod
    def align(boid: Sprite, boids_group: set[Sprite]):
        if len(boids_group) < 2:
            return 0
        avg_movement = [0] * len(boid.pos)
        total = 0
 
        for another_boid in boids_group:
            #   accumulate all velocity vectors
            avg_movement = VectorsMath.sum_of_vectors(avg_movement, another_boid.vel)
            total += 1
 
        if total > 1:
            avg_movement = VectorsMath.dividing_vector_by_value(avg_movement, total)
            return avg_movement
        else:
            return 0
 
    #   normalize velocity vector to be applicable to the simulation
    @staticmethod
    def normalize_velocity_vector(vector: set[int]):
        for i in range(len(vector)):
            if vector[i] > 1:
                vector[i] = 1
            elif vector[i] < -1:
                vector[i] = -1
 
        return vector
 
    #   define all vectors for alignment, separation, cohesion, chase, then apply them to the velocity
    @staticmethod
    def apply_all_flock_laws(boid: Sprite, boids_group: set[Sprite], ship_to_be_chased: Ship):
        #   initialize vector for accumulating flock changes
        applied_velocity = [0] * len(boid.vel)
 
        #   calculate all flock movement vectors
        cohesion_velocity = BoidBehavior.cohesion(boid, boids_group)
        separation_velocity = BoidBehavior.separation(boid, boids_group)
        align_velocity = BoidBehavior.align(boid, boids_group)
 
        #   accumulate all flock movement vectors
        if cohesion_velocity != 0:
            applied_velocity = VectorsMath.sum_of_vectors(applied_velocity, cohesion_velocity)
        if separation_velocity != 0:
            applied_velocity = VectorsMath.sum_of_vectors(applied_velocity, separation_velocity)
        if align_velocity != 0:
            applied_velocity = VectorsMath.sum_of_vectors(applied_velocity, align_velocity)
        if ship_to_be_chased.is_chased:
            chasing_velocity = BoidBehavior.chase(boid, ship_to_be_chased)
            if chasing_velocity != 0:
                applied_velocity = VectorsMath.sum_of_vectors(applied_velocity, chasing_velocity)
 
        #   apply flock movement vectors to the movement vector
        boid.vel = VectorsMath.sum_of_vectors(boid.vel, applied_velocity)
 
        #   normalize velocity and round it to the least possible step
        boid.vel = BoidBehavior.normalize_velocity_vector(boid.vel)
        for i in range(len(boid.vel)):
            boid.vel[i] = round(boid.vel[i], 3)
 
        return boid.vel
```

All code is commented almost for every line in order to make clear what program does and to show how calculations work. Class implements all three laws of the boid and additional law for chasing ship conform task of the laboratory work.

## Example of how to launch code and how it works

Code is written to work using Code Skulptor 3. 

![Example of work of the game with implemented patters for laboratory work nr. 2](https://github.com/filpatterson/python_fia_codes/blob/master/lab_2_game_record.gif?raw=true)