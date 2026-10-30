
import numpy as np
import pandas as pd


class DataAnalytics:

    MAX_ELEMENTS = 10000

    def __init__(self):
        self.__arrays = {
            1: np.array([]),
            2: np.array([]),
            3: np.array([])
        }

    @classmethod
    def show_supported_dimensions(cls):
        print("\nSupported Arrays:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

    @staticmethod
    def validate_dimensions(shape):
        return all(size > 0 for size in shape)

    @staticmethod
    def get_dimension(array):
        return len(array.shape)

    def __calculate_total(self, shape):
        total = 1
        for size in shape:
            total *= size
        return total

    def select_array(self):
        self.show_supported_dimensions()

        try:
            dimension = int(input("\nChoose array type: "))

            if dimension not in (1, 2, 3):
                print("Invalid choice. Please select 1, 2, or 3.")
                return None

            if self.__arrays[dimension].size == 0:
                print(f"\nThe {dimension}D array has not been created yet.")
                print("Please create this array first.")
                return None

            print(f"\nSelected: {dimension}D Array")
            return dimension

        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")
            return None

    def create_array(self):
        self.show_supported_dimensions()

        try:
            dimension = int(input("\nChoose array type to create: "))

            if dimension not in (1, 2, 3):
                print("Invalid choice. Select 1, 2, or 3.")
                return

            if dimension == 1:
                size = int(input("Enter number of elements: "))
                shape = (size,)

            elif dimension == 2:
                rows = int(input("Enter number of rows: "))
                columns = int(input("Enter number of columns: "))
                shape = (rows, columns)

            else:
                layers = int(input("Enter number of layers: "))
                rows = int(input("Enter number of rows: "))
                columns = int(input("Enter number of columns: "))
                shape = (layers, rows, columns)

            if not self.validate_dimensions(shape):
                print("Invalid dimensions. All dimensions must be greater than zero.")
                return

            total = self.__calculate_total(shape)

            if total > self.MAX_ELEMENTS:
                print(f"Array too large. Maximum allowed elements: {self.MAX_ELEMENTS}.")
                return

            total = self.__calculate_total(shape)

            print(f"\nEnter exactly {total} integer values:")
            values = list(map(int, input("Values: ").split()))

            if len(values) != total:
                print(f"Incorrect number of values. Please enter exactly {total} values.")
                return

            values = list(map(float, values))
            new_array = np.array(values).reshape(shape)

            self.__arrays[dimension] = new_array

            print(f"\n{dimension}D Array created successfully!")
            print("\nArray:")
            print(new_array)

        except ValueError:
            print("Invalid input. Enter valid integers for dimensions and numeric values for the array.")
        except MemoryError:
            print("Memory error. Not enough memory to create this array.")
        except TypeError:
            print("Invalid data type. Please enter numeric values only.")

    def display_array(self):
        self.show_supported_dimensions()

        try:
            dimension = int(input("\nChoose array to display: "))

            if dimension not in (1, 2, 3):
                print("Invalid choice. Select 1, 2, or 3.")
                return

            array = self.__arrays[dimension]

            if array.size == 0:
                print(f"The {dimension}D array has not been created yet.")
                return

            print(f"\n===== {dimension}D ARRAY =====")
            print("\nArray shape:", array.shape)
            print("Total elements:", array.size)

            if dimension == 1:
                print("\n1D Array:")
                print(pd.DataFrame(array, columns=["Values"]))

            elif dimension == 2:
                print("\n2D Array:\n")
                print(array)

            else:
                print("\n3D Array:")
                for i in range(array.shape[0]):
                    print(f"\nLayer {i + 1}:")
                    print(array[i, :, :])

        except ValueError:
            print("Invalid input. Enter 1, 2, or 3 to select the array.")

    def indexing_slicing(self):
        dimension = self.select_array()

        if dimension is None:
            return

        array = self.__arrays[dimension]

        try:
            print("\nArray shape:", array.shape)
            indices = []

            for i in range(dimension):
                index = int(input(f"Enter index for dimension {i + 1}: "))
                indices.append(index)

            print("\nSelected element:", array[tuple(indices)])

            print("\nEnter slicing range for each dimension.")
            slices = []

            for i in range(dimension):
                start = int(input(f"Enter start index for dimension {i + 1}: "))
                end = int(input(f"Enter end index for dimension {i + 1}: "))
                slices.append(slice(start, end))

            print("\nSliced Array:\n")
            print(array[tuple(slices)])

        except ValueError:
            print("Invalid input. Indexes and slice ranges must be integers.")
        except IndexError:
            print("Index error. The entered index is outside the array range.")
        except TypeError:
            print("Invalid indexing operation. Please check your indexes.")

    def mathematical_operations(self):
        dimension = self.select_array()

        if dimension is None:
            return

        first = self.__arrays[dimension]

        try:
            print(f"\nSelected {dimension}D array shape:", first.shape)
            print(f"Enter {first.size} values for the second {dimension}D array.")

            values = input("Enter values separated by spaces: ").split()

            if len(values) != first.size:
                print(f"Incorrect number of values. Enter exactly {first.size} values.")
                return

            second = np.array(list(map(float, values))).reshape(first.shape)

            print("\n===== ARITHMETIC OPERATIONS =====")

            print("\nAddition:\n")
            print(np.add(first, second))

            print("\nSubtraction:\n")
            print(np.subtract(first, second))

            print("\nElement-wise Multiplication:\n")
            print(np.multiply(first, second))

            if np.any(second == 0):
                print("\nDivision cannot be performed because the second array contains zero.")
            else:
                print("\nDivision:\n")
                print(np.divide(first, second))

        except ValueError:
            print("Invalid input. Enter the correct number of numeric values.")
        except MemoryError:
            print("Memory error. Not enough memory to perform arithmetic operations.")
        except TypeError:
            print("Invalid data type. Arithmetic operations require numeric arrays.")

    def dot_product(self):
        dimension = self.select_array()

        if dimension is None:
            return

        first = self.__arrays[dimension]

        try:
            print("\nSelected array shape:", first.shape)

            if dimension == 1:
                size = int(input("Enter number of elements in the second 1D array: "))

                if size != first.shape[0]:
                    print("Both 1D arrays must have the same length.")
                    return

                if size <= 0:
                    print("Array size must be greater than zero.")
                    return

                values = input("Enter second array values: ").split()

                if len(values) != size:
                    print(f"Enter exactly {size} values.")
                    return

                second = np.array(list(map(float, values)))
                print("\nDot Product:", np.dot(first, second))

            elif dimension == 2:
                rows = int(input("Enter rows of second matrix: "))
                columns = int(input("Enter columns of second matrix: "))

                if rows <= 0 or columns <= 0:
                    print("Matrix dimensions must be greater than zero.")
                    return

                if rows * columns > self.MAX_ELEMENTS:
                    print("Second matrix is too large.")
                    return

                if first.shape[1] != rows:
                    print("Incompatible matrices. First matrix columns must equal second matrix rows.")
                    return

                values = input("Enter second matrix values: ").split()

                if len(values) != rows * columns:
                    print(f"Enter exactly {rows * columns} values.")
                    return

                second = np.array(list(map(float, values))).reshape(rows, columns)

                print("\nMatrix Multiplication:\n")
                print(np.dot(first, second))

            else:
                print("\nFor 3D dot product, enter the shape of the second array.")

                layers = int(input("Enter number of layers: "))
                rows = int(input("Enter rows: "))
                columns = int(input("Enter columns: "))

                shape = (layers, rows, columns)

                if not self.validate_dimensions(shape):
                    print("All dimensions must be greater than zero.")
                    return

                if self.__calculate_total(shape) > self.MAX_ELEMENTS:
                    print("Second array is too large.")
                    return

                if first.shape[2] != rows:
                    print("Incompatible arrays. First array's last dimension must equal the second array's second dimension.")
                    return

                total = self.__calculate_total(shape)
                values = input(f"Enter exactly {total} values: ").split()

                if len(values) != total:
                    print(f"Incorrect number of values. Enter exactly {total} values.")
                    return

                second = np.array(list(map(float, values))).reshape(shape)

                print("\n3D Dot Product:\n")
                print(np.dot(first, second))

        except ValueError:
            print("Invalid input. Enter valid integer dimensions and numeric values.")
        except MemoryError:
            print("Memory error. Not enough memory to perform dot product.")
        except TypeError:
            print("Invalid data type for dot product.")
        except IndexError:
            print("Invalid array dimensions. Please check the entered shape.")

    def aggregative_operations(self):
        dimension = self.select_array()

        if dimension is None:
            return

        array = self.__arrays[dimension]

        try:
            print("\n===== AGGREGATIVE OPERATIONS =====")
            print("\nSum:", np.sum(array))
            print("Mean:", np.mean(array))
            print("Median:", np.median(array))
            print("Standard Deviation:", np.std(array))
            print("Variance:", np.var(array))

        except (ValueError, TypeError):
            print("Unable to calculate aggregate values. Check the array data.")
        except MemoryError:
            print("Memory error while calculating aggregate values.")

    def statistical_operations(self):
        dimension = self.select_array()

        if dimension is None:
            return

        array = self.__arrays[dimension]

        try:
            print("\n===== STATISTICAL OPERATIONS =====")
            print("\nMinimum:", np.min(array))
            print("Maximum:", np.max(array))

            percentile = float(input("\nEnter percentile (0 to 100): "))

            if percentile < 0 or percentile > 100:
                print("Invalid percentile. Enter a value between 0 and 100.")
                return

            print("Percentile:", np.percentile(array, percentile))

            if dimension != 1:
                print("\nCorrelation is available only for 1D arrays.")
                return

            values = input("\nEnter second 1D array values for correlation: ").split()

            if len(values) != len(array):
                print("Both arrays must have the same length.")
                return

            second = np.array(list(map(float, values)))

            if len(array) < 2:
                print("At least two values are required for correlation.")
                return

            if np.std(array) == 0 or np.std(second) == 0:
                print("Correlation is undefined for constant values.")
                return

            print("Correlation coefficient:", np.corrcoef(array, second)[0, 1])

        except ValueError:
            print("Invalid input. Enter a valid percentile and numeric values.")
        except TypeError:
            print("Invalid data type for statistical operations.")
        except MemoryError:
            print("Memory error while performing statistical operations.")

    def search_value(self):
        dimension = self.select_array()

        if dimension is None:
            return

        array = self.__arrays[dimension]

        try:
            print("\n===== SEARCH CONDITIONS =====")
            print("1. Equal to")
            print("2. Greater than")
            print("3. Less than")
            print("4. Greater than or equal to")
            print("5. Less than or equal to")

            condition = int(input("\nChoose condition: "))
            value = float(input("Enter search value: "))

            if condition == 1:
                mask = array == value
            elif condition == 2:
                mask = array > value
            elif condition == 3:
                mask = array < value
            elif condition == 4:
                mask = array >= value
            elif condition == 5:
                mask = array <= value
            else:
                print("Invalid condition. Select from 1 to 5.")
                return

            indices = np.argwhere(mask)

            if indices.size > 0:
                print("\nMatching indexes:\n")
                print(indices)
                print("\nMatching values:\n")
                print(array[mask])
            else:
                print("\nNo matching values found.")

        except ValueError:
            print("Invalid input. Enter an integer condition and a numeric search value.")
        except TypeError:
            print("Invalid data type for searching.")

    def sort_array(self):
        dimension = self.select_array()

        if dimension is None:
            return

        array = self.__arrays[dimension]

        try:
            print("\n1. Ascending")
            print("2. Descending")

            order = int(input("\nChoose sorting order: "))

            if order == 1:
                result = np.sort(array, axis=-1)
            elif order == 2:
                result = np.flip(np.sort(array, axis=-1), axis=-1)
            else:
                print("Invalid choice. Select 1 or 2.")
                return

            print("\nSorted Array:\n")
            print(result)

        except ValueError:
            print("Invalid input. Enter 1 for ascending or 2 for descending.")
        except TypeError:
            print("Unable to sort the array. Check the data type.")

    def filter_array(self):
        dimension = self.select_array()

        if dimension is None:
            return

        array = self.__arrays[dimension]

        try:
            print("\n1. Equal to")
            print("2. Greater than")
            print("3. Less than")
            print("4. Greater than or equal to")
            print("5. Less than or equal to")

            condition = int(input("\nChoose filter condition: "))
            value = float(input("Enter filter value: "))

            if condition == 1:
                result = array[array == value]
            elif condition == 2:
                result = array[array > value]
            elif condition == 3:
                result = array[array < value]
            elif condition == 4:
                result = array[array >= value]
            elif condition == 5:
                result = array[array <= value]
            else:
                print("Invalid condition. Select from 1 to 5.")
                return

            print("\nFiltered Values:\n")
            print(result)

        except ValueError:
            print("Invalid input. Enter a valid condition and numeric filter value.")
        except TypeError:
            print("Invalid data type for filtering.")

    def combine_arrays(self):
        dimension = self.select_array()

        if dimension is None:
            return

        first = self.__arrays[dimension]

        try:
            print("\nSelected array shape:", first.shape)
            print(f"Enter another {dimension}D array with the same shape.")

            values = input("Enter values separated by spaces: ").split()

            if len(values) != first.size:
                print(f"Incorrect number of values. Enter exactly {first.size} values.")
                return

            second = np.array(list(map(float, values))).reshape(first.shape)

            print("\n===== COMBINED ARRAY =====\n")
            print(np.concatenate((first, second), axis=0))

            first_part, second_part = np.array_split(first, 2, axis=0)

            print("\n===== FIRST SPLIT =====\n")
            print(first_part)

            print("\n===== SECOND SPLIT =====\n")
            print(second_part)

        except ValueError:
            print("Invalid input. Enter the correct number of numeric values.")
        except MemoryError:
            print("Memory error. Not enough memory to combine or split arrays.")
        except TypeError:
            print("Unable to combine arrays. Check their data types and shapes.")

    def update_value(self):
        dimension = self.select_array()

        if dimension is None:
            return

        array = self.__arrays[dimension]

        try:
            print("\nArray shape:", array.shape)
            indices = []

            for i in range(dimension):
                index = int(input(f"Enter index for dimension {i + 1}: "))
                indices.append(index)

            value = float(input("\nEnter new value: "))

            array[tuple(indices)] = value

            print("\nArray updated successfully!")
            print("\nUpdated Array:\n")
            print(array)

        except ValueError:
            print("Invalid input. Enter integer indexes and a numeric new value.")
        except IndexError:
            print("Index error. The entered index is outside the array range.")
        except TypeError:
            print("Invalid value type. Please enter a numeric value.")


def main():

    analyzer = DataAnalytics()

    while True:

        print("\n========== NUMPY ANALYZER ==========")
        print("\n1. Create Array")
        print("2. Display Array")
        print("3. Indexing and Slicing")
        print("4. Arithmetic Operations")
        print("5. Dot Product / Matrix Multiplication")
        print("6. Aggregative Operations")
        print("7. Statistical Operations")
        print("8. Search")
        print("9. Sort")
        print("10. Filter")
        print("11. Combine and Split")
        print("12. Update Array")
        print("13. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                analyzer.create_array()

            elif choice == 2:
                analyzer.display_array()

            elif choice == 3:
                analyzer.indexing_slicing()

            elif choice == 4:
                analyzer.mathematical_operations()

            elif choice == 5:
                analyzer.dot_product()

            elif choice == 6:
                analyzer.aggregative_operations()

            elif choice == 7:
                analyzer.statistical_operations()

            elif choice == 8:
                analyzer.search_value()

            elif choice == 9:
                analyzer.sort_array()

            elif choice == 10:
                analyzer.filter_array()

            elif choice == 11:
                analyzer.combine_arrays()

            elif choice == 12:
                analyzer.update_value()

            elif choice == 13:
                print("\nThank you for using NumPy Analyzer!")
                break

            else:
                print("\nInvalid menu choice. Please select from 1 to 13.")

        except ValueError:
            print("\nInvalid input. Please enter a menu number from 1 to 13.")

        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
            break

        except MemoryError:
            print("\nMemory error. The requested operation needs too much memory.")

        except Exception as error:
            print("\nUnexpected error occurred:", error)
            print("Please check your input and try again.")


if __name__ == "__main__":
    main()
