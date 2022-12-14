#Written by Sanjana Kolisetty
#Question 2 - The 8 puzzle problem
#Code File - Question2_210101093.py
#Terminal Command to run the file - python3 Question2_210101093.py
#Input - Enter the initial and final configuration in the form of a 3x3 matrix
#        with the empty space or blank as zero
#Output - If the problem is not solvable, the programme will print "Not Possible", otherwise, it'll print all the steps 
#         if the problem is solvable in less than 10 steps, otherwise it'll print the first 10 steps and will print 
#         "The given problem can be solved but will require more than 10 steps.".

#First, I defined a swap function which is used to swap the empty tile with any of the possible other tiles.
#It takes initial configuration and the coordinates of the tiles to be swapped.

#I've imported a python library to store the updated initial configuration and later when we swap and if we get the same configuration then we
#reverse the swap and then do a new swap. Otherwise, we store the configuration and we continue.  
import copy
already = []

def swap(init_config,i,j,a,b):
      temp = init_config[i][j]
      init_config[i][j] = init_config[a][b]
      init_config[a][b] = temp

#This function is used to find out the tile with which the empty tile is to be swapped in order to reach the final configuration.
#Here we initially, find out the coordinates of the empty tile and then, check if the initial configuration is equal to the final 
#final configuration, if that's the case, then, number of misplaced tiles will be equal to zero, then the function returns and prints the final 
#configuration. Otherwise, depending on the position of the empty tile, we have eithere two, or three or four choices to move it
#We swap to the one in which the current the position of the empty tile is where the tile with which the empty tile is to be swapped should
#be. If such a tile doesn't exist then, we have defined certain swaps, later in the function. The return value of this function is
#the updated value of the number of misplaced tiles.

#If the empty tile is in one of the corners, it can move to either it's left or right and above or below, having two choices
#If the empty tile is in the middle of the first or third row or in the middle of the first or the third column, then it has three 
#choices
#Else, it can be at the center, having four choices, i.e, left, right, above and below.

def possible(init_config, final_config, misplaced):
      #Finding the coordinates of the empty tile represented by '0'
      for i in range(0,3):
            for j in range(0,3):
                  if(init_config[i][j]==0):
                        x = i
                        y = j
                        break
      if(init_config == final_config):
            return 0 #If the initial and final configuration are the same, the function returns
      else:
            if(x == 0):
                  if(init_config[1][y] == final_config[0][y]): #Checking if the tile to be swapped is the one that should be
                    #in the current empty tile's place
                        swap(init_config,1,y,0,y) #If that's the case, it is swapped and we check again if the initial and configuration
                        #are same, else, because of the swap the number of misplaced tiles reduce by 1
                        if(init_config in already):
                              swap(init_config,1,y,0,y)
                              if(y > 0):
                                    swap(init_config,1,y,0,y-1)
                                    already.append(copy.deepcopy(init_config)) #we are using deep copy because we don't want the copy of the current initial configuration 
                                    #to change if we change initial configuration later. 
                              else:
                                    swap(init_config,1,y,0,y+1)
                                    already.append(copy.deepcopy(init_config))
                        else:
                              already.append(copy.deepcopy(init_config))
                              if(init_config == final_config):
                                    return 0
                              else:
                                    misplaced = misplaced-1
                        return  misplaced
            #We follow a similar procedure and check if the tile to be swapped needs to be there, if it satisfies, then swap it
            #otherwise, check other possible swaps
            elif(x == 1):
                  if(init_config[2][y] == final_config[1][y]):
                        swap(init_config,2,y,1,y)
                        if(init_config in already):
                              swap(init_config,2,y,1,y)
                              if(y > 0):
                                    swap(init_config,1,y,0,y-1)
                                    already.append(copy.deepcopy(init_config))
                              else:
                                    swap(init_config,1,y,0,y+1)
                                    already.append(copy.deepcopy(init_config))
                        else:
                              already.append(copy.deepcopy(init_config))
                              if(init_config == final_config):
                                    return 0
                              else:
                                    misplaced = misplaced-1
                        return  misplaced
                  elif(init_config[0][y] == final_config[1][y]):
                        swap(init_config,0,y,1,y)
                        if(init_config in already):
                              swap(init_config,0,y,1,y)
                              if(y > 0):
                                    swap(init_config,1,y,0,y-1)
                                    already.append(copy.deepcopy(init_config))
                              else:
                                    swap(init_config,1,y,0,y+1)
                                    already.append(copy.deepcopy(init_config))
                        else:
                              already.append(copy.deepcopy(init_config))
                              if(init_config == final_config):
                                    return 0
                              else:
                                    misplaced = misplaced-1
                        return  misplaced
            elif(x == 2):
                  if(init_config[1][y] == final_config[2][y]):
                        swap(init_config,1,y,2,y)
                        if(init_config in already):
                              swap(init_config,1,y,2,y)
                              if(y > 0):
                                    swap(init_config,1,y,0,y-1)
                                    already.append(copy.deepcopy(init_config))
                              else:
                                    swap(init_config,1,y,0,y+1)
                                    already.append(copy.deepcopy(init_config))
                        else:
                              already.append(copy.deepcopy(init_config))
                              if(init_config == final_config):
                                    return 0
                              else:
                                    misplaced = misplaced-1
                        return  misplaced
            if(y == 0):
                  if(init_config[x][1] == final_config[x][0]):
                        swap(init_config,x,1,x,0)
                        if(init_config in already):
                              swap(init_config,x,1,x,0)
                              if(x > 0):
                                    swap(init_config,1,x,0,x-1)
                                    already.append(copy.deepcopy(init_config))
                              else:
                                    swap(init_config,1,x,0,x+1)
                                    already.append(copy.deepcopy(init_config))
                        else:
                              already.append(copy.deepcopy(init_config))
                              if(init_config == final_config):
                                    return 0
                              else:
                                    misplaced = misplaced-1
                        return  misplaced
            elif(y == 1):
                  if(init_config[x][2] == final_config[x][1]):
                        swap(init_config,x,2,x,1)
                        if(init_config in already):
                              swap(init_config,x,2,x,1)
                              if(x > 0):
                                    swap(init_config,1,x,0,x-1)
                                    already.append(copy.deepcopy(init_config))
                              else:
                                    swap(init_config,1,x,0,x+1)
                                    already.append(copy.deepcopy(init_config))
                        else:
                              already.append(copy.deepcopy(init_config))
                              if(init_config == final_config):
                                    return 0
                              else:
                                    misplaced = misplaced-1
                        return  misplaced
                  elif(init_config[x][0] == final_config[x][1]):
                        swap(init_config,x,0,x,1)
                        if(init_config in already):
                              swap(init_config,x,1,x,0)
                              if(x > 0):
                                    swap(init_config,1,x,0,x-1)
                                    already.append(copy.deepcopy(init_config))
                              else:
                                    swap(init_config,1,x,0,x+1)
                                    already.append(copy.deepcopy(init_config))
                        else:
                              already.append(copy.deepcopy(init_config))
                              if(init_config == final_config):
                                    return 0
                              else:
                                    misplaced = misplaced-1
                        return  misplaced
            elif(y == 2):
                  if(init_config[x][1] == final_config[x][2]):
                        swap(init_config,x,1,x,2)
                        if(init_config in already):
                              swap(init_config,x,1,x,2)
                              if(x > 0):
                                    swap(init_config,1,x,0,x-1)
                                    already.append(copy.deepcopy(init_config))
                              else:
                                    swap(init_config,1,x,0,x+1)
                                    already.append(copy.deepcopy(init_config))
                        else:
                              already.append(copy.deepcopy(init_config))
                              if(init_config == final_config):
                                    return 0
                              else:
                                    misplaced = misplaced-1
                        return  misplaced
            #If none of the tiles that can be swapped with the empty tile is the one that needs to be there in the position of the
            #empty tile in the final configuration, then, we have defined a set of default swaps.
            if(x < 2 and init_config[x+1][y] != final_config[x+1][y]):
                  swap(init_config,x,y,x+1,y)
                  already.append(copy.deepcopy(init_config))
            elif(x > 0 and init_config[x-1][y] != final_config[x-1][y]):
                  swap(init_config,x,y,x-1,y)
                  already.append(copy.deepcopy(init_config))
            elif(y < 2 and init_config[x][y+1] != final_config[x][y+1]):
                  swap(x,y,x,y+1)
                  already.append(copy.deepcopy(init_config))
            elif (y > 0 and init_config[x][y] != final_config[x][y-1]):
                  swap(x,y,x,y-1)
                  already.append(copy.deepcopy(init_config))
            elif(x < 2):
                  swap(init_config,x,y,x+1,y)
                  already.append(copy.deepcopy(init_config))
            else:
                 swap(init_config,x,y,x-1,y) 
                 already.append(copy.deepcopy(init_config))       
            return  misplaced

#So, the programme starts here.
# First, I created two 2D lists to store the initial and final configuration.                 

print("Enter the initial Configuration: -") #Printing the required statement to take the input
init_config = [list(map(int,input().split())) for i in range(3)]

print(" ")

#Similarly, I took the final configuration input
print("Enter the final Configuration: -")
final_config = [list(map(int,input().split())) for i in range(3)]

#Then I created two 1D lists, one taking the intial and the other taking the final configuration in the form a 1D list to calculate the inversion count.
p = []
q = []

#I have created two variable to check the inversion count in order to determine if the problem can be solved or not.
count1 = 0
count2 = 0
print("")

#Here we are taking p as the initial configuration and q as the final configuration with two for loops.
for i in range(0,3):
      for j in range(0,3):
            p.append(init_config[i][j])
            q.append( final_config[i][j])

#Here we are calculating the inversion count for both the initial and final configuration.
for i in range (0,8):
      for j in range (i+1,9):
            if(p[j] > p[i] and p[i] != 0):
                  count1 = count1 + 1
            if(q[j] > q[i] and q[i] != 0):
                  count2 = count2 + 1

#Only if the inversion counts of the initial and final configuration are of the same parity, we can solve the problem.
#So, if that condition is not satisfying, the programme prints "Not Possible".

if (count1%2) != (count2%2):
      print("Not Possible ")
else:
       #If the problem is solvable, we first calculate the number of misplaced tiles
       misplaced = 0
       for i in range(0,3):
            for j in range(0,3):
                  if(init_config[i][j] != final_config[i][j]):
                         misplaced = misplaced + 1
        
        #If the number of misplaced tiles equal to 0, then it means initial and final configuration are same and the
        #programme prints that 0 steps are required.
       if( misplaced == 0):
            print("The number of steps required are 0")
            print("Done")
       else:
            #Otherwise, we create a boolean variable and equate it to 'False'. It will be changed to 'True', if the problem 
            #is solved within 10 steps, otherwise, it'll print that the problem can be solved but in more than 10 steps.
            done = False

            #Here, we print the initial configuration first.
            print("Initial Configuration")
            print(" ")
            for i in range(0,3):
                  print(init_config[i][0]," ",init_config[i][1]," ",init_config[i][2])
            print(" ")

            #Since we are told to iterate 10 times, we run a while loop 10 times, where we execute possible function.
            n = 10  
            while(n != 0):
                  n = n-1
                  misplaced = possible(init_config, final_config, misplaced) #Everytime, we execute the possible function.
                  #we print the changed initial configuration
                  for i in range(0,3):
                        print(init_config[i][0]," ",init_config[i][1]," ",init_config[i][2])
                  print("")
                  #If the misplaced becomes 0 at any time, it means we have reached the final configuration, so we print it and then 
                  #print the number of steps taken to reach there
                  if( misplaced == 0):
                        print("Final Configuration")
                        print("")
                        print("The number of steps required are", 10-n)
                        print("Done")
                        done = True
                        break
            #If the problem couldn't be solved within the 10 steps, then we print that it can be solved but will take more than 10 steps.
            if done == False:
                  print("The given problem can be solved but will require more than 10 steps.")