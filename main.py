#include <iostream>
#include <fstream>
#include <string>
#include <thread>
using namespace std;

//Function Prototypes
void printArray(int arr[][20],int rows, int cols);
int numNeighbors(int i,int j,int arr[][20], int rows, int cols);
int deadOrAlive(int i, int j, int arr[][20], int n);
void playThreaded(int arr[][20], int row_begin, int row_end, int col_begin, int col_end, int rows, int cols, int newArray[][20]);  
bool again();

//Main function to read in file, generate array, and create the threads to "play" the Game of Life
int main() {   

    //Input files will list the number of rows, the number of cols in the next line, then the contents of each row in each subsequent line
    
    string fileName = "";  //Input file
    cout << "Please enter the name of a file containing Game of Life data: ";
    cin >> fileName;

    fstream inFile;
    inFile.open(fileName);

    if(inFile.is_open() == false){
        cout << "Invalid file name." << endl;
        exit(-1);
    }

    int rows = 0;
    int cols = 0;

    inFile >> rows;
    inFile >> cols;

    string line = ""; 
    getline(inFile, line);

    int array[20][20];

    int currentRow = 0; //Populating array
    while(getline(inFile,line)){
        for(int i = 0; i < cols; i++){
            if(line[i] == '0'){
                array[currentRow][i] = 0;
            }
            else{
                array[currentRow][i] = 1;
        }}
        currentRow++;
    }

    cout << "\nOriginal Grid: \n"; //Printing original array
    printArray(array,rows,cols);
    cout << "\n";

    int newArray[20][20]; //Creating threads to play the Game of Life as long as the user wishes to continue
    int iteration = 1;
    while (again() == true){
        thread th1(playThreaded, array, 0, 3, 0, 3, rows, cols, newArray);  
        thread th2(playThreaded, array, 0, 3, 3, 5, rows, cols, newArray);   
        thread th3(playThreaded, array, 3, 5, 0, 3, rows, cols, newArray);
        thread th4(playThreaded, array, 3, 5, 3, 5, rows, cols, newArray);
        th1.join();
	    th2.join();
	    th3.join();
	    th4.join();
        cout << "\nIteration #" << iteration << "\n"; //Prints it out in a pleasing way
        printArray(newArray, rows, cols);  
        cout << "\n";
        for (int i = 0; i < rows; i++) {  //Populates the old array with the new array so you can repopulate newArray
            for (int j = 0; j < cols; j++) {
                array[i][j] = newArray[i][j];
        }}
        iteration ++;     
    }   
}

void playThreaded(int arr[][20], int row_begin, int row_end, int col_begin, int col_end, int rows, int cols, int newArray[][20]){
    for (int i = row_begin; i < row_end; i++){  //Nested for loop that will call the functions for only the rows and cols that the thread calls for
        for (int j = col_begin; j < col_end; j++){         
            int n = numNeighbors(i, j, arr, rows, cols); 
            newArray[i][j] = deadOrAlive(i, j, arr, n);  
}}}

int numNeighbors(int i,int j,int arr[][20], int rows, int cols) {   //Counts the number of neighbors of position [i][j]
    int neighbors = 0;
    if (i==0){
        if (j==0){
            neighbors = arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1];
        }
        else if (j==(cols-1)){
            neighbors = arr[i+1][j] + arr[i+1][j-1] + arr[i][j-1];
        }
        else {
            neighbors = arr[i][j-1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1];
        }}
    else if (i == rows-1){
        if (j==0){
            neighbors = arr[i-1][j] + arr[i-1][j+1] + arr[i][j+1];
        }
        else if (j== cols-1){
            neighbors = arr[i-1][j] + arr[i-1][j-1] + arr[i][j-1];
        }
        else {
            neighbors = arr[i][j-1] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j+1];
        }}
    else if (j == 0) {
        neighbors = arr[i-1][j] + arr[i-1][j+1] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j];
    }      
    else if (j == cols-1) { 
        neighbors = arr[i-1][j] + arr[i-1][j-1] + arr[i][j-1] + arr[i+1][j-1] + arr[i+1][j];
    }
    else {
        neighbors = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j-1] + arr[i][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1];
    }
    return neighbors;
}      

void printArray(int arr[][20],int rows, int cols){
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < cols; j++){
            cout << arr[i][j] << " "; 
        }
        cout << endl;         
}}

bool again(){ //Will ask the user if they would like to run another iteration
    string answer = "";
        cout << "Would you like to see the next iteration? (Y/N): ";
        cin >> answer;
        while ((answer != "Y") and (answer != "N") and (answer != "y") and (answer != "n")){
            cout << "\nInvalid input, please try again: ";
            cin >> answer;
        }
        if ((answer == "N") or (answer == "n")){
            return false;
        }
        else{
            return true;
        }
}

int deadOrAlive(int i, int j, int arr[][20], int n){  //Checks for living status of position [i][j]
    int result = 0;
    if (n == 2){
        if (arr[i][j] == 1){
            result = 1;
        }}
    else if (n == 3) {
        result = 1;
    }
    return result;
}
