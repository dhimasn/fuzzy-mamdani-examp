def main():
    
    #input nilai neukritisme
    rawScoreNeuroticism = float(input("Enter Score of neuroticism"))
    #input nilai exkrotivime
    rawScoreExtroversion = float(input("Enter Score of extroversion"))
    
    rules = evaluateRules(rawScoreNeuroticism, rawScoreExtroversion)    
   
    print(rules)

def trapmfNeu(x, points):
    pointA = points[0]
    pointB = points[1]
    pointC = points[2]
    pointD = points[3]
    if x <= pointA:
        result = 'SB1'
    if x > pointA and x <= pointB:
        result = 'SB2'
    elif x > pointB and x <= pointC:
        result = 'SB3'
    elif x > pointC and x < pointD:
        result = 'SB4'
    return result

def trapmfExt(x, points):
    pointA = points[0]
    pointB = points[1]
    pointC = points[2]
    pointD = points[3]
    if x <= pointA:
        result = 'SD1'
    if x > pointA and x <= pointB:
        result = 'SD2'
    elif x > pointB and x <= pointC:
        result = 'SD3'
    elif x > pointC and x < pointD:
        result = 'SD4'
    return result

def defuzzyNeuExtro(N, E, points):
    pointA = points[0]
    pointB = points[1]
    pointC = points[2]
    pointD = points[3]
    avgNe = (N + E)/2
    if avgNe <= pointA:
        result = 'L'
    if  avgNe > pointA and avgNe <= pointB:
        result = 'M'
    elif avgNe > pointB and avgNe <= pointC:
        result = 'H'
    elif avgNe > pointC and avgNe < pointD:
        result = 'E'
    return result
    
    
def evaluateRules(rawScoreNeuroticism, rawScoreExtroversion):
    
    def fuzzyNeukritisme(rawScoreNeuroticism):
         return trapmfNeu(rawScoreNeuroticism, [45, 47, 49, 51])
    
    def fuzzyExtrotivisme(rawScoreExtroversion):
         return trapmfExt(rawScoreExtroversion, [40, 43, 47, 50])

    def fuzzySetanxietyRules(rawScoreNeuroticism, rawScoreExtroversion, classNeukr, classExtro):
         return defuzzyNeuExtro(rawScoreNeuroticism, rawScoreExtroversion ,[0, 20, 40, 60])
    
    print ("class Neuroticism %d class Extro %d Level of Anxiety %d", (fuzzyNeukritisme, fuzzyExtrotivisme, fuzzySetanxietyRules))
     

if __name__ == "__main__":
    main()
