import numpy as np, matplotlib.pyplot as plt, random

#This program is done to test Algo
# h1 = huristic funcitons (count the number of attacking queens for 8 queen problem)
class play:

    def __init__(self):
        self.box = np.zeros((8,8))                      #will stores the main box elements data
        self.queen_pos = [0 for x in range(8)]          #will store the queen postion for every random_assignment
        self.huristic_score = 0                         #will store the huristic_score
        self.temp_alloc = np.zeros((8,8))               #will store the temporary data to calculate the huristic_score
        self.test_matrix = np.array([]) # --h1()--  used as a test matrix
        self.attacking_paris = []       # --h1()--  used to store the attacking pairs

    def random_assignment(self):
        for i in range(8):  #generating 8 random number between 0-7 for placing queens
            self.queen_pos[i] = random.randint(0,7)
        for i in range(8):  #Placing queens
            self.box[i][self.queen_pos[i]] = 1

    def temp_alloc_reset(self):
        self.temp_alloc = np.zeros((8,8))

    def marking_territories(self, pos): #used to mark 1 in self.temp_alloc for the places where queen with pos can attack
        self.temp_alloc_reset()
        for i in range(8):
            self.temp_alloc[pos[0]][i] = 1
            self.temp_alloc[i][pos[1]] = 1
        if(pos[0]-pos[1]>=0):   #diagonal 1
            for i in range(8):
                if(pos[0]-pos[1]+i<8):
                    self.temp_alloc[pos[0]-pos[1]+i, i] = 1
        elif(pos[0]-pos[1]<0):
            for i in range(8):
                if(pos[1]-pos[0]+i<8):
                    self.temp_alloc[i, pos[1]-pos[0]+i] = 1
        if(pos[0]+pos[1]<8): #diagonal 2
            for i in range(8):
                if(pos[0]+pos[1]-i>=0):
                    self.temp_alloc[i, pos[0]+pos[1]-i] = 1
        if(pos[0]+pos[1]>=8):
            for i in range(8):
                if(pos[0]+pos[1]-(8-1)+i<8 and (8-1-i)>=0):
                    self.temp_alloc[pos[0]+pos[1]-(8-1)+i, 8-1-i] = 1


    def h1(self):   # Huristic cost function to return numbers of attacking pairs
        self.__init__()
        self.random_assignment()
        for i in range(8):
            self.marking_territories([i,self.queen_pos[i]])
            self.test_matrix = self.box + self.temp_alloc
            #print()
            #print(self.test_matrix)
            for j in range(8):
                for k in range(8):
                    if(self.test_matrix[j][k] == 2  ):
                        self.attacking_paris.append([i,j])
            #print(self.attacking_paris)
            #print()
        #print(self.attacking_paris)
        self.huristic_score = (self.attacking_paris.__len__() - 8)//2
        print("Data :" + str(self.huristic_score) + " with :" + str(self.queen_pos))

    def __repr__(self):                 #will help to print huristic_score when the opject is made to print
        return "Huristic Value :" + str(self.huristic_score)

    def h1_docs(self):                  #try n number of random combination and will tell the minimum huristic_score
        self.random_assignment()
        self.h1()
        min = self.huristic_score
        min_data = self.queen_pos
        for i in range(10000):
            #print(i)
            self.random_assignment()
            self.h1()
            if(self.huristic_score < min):
                min = self.huristic_score
                min_data = self.queen_pos
            else:
                pass
        print("We found the Minumum is Archived at :" + str(min) + " with :" + str(min_data))





a = play();
a.random_assignment()
a.queen_pos
a.h1_docs()
