# NumPy Analyzer – Multi-Dimensional Array Analysis Tool

A menu-driven Python application built using **NumPy and Pandas** to create, manipulate, and analyze multidimensional arrays. It supports 1D, 2D, and 3D arrays and provides various mathematical, statistical, searching, sorting, and filtering operations.

## 📌 Project Overview

The **NumPy Analyzer** is designed to perform different operations on multidimensional arrays through an interactive menu-driven interface. Users can create arrays, access and modify elements, perform mathematical calculations, apply conditions, and analyze numerical data.

The application follows an Object-Oriented Programming approach using a `DataAnalytics` class. Different methods are used to organize individual operations, making the program structured and easier to maintain.

## ✨ Features

- **Array Creation:** Create 1D, 2D, and 3D NumPy arrays with a maximum limit of 10,000 elements.
- **Array Display:** Display 1D and 2D arrays using Pandas DataFrames and 3D arrays using NumPy.
- **Indexing and Slicing:** Access individual elements, rows, columns, layers, and selected portions of arrays.
- **Arithmetic Operations:** Perform addition, subtraction, element-wise multiplication, and division.
- **Dot Product:** Calculate the dot product of 1D arrays using `np.dot()`.
- **Matrix Multiplication:** Perform matrix multiplication on compatible 2D arrays using `np.dot()`.
- **Aggregate Operations:** Calculate sum, mean, median, standard deviation, and variance.
- **Statistical Operations:** Find minimum, maximum, percentiles, and correlation coefficients.
- **Search Operations:** Search for array elements using equality and comparison conditions.
- **Sorting:** Sort array elements in ascending or descending order along the last axis.
- **Filtering:** Retrieve array elements based on specified comparison conditions.
- **Combine and Split:** Combine arrays along the first axis and split an existing array into two parts.
- **Update Values:** Modify existing array elements using their indexes.

## 🛠️ Technologies Used

- Python 3
- NumPy
- Pandas

## 📂 Project Structure

```text
project_8_Numpy_Analyzer/
│
├── numpy_analyzer.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

**2. Navigate to the project directory**

```bash
cd project_8_Numpy_Analyzer
```

**3. Install the required libraries**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
python numpy_analyzer.py
```

## 📋 Main Menu

| Option | Operation |
|:---:|---|
| 1 | Create Array |
| 2 | Display Array |
| 3 | Indexing and Slicing |
| 4 | Arithmetic Operations |
| 5 | Dot Product / Matrix Multiplication |
| 6 | Aggregative Operations |
| 7 | Statistical Operations |
| 8 | Search |
| 9 | Sort |
| 10 | Filter |
| 11 | Combine and Split |
| 12 | Update Array |
| 13 | Exit |

## 🧠 Python Concepts Demonstrated

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors
- Encapsulation
- Private Variables and Methods
- Class Methods
- Static Methods
- Conditional Statements
- Loops
- Exception Handling
- Input Validation
- NumPy Array Manipulation
- Pandas DataFrame

## 🛡️ Input Validation and Exception Handling

The application uses input validation and exception handling to manage common input errors and prevent invalid operations.

Some situations handled include:

- Invalid numerical input
- Incorrect array dimensions
- Negative or zero dimensions
- Array size exceeding the maximum allowed limit during array creation
- Incorrect number of input values
- Invalid array indexes
- Division by zero
- Incompatible matrix dimensions
- Invalid menu selections
- Invalid percentile values
- Arrays with unequal lengths for correlation
- Correlation with constant values
- Memory-related errors during selected array operations

## 🎯 Learning Outcomes

Through this project, I gained practical experience working with multidimensional NumPy arrays and performing mathematical and statistical operations.

I also improved my understanding of Object-Oriented Programming, encapsulation, array indexing and slicing, input validation, and exception handling. Developing this application helped me organize multiple operations into a structured, menu-driven Python program.

## 🔗 Connect & Project Resources

- **Project Explanation Video:** [Watch Here](YOUR_VIDEO_LINK)
- **LinkedIn:** [Connect with Me](https://www.linkedin.com/in/vaidika-ghoghari-2196a534a)
- **Email:** [Contact Me](mailto:ghogharivaidika@gmail.com)

## 👩‍💻 Author

**Vaidika**

Python Programming | NumPy | Pandas | Object-Oriented Programming

---

⭐ If you find this project useful, consider giving the repository a star!
