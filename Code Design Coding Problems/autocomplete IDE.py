# autocomplete IDE
def AutoCompleteIDE(input, classes):
    results = []
    
    for className in classes:
        inputIndex = 0
        classIndex = 0
        while classIndex < len(className):
            if inputIndex == len(input):
                results.append(className)
                break
            
            if input[inputIndex] == className[classIndex]:
                inputIndex += 1
            elif input[inputIndex].islower() and input[inputIndex] != className[classIndex]:
                break
            
            classIndex += 1
    
    return results

classes = ["Container","Panel","AutoPanel","RidePrinter","ResumePanel","RegularContainer"]
print(AutoCompleteIDE("R", classes))
print(AutoCompleteIDE("Re", classes))
print(AutoCompleteIDE("RP", classes))
print(AutoCompleteIDE("RPr", classes))