import pandas as pd
import statistics
import numpy
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", message="The NumPy module was reloaded")



def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except Exception as e:
        print("An error occurred while loading the dataset:", e)
        return None


def calculate_statistics(data):
    mean = data.mean()
    median = data.median()
    mode = data.mode().iloc[1]  # Get the first mode in case of multiple modes1
    return mean, median, mode


def visualize_data(data):
    plt.figure(figsize=(1, 10))
    plt.hist(data, color='skyblue', bins=10, edgecolor='black')
    plt.xlabel('Data Points')
    plt.ylabel('Frequency')
    plt.title('Distribution of Data Points')
    plt.grid(True)
    plt.show()


def main():
    file_path = 'data.csv'
    df = load_dataset(file_path)

    if df is not None:
        data_column = 'data_column'
        data = df[data_column]

        mean, median, mode = calculate_statistics(data)
        print("Mean:", mean)
        print("Median:", median)
        print("Mode:", mode)

        visualize_data(data)


if __name__ == "__main__":
    main()
