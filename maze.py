import linecache
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', default='inputfile.txt',help='Input File')
    parser.add_argument('-o', default='outputfile.txt',help='Output File')

    input_file = open("inputfile.txt", "r")
    output_file = open("outputfile.txt", "w")
    N = linecache.getline("inputfile.txt", 1)
    N = int(N)

    input_file = open("inputfile.txt", "r")

    input_file = open("inputfile.txt", "r")
    input_matrix = []

    for i in range(N+1):
        line = input_file.readline()
        if i > 0:
            input_matrix.append(list(map(int, line.rstrip().split())))
    input_file.close()

    temp_list = solveMaze(input_matrix, N)

    if type(temp_list) is list:
        for i in temp_list:
            for j in i:
                output_file.write(str(j))
                output_file.write(" ")

            output_file.write("\n")
        output_file.close()

    else:
        output_file.write(str(temp_list))
        output_file.close()

def isSafe(maze, x, y, N):

    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True

    return False


def solveMaze(maze, N):

    sol = [[0 for j in range(N)] for i in range(N)]

    if not solveMazeRat(maze, 0, 0, sol, N):
        return "-1"
    return sol


def solveMazeRat(maze, x, y, sol, N):

    if x == N - 1 and y == N - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True

    if isSafe(maze, x, y, N):
        sol[x][y] = 1

        if solveMazeRat(maze, x + 1, y, sol, N):
            return True

        if solveMazeRat(maze, x, y + 1, sol, N):
            return True

        sol[x][y] = 0
        return False


if __name__ == '__main__':
    main()