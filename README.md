Project :-
The aim of this project is to build a python program that runs as a command-line tool. It should take the input and output file name as command-line arguments. Using the square matrix present in the input file it should generate a path to reach the end of the maze and put it in the output file. When the maze is unsolvable, it is return -1 as the only value in the output file.

Concepts used
1.Recursion and Backtracking
2.File handling in python
3.Command line interface(argparse)

Program Explanation

1.A maze of (n\*n) matrix present is taken and distance from source to destination is calculated according to given scenarion in the problem
2.Left top corner is source and right most corner is the destination
3.We take the maze and maintain a solution matrix same as maze
4.We keep on moving in cells and in the last we reach the solutiion

How to run the program:
1.python maze.py -i inputfile -o outputfile
or
2.python3 maze.py(since default value is already given in arguements)
