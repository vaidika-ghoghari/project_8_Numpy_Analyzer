
import numpy as np
import pandas as pd

class DataAnalytics:
    MAX_ELEMENTS = 10000

    def __init__(self):
        self.__data = np.array([])

    @classmethod
    def show_supported_dimensions(cls):
        print('Supported array dimensions: 1D, 2D, and 3D')

    @staticmethod
    def validate_dimensions(shape):
        return all(size > 0 for size in shape)

    @staticmethod
    def get_dimension(array):
        if len(array.shape) == 1:
            return 1
        elif len(array.shape) == 2:
            return 2
        elif len(array.shape) == 3:
            return 3
        else:
            return 0

    def __calculate_total(self, shape):
        total = 1
        for size in shape:
            total = total * size
        return total

    @staticmethod
    def calculate_correlation(array1, array2):
        if len(array1) != len(array2):
            print('Both arrays must have the same length.')
            return None
        if len(array1) < 2:
            print('At least two values are required.')
            return None
        if np.std(array1) == 0 or np.std(array2) == 0:
            print('Correlation is undefined for constant values.')
            return None
        return np.corrcoef(array1, array2)[0, 1]

    def create_array(self):
        self.show_supported_dimensions()
        try:
            dimension = int(input('Enter dimension (1, 2, or 3): '))
            if dimension == 1:
                shape = (int(input('Enter number of elements: ')),)
            elif dimension == 2:
                rows = int(input('Enter rows: '))
                columns = int(input('Enter columns: '))
                shape = (rows, columns)
            elif dimension == 3:
                layers = int(input('Enter layers: '))
                rows = int(input('Enter rows: '))
                columns = int(input('Enter columns: '))
                shape = (layers, rows, columns)
            else:
                print('Choose dimension 1, 2, or 3.')
                return

            if not self.validate_dimensions(shape):
                print('Dimensions must be greater than zero.')
                return

            total = self.__calculate_total(shape)
            if total > self.MAX_ELEMENTS:
                print(f'Array is too large. Maximum allowed elements: {self.MAX_ELEMENTS}.')
                return

            values = input('Enter all numbers separated by spaces: ').split()
            if len(values) != total:
                print('Number of values does not match dimensions.')
                return

            values = list(map(float, values))
            self.__data = np.array(values).reshape(shape)
            print('Array created successfully!')
            print(self.__data)

        except ValueError:
            print('Error: Enter valid numbers.')
        except MemoryError:
            print('Error: Not enough memory to create the array.')

    def display_array(self):
        if self.__data.size == 0:
            print('Please create an array first.')
            return

        dimension = self.get_dimension(self.__data)
        if dimension == 1:
            print('1D Array')
            print(pd.DataFrame(self.__data, columns=['Values']))
        elif dimension == 2:
            print('2D Array')
            print(pd.DataFrame(self.__data))
        elif dimension == 3:
            print('3D Array')
            print(self.__data)

    def indexing_slicing(self):
        if self.__data.size == 0:
            print('Please create an array first.')
            return

        try:
            dimension = self.get_dimension(self.__data)
            print('Array shape:', self.__data.shape)

            if dimension == 1:
                index = int(input('Enter element index: '))
                print('Element:', self.__data[index])
                start = int(input('Slice start: '))
                end = int(input('Slice end: '))
                print('Slice:', self.__data[start:end])

            elif dimension == 2:
                row = int(input('Enter row index: '))
                column = int(input('Enter column index: '))
                print('Element:', self.__data[row, column])
                print('Row:', self.__data[row, :])
                print('Column:', self.__data[:, column])
                
                row_start = int(input('Row slice start: '))
                row_end = int(input('Row slice end: '))
                column_start = int(input('Column slice start: '))
                column_end = int(input('Column slice end: '))

                print('Sliced array:\n',
                    self.__data[row_start:row_end, column_start:column_end])

            elif dimension == 3:
                layer = int(input('Enter layer index: '))
                row = int(input('Enter row index: '))
                column = int(input('Enter column index: '))
                print('Element:', self.__data[layer, row, column])
                print('Selected layer:\n', self.__data[layer, :, :])
                print('Selected row:', self.__data[layer, row, :])
                print('Selected column:', self.__data[layer, :, column])
                start = int(input('Layer slice start: '))
                end = int(input('Layer slice end: '))
                print('Sliced layers:\n', self.__data[start:end, :, :])

        except ValueError:
            print('Error: Enter valid integer indexes.')
        except IndexError:
            print('Error: Index is outside the array range.')

    def mathematical_operations(self):
        if self.__data.size == 0:
            print('Please create an array first.')
            return

        try:
            values = input('Enter another array with the same shape: ').split()
            if len(values) != self.__data.size:
                print('Incorrect number of values.')
                return

            second = np.array(list(map(float, values))).reshape(self.__data.shape)

            print('Addition:\n', np.add(self.__data, second))
            print('Subtraction:\n', np.subtract(self.__data, second))
            print('Multiplication:\n', np.multiply(self.__data, second))

            if np.any(second == 0):
                print('Division cannot be performed because the second array contains zero.')
            else:
                print('Division:\n', np.divide(self.__data, second))

        except ValueError:
            print('Error: Enter valid numbers.')
        except MemoryError:
            print('Error: Not enough memory to perform the operation.')

    def dot_product(self):
        if self.__data.size == 0:
            print('Please create an array first.')
            return

        try:
            dimension = self.get_dimension(self.__data)

            if dimension == 1:
                values = input('Enter another 1D array: ').split()
                second = np.array(list(map(float, values)))

                if len(second) != len(self.__data):
                    print('Both arrays must have the same length.')
                    return

                print('Dot product:', np.dot(self.__data, second))

            elif dimension == 2:
                rows = int(input('Enter second matrix rows: '))
                columns = int(input('Enter second matrix columns: '))

                if rows <= 0 or columns <= 0:
                    print('Dimensions must be greater than zero.')
                    return

                if rows * columns > self.MAX_ELEMENTS:
                    print('Second matrix is too large.')
                    return

                if self.__data.shape[1] != rows:
                    print('Matrix dimensions are incompatible.')
                    return

                values = input('Enter second matrix values: ').split()
                total = rows * columns

                if len(values) != total:
                    print('Incorrect number of values.')
                    return

                second = np.array(list(map(float, values)))
                second = second.reshape(rows, columns)

                print('Matrix multiplication using dot product:')
                print(np.dot(self.__data, second))

                if self.__data.shape == second.shape:
                    print('Element-wise multiplication:')
                    print(np.multiply(self.__data, second))

            else:
                print('Use a 1D or 2D array for this operation.')

        except ValueError:
            print('Error: Enter valid numbers.')
        except MemoryError:
            print('Error: Not enough memory to perform matrix operations.')

    def aggregative_operations(self):
        if self.__data.size == 0:
            print('Please create an array first.')
            return

        try:
            print('Sum:', np.sum(self.__data))
            print('Mean:', np.mean(self.__data))
            print('Median:', np.median(self.__data))
            print('Standard deviation:', np.std(self.__data))
            print('Variance:', np.var(self.__data))

        except (ValueError, TypeError):
            print('Error: Unable to calculate aggregate values.')

    def statistical_operations(self):
        if self.__data.size == 0:
            print('Please create an array first.')
            return

        try:
            print('Minimum:', np.min(self.__data))
            print('Maximum:', np.max(self.__data))

            percentile = float(input('Enter percentile (0 to 100): '))
            if not 0 <= percentile <= 100:
                print('Percentile must be between 0 and 100.')
                return

            print('Percentile:', np.percentile(self.__data, percentile))

            if self.get_dimension(self.__data) != 1:
                print('Correlation currently supports 1D arrays only.')
                return

            values = input('Enter another array for correlation: ').split()
            second = np.array(list(map(float, values)))

            result = self.calculate_correlation(self.__data, second)
            if result is not None:
                print('Correlation coefficient:', result)

        except ValueError:
            print('Error: Enter valid numbers.')

    def search_value(self):
        if self.__data.size == 0:
            print('Please create an array first.')
            return

        try:
            print('1. Equal to')
            print('2. Greater than')
            print('3. Less than')
            print('4. Greater than or equal to')
            print('5. Less than or equal to')

            condition = input('Choose condition: ')
            value = float(input('Enter search value: '))

            if condition == '1':
                mask = self.__data == value
            elif condition == '2':
                mask = self.__data > value
            elif condition == '3':
                mask = self.__data < value
            elif condition == '4':
                mask = self.__data >= value
            elif condition == '5':
                mask = self.__data <= value
            else:
                print('Invalid condition.')
                return

            indices = np.argwhere(mask)

            if indices.size > 0:
                print('Matching indices:\n', indices)
                print('Matching values:', self.__data[mask])
            else:
                print('No matching values found.')

        except ValueError:
            print('Error: Enter a valid number.')

    def sort_array(self):
        if self.__data.size == 0:
            print('Please create an array first.')
            return

        try:
            dimension = self.get_dimension(self.__data)
            order = input('1. Ascending  2. Descending: ')

            if order == '1':
                print('Sorted array:\n', np.sort(self.__data, axis=dimension - 1))
            elif order == '2':
                sorted_array = np.sort(self.__data, axis=dimension - 1)
                print('Sorted array:\n', np.flip(sorted_array, axis=dimension - 1))
            else:
                print('Invalid choice.')

        except (ValueError, TypeError):
            print('Error: Unable to sort the array.')

    def filter_array(self):
        if self.__data.size == 0:
            print('Please create an array first.')
            return

        try:
            print('1. Equal to')
            print('2. Greater than')
            print('3. Less than')
            print('4. Greater than or equal to')
            print('5. Less than or equal to')

            condition = input('Choose condition: ')
            value = float(input('Enter filter value: '))

            if condition == '1':
                result = self.__data[self.__data == value]
            elif condition == '2':
                result = self.__data[self.__data > value]
            elif condition == '3':
                result = self.__data[self.__data < value]
            elif condition == '4':
                result = self.__data[self.__data >= value]
            elif condition == '5':
                result = self.__data[self.__data <= value]
            else:
                print('Invalid condition.')
                return

            print('Filtered values:', result)

        except ValueError:
            print('Error: Enter a valid number.')

    def combine_arrays(self):
        if self.__data.size == 0:
            print('Please create an array first.')
            return

        try:
            values = input('Enter another array with the same shape: ').split()

            if len(values) != self.__data.size:
                print('Incorrect number of values.')
                return

            second = np.array(list(map(float, values)))
            second = second.reshape(self.__data.shape)

            print('Combined array:\n', np.concatenate((self.__data, second), axis=0))

            first, other = np.array_split(self.__data, 2)
            print('First split:\n', first)
            print('Second split:\n', other)

        except ValueError:
            print('Error: Enter valid numbers.')
        except MemoryError:
            print('Error: Not enough memory to combine or split arrays.')

    def update_value(self):
        if self.__data.size == 0:
            print('Please create an array first.')
            return

        try:
            dimension = self.get_dimension(self.__data)
            indices = []

            for i in range(dimension):
                index = int(input(f'Enter index for dimension {i + 1}: '))
                indices.append(index)

            value = float(input('Enter new value: '))
            self.__data[tuple(indices)] = value

            print('Updated array:\n', self.__data)

        except ValueError:
            print('Error: Enter valid index and value.')
        except IndexError:
            print('Error: Index is outside the array range.')


def main():
    analyzer = DataAnalytics()

    while True:
        print('\n===== NUMPY ANALYZER =====')
        print('1. Create Array')
        print('2. Display Array')
        print('3. Indexing and Slicing')
        print('4. Arithmetic Operations')
        print('5. Dot Product / Matrix Multiplication')
        print('6. Aggregative Operations')
        print('7. Statistical Operations')
        print('8. Search')
        print('9. Sort')
        print('10. Filter')
        print('11. Combine and Split')
        print('12. Update Array')
        print('13. Exit')

        try:
            choice = int(input('Enter your choice: '))

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
                print('Thank you for using NumPy Analyzer!')
                break
            else:
                print('Invalid choice. Select from 1 to 13.')

        except ValueError:
            print('Error: Enter a valid menu number.')


if __name__ == '__main__':
    main()
