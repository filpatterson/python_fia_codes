#   Here is representation of data that will be given to the system. All the data
# is structured in the table where column represents attribute field and rows
# represent rules.
#   For correct understanding below is also represented "table" and how it looks like
orientirs = []
race1 = ['nose',    'common skin',  'common eyes',    'common body',  'common hair',  0]
race2 = ['nose',    'common skin',  'red eyes',       'tall body',    'red hair',     1]
race3 = ['gills',   'scaly skin',   'wide eyes',      'low body',     'n/a hair',     2]
race4 = ['nose',    'scaly skin',   'dark eyes',      'common body',  'dark hair',    3]
race5 = ['nose',    'common skin',  'offended eyes',  'common body',  'common hair',  4]
race6 = ['nose',    'common skin',  'common eyes',    'common body',  'white hair',   5]

#  |--------------------------------------------------------------------------------------------------------------
#  |nr|  Name        |   Respiratory system   |   Skin       |   Eyes            |   Body type   |   Hair        |
#  |--------------------------------------------------------------------------------------------------------------
#  |1.|  dirts       |   nose                 |  common skin |   common eyes     |   common body |   common hair |
#  |2.|  marsmen     |   nose                 |  common skin |   red eyes        |   tall body   |   red hair    |
#  |3.|  neptunes    |   gills                |  scaly skin  |   wide eyes       |   low body    |   n/a hair    |
#  |4.|  jews        |   nose                 |  scaly skin  |   dark eyes       |   common body |   dark hair   |
#  |5.|  tolerants   |   nose                 |  common skin |   offended eyes   |   common body |   common hair |
#  |6.|  lunies      |   nose                 |  common skin |   common eyes     |   common body |   white hair  |
#  ---------------------------------------------------------------------------------------------------------------


#   define list of all rules and append all rules to that list
allSpeciesList=[]
allSpeciesList.append(race1)
allSpeciesList.append(race2)
allSpeciesList.append(race3)
allSpeciesList.append(race4)
allSpeciesList.append(race5)
allSpeciesList.append(race6)

#   set dictionary, where index appended to the rule sets key and string represents answer of the system
# conform that rule
speciesDict = {
  race1[-1]: "dirts",
  race2[-1]: "marsmen",
  race3[-1]: "neptunes",
  race4[-1]: "jews",
  race5[-1]: "tolerasts",
  race6[-1]: "lunies"
}

#   remove elements (conditions) that are not matching with user answer
def removeFromAllSpecies(redactedAnsw):
    for x in allSpeciesList:
        if redactedAnsw not in x:
            allSpeciesList.remove(x)
    for x in allSpeciesList:
        if redactedAnsw not in x:
            removeFromAllSpecies(redactedAnsw)

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

#   program launch
processDialog()