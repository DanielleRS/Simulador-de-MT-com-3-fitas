
class TuringMachine:
    
    def __init__(self, transitions, initial, finals):
        self.D = 0
        self.E = 1
        self.I = 2
        self.INICIO = '<'
        self.BRANCO = ' '
        self.finals = finals
        self.transitions = transitions
        self.initial = initial
        
    def processWord(self, word):
        
        state = self.initial
        
        tape1 = [self.INICIO]
        tape2 = [self.INICIO]
        tape3 = [self.INICIO]
        
        for symbol in word:
            tape1.append(symbol)
        
        tape1pos = 1
        tape2pos = 1
        tape3pos = 1
        
        stopComputing = False
        
        while not stopComputing:
            
            symbol1 = tape1[tape1pos] if tape1pos < len(tape1) else self.BRANCO
            symbol2 = tape2[tape2pos] if tape2pos < len(tape2) else self.BRANCO
            symbol3 = tape3[tape3pos] if tape3pos < len(tape3) else self.BRANCO
            
            print("Estado " + str(state))
            print("Fita 1: " + str(tape1))
            print("\t cabecote na posicao " + str(tape1pos)) 
            print("Fita 2: " + str(tape2))
            print("\t cabecote na posicao " + str(tape2pos))
            print("Fita 3: " + str(tape3))
            print("\t cabecote na posicao " + str(tape3pos) + "\n")
            
            if (state, symbol1, symbol2, symbol3) in self.transitions:
                newState, newSymbol1, newSymbol2, newSymbol3, direction1, direction2, direction3 = self.transitions[(state, symbol1, symbol2, symbol3)]
                state = newState
                
                if tape1pos < len(tape1):
                    tape1[tape1pos] = newSymbol1
                else:
                    tape1.append(newSymbol1)
                    
                if tape2pos < len(tape2):
                    tape2[tape2pos] = newSymbol2
                else:
                    tape2.append(newSymbol2)
                    
                if tape3pos < len(tape3):
                    tape3[tape3pos] = newSymbol3
                else:
                    tape3.append(newSymbol3)
                
                tape1pos = tape1pos - 1 if direction1 == self.E else (tape1pos + 1 if direction1 == self.D else tape1pos)
                tape2pos = tape2pos - 1 if direction2 == self.E else (tape2pos + 1 if direction2 == self.D else tape2pos)
                tape3pos = tape3pos - 1 if direction3 == self.E else (tape3pos + 1 if direction3 == self.D else tape3pos)
            else:
                stopComputing = True
        
        return True if state in self.finals else False
