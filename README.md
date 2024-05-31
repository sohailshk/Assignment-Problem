# Assignment Problem Solver

## Description
This project is a graphical user interface (GUI) application developed using Python and Tkinter for solving the assignment problem. The assignment problem is a fundamental combinatorial optimization problem that involves assigning tasks to agents in a way that minimizes the total cost or maximizes the total profit. Users can input the cost matrix via the Tkinter GUI, and the application will provide the optimal assignment solution.

## Features
- **User-Friendly GUI**: Enter the cost matrix directly through a graphical user interface.
- **Optimal Assignment Solution**: Computes and displays the optimal assignment solution using a custom implementation of the Hungarian Algorithm.
- **Error Handling**: Validates user input to ensure a valid cost matrix.
- **Dynamic Matrix Creation**: Users can specify the number of rows and columns for the cost matrix.
- **Interactive Input**: Matrix entries can be easily navigated using the keyboard.
- **Clear and Reset**: Easily clear the input matrix and start over with new data.
- **Result Display**: Clearly displays the steps and final results in the GUI.

## Installation
To run this project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/sohailshk/Assignment-Problem.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd Assignment-Problem
    ```
4. **Run the application:**
    ```bash
    python main.py
    ```

## Usage
1. **Launch the application** by running `python main.py`.
2. **Enter the number of rows and columns** in the respective input fields.
3. **Click "Create Matrix"** to generate the matrix input fields.
4. **Enter the cost matrix values** into the provided input fields in the Tkinter GUI.
5. **Click "Compute"** to calculate and display the optimal assignment solution.
6. The **result will be displayed** in the GUI, showing the optimal assignment and the total cost.

## Code Quality and Project Highlights
- **Structured Code**: The project follows a modular structure, encapsulating the logic in static methods for better organization and readability.
- **Error Handling**: Ensures the application handles invalid inputs gracefully.
- **Optimized Algorithm**: Implements the Hungarian Algorithm with additional optimizations for performance.
- **Interactive and Dynamic GUI**: The Tkinter interface is designed to be intuitive, allowing users to easily interact with the matrix and view results.
- **Comprehensive Output**: Displays intermediate steps and the final optimized assignment with the total cost for better understanding.

## Screenshots
![Screenshot 1](![Screenshot 2024-05-31 105504](https://github.com/sohailshk/Assignment-Problem/assets/122166523/7c7330b0-a851-436b-982a-c1830d678fa8)
)
![Screenshot 2](![Screenshot 2024-05-31 105529](https://github.com/sohailshk/Assignment-Problem/assets/122166523/de777903-339e-4d20-9a8b-53f37338a7ac)
)

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## Contact
For any questions or feedback, please contact [sohailsaif504@gmail.com]
