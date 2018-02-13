Foundations of Intelligent Systems
Project 1

SANDHYA MURLI (sm2290@g.rit.edu)
ROHAN SHIROOR (rss1103@g.rit.edu)

----------------------------------------------------------------------------------
Files in this directory:

rdmaze.py:  The python file which consists of the code for rolling die mazes.
README.txt: README file
----------------------------------------------------------------------------------
Steps to Run the code:

1. Extract zip file
1. OPEN cmd (or terminal if Linux or MAC OSX)
2. GO to the path where the folder is saved
3. RUN command: python rdmaze.py
4. Give input of puzzle text file.

OUTPUT INTERPRETATION:

1) The initial state of the maze as read from text file.

S . . . G 
. . . . . 

------------------------

2) The program run for Euclidean distance heuristic.

For Heuristics : Eucledian Distance


3) Goal state was found 

GOAL FOUND!!!

4) The path from start node (S) to the goal node of the maze (G).

the path is :

5) Each point selected in the path

Iteration :

6) The point selected in the path to the goal state (x and y coordinate)  

point selected :  [0, 0]

7) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
. . . . .

8) The orientation of the die at the start state. 

dice orientation :

east : 3
west : 4
north : 2
south : 5
top : 1
bottom : 6

------------------------

9) Each point selected in the path

Iteration :

10) The point selected in the path to the goal state (x and y coordinate)

point selected :  [1, 0]

11) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ . . . . 

12) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 3
west : 4
north : 6
south : 1
top : 2
bottom : 5

------------------------

13)Each point selected in the path

Iteration :

14) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [1, 1]

15) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ ~ . . . 

16) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 2
west : 5
north : 6
south : 1
top : 4
bottom : 3


------------------------

17) Each point selected in the path

Iteration :

18) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [1, 2]

19) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ ~ ~ . . 

20) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 4
west : 3
north : 6
south : 1
top : 5
bottom : 2


------------------------

21) Each point selected in the path

Iteration :

22) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [1, 3]

23) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ ~ ~ ~ . 

24) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 5
west : 2
north : 6
south : 1
top : 3
bottom : 4

------------------------

25) Each point selected in the path

Iteration :

26) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [1, 4]

27) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ ~ ~ ~ ~ 

28) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 3
west : 4
north : 6
south : 1
top : 2
bottom : 5

------------------------

29) Each point selected in the path

Iteration :

30) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [0, 4]

31) The state of the maze after reaching the goal state.

~ . . . ~ 
~ ~ ~ ~ ~ 

32) The orientation of the die after moving to the goal state.

dice orientation :

east : 3
west : 4
north : 2
south : 5
top : 1
bottom : 6

33) The total path from the start to goal state along with the Nodes generated, nodes visisted and the number of nodes in solution.

Total path is :  [[0, 0], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [0, 4]]
Nodes Generated :  22
Nodes visited :  15
Number of moves in the Solution :  7

34) The program run for Euclidean distance heuristic.

-----------------------------------
For Heuristics : Manhatten Distance

35) Goal state was found 

GOAL FOUND!!!

36) The path from start node (S) to the goal node of the maze (G).

the path is :

37) Each point selected in the path

Iteration :

38) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [0, 0]

39) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
. . . . . 

40) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 3
west : 4
north : 2
south : 5
top : 1
bottom : 6

------------------------

41) Each point selected in the path

Iteration :

42) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [1, 0]

43) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ . . . . 

44) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 3
west : 4
north : 6
south : 1
top : 2
bottom : 5

------------------------

45) Each point selected in the path

Iteration :

46) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [1, 1]

47) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ ~ . . . 

48) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 2
west : 5
north : 6
south : 1
top : 4
bottom : 3

------------------------

49) Each point selected in the path

Iteration :

50) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [1, 2]

51) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ ~ ~ . . 

52) The state of the maze after the point is selected. ~ represents the current point that was selected.

dice orientation :

east : 4
west : 3
north : 6
south : 1
top : 5
bottom : 2

------------------------

53) Each point selected in the path

Iteration :

54) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [1, 3]

55) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ ~ ~ ~ . 

56) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 5
west : 2
north : 6
south : 1
top : 3
bottom : 4

------------------------

57) Each point selected in the path

Iteration :

58) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [1, 4]

59) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ ~ ~ ~ ~ 

60) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 3
west : 4
north : 6
south : 1
top : 2
bottom : 5

------------------------

61) Each point selected in the path

Iteration :

62) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [0, 4]

63) The state of the maze after reaching the goal state.

~ . . . ~ 
~ ~ ~ ~ ~ 

64) The orientation of the die after moving to the goal state.

dice orientation :

east : 3
west : 4
north : 2
south : 5
top : 1
bottom : 6

65) The total path from the start to goal state along with the Nodes generated, nodes visisted and the number of nodes in solution.

Total path is :  [[0, 0], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [0, 4]]
Nodes Generated :  22
Nodes visited :  15
Number of moves in the Solution :  7

66) The program run for Diagonal distance heuristic.

-----------------------------------
For Heuristics : Diagonal Distance

67) Goal state was found 

GOAL FOUND!!!

68) The path from start node (S) to the goal node of the maze (G).

the path is :

69) Each point selected in the path

Iteration :

70) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [0, 0]

71) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
. . . . . 

72) The state of the maze after the point is selected. ~ represents the current point that was selected.

dice orientation :

east : 3
west : 4
north : 2
south : 5
top : 1
bottom : 6

------------------------

73) Each point selected in the path

Iteration :

74) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [1, 0]

75) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ . . . . 

76) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 3
west : 4
north : 6
south : 1
top : 2
bottom : 5

------------------------

77) Each point selected in the path

Iteration :

78) The point selected in the path to the goal state (x and y coordinate)

point selected :  [1, 1]

79) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ ~ . . . 

80) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 2
west : 5
north : 6
south : 1
top : 4
bottom : 3

------------------------

81) Each point selected in the path

Iteration :

82) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [1, 2]

83) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ ~ ~ . . 

84) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 4
west : 3
north : 6
south : 1
top : 5
bottom : 2

------------------------

85) Each point selected in the path

Iteration :

86) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [1, 3]

87) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ ~ ~ ~ . 

88) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 5
west : 2
north : 6
south : 1
top : 3
bottom : 4

------------------------

89) Each point selected in the path

Iteration :

90) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [1, 4]

91) The state of the maze after the point is selected. ~ represents the current point that was selected.

~ . . . G 
~ ~ ~ ~ ~ 

92) The orientation of the die after moving to the new state in the path to the goal state.

dice orientation :

east : 3
west : 4
north : 6
south : 1
top : 2
bottom : 5

------------------------

93) Each point selected in the path

Iteration :

94) The point selected in the path to the goal state (x and y coordinate) 

point selected :  [0, 4]

95) The state of the maze after reaching the goal state.

~ . . . ~ 
~ ~ ~ ~ ~ 

96) The orientation of the die after moving to the goal state.

dice orientation :

east : 3
west : 4
north : 2
south : 5
top : 1
bottom : 6

97) The total path from the start to goal state along with the Nodes generated, nodes visisted and the number of nodes in solution.

Total path is :  [[0, 0], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [0, 4]]
Nodes Generated :  22
Nodes visited :  15
Number of moves in the Solution :  7

-----------------------------------
