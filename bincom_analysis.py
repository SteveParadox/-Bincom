import pandas as pd
import numpy as np

# computed the table data in a dictionary format using pandas 
data = {
    'Monday': ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    'Tuesday': ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE'],
    'Wednesday': ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE'],
    'Thursday': ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    'Friday': ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']
}

def bincom_analysis():

    # i converted the data to a Pandas DataFrame
    df = pd.DataFrame(data)

    # this code counts the frequency of each color
    color_counts = df.apply(pd.Series.value_counts).fillna(0)

    # Calculating the mean color
    mean_color = color_counts.mean(axis=1).idxmax()

    # Calculating the mode (most frequently occurring) color
    mode_color = color_counts.sum(axis=1).idxmax()

    # Calculating the median color
    median_color = color_counts.sum(axis=1).sort_values().iloc[color_counts.shape[0] // 2]

    variance = color_counts.var(axis=1).mean()

    # Counting the frequency of each color across all days
    color_counts = df.stack().value_counts()

    # Counting the frequency of the color red
    red_count = color_counts.get('RED', 0)

    # checking the probability that a randomly chosen color is red
    prob_red = red_count / color_counts.sum()

   
    print(f"The mean color is {mean_color}")
    print(f"The most worn color throughout the week is {mode_color}")
    print(f"The median color is {median_color}")
    print("the Variance is:", variance)
    print(f"The probability that a randomly chosen color is red is {prob_red:.2%}")

    return mean_color, mode_color, median_color, variance

mean_color, mode_color, median_color, variance = bincom_analysis()
