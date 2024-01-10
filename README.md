# GameOfLife
Individual C++ project of a multi-threaded version of Conway's Game of Life.

Conway's Game of Life is a cellular automation devised by mathematician John Conway in 1970. Each "cell" can be dead or alive, and each cell will change with each iteration depending on the state of its neighboring cells. The following rules determine the state of a cell:
    - Any live cell with fewer than two live neighbours dies (referred to as underpopulation).
    - Any live cell with more than three live neighbours dies (referred to as overpopulation).
    - Any live cell with two or three live neighbours lives, unchanged, to the next generation.
    - Any dead cell with exactly three live neighbours comes to life.

This project reads in its intitial state through an input file containing the number of rows, the number of columns, and then the status of all the cells in the array (See "file.txt" for example).
This project is multi-threaded to achieve greater efficiency of iterations of large arrays
