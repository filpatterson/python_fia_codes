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

    def show_info(self):
        print("Here is a person with " + self.hair + " hair, " + self.eyes + " eyes, " + self.headshape + " head shape, " +
              self.height + " height, " + self.mouthSize + " mouth size, " + self.language + " is language that person speaks, " + 
              self.skinColor + " skin of color")
        
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