import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv");

    # Create scatter plot
    df.plot(x = "Year", y = "CSIRO Adjusted Sea Level", kind = "scatter", title = "Rise in Sea Level", xlabel = "Year", ylabel = "Sea Level (inches)");
    x = df["Year"];
    y = df["CSIRO Adjusted Sea Level"];

    # Create first line of best fit
    result = linregress(x, y);
    # the line above could have also been broken out into its individual components if desired
    # example = slope, intercept, r_value, p_value, std_err = linregress(x, y);
        
    x_pred = pd.Series([i for i in range(1880, 2051)]);
    y_pred = result.slope * x_pred + result.intercept;
    plt.plot(x_pred, y_pred, "r");

    # Create second line of best fit
    df2 = df.loc[df["Year"] >= 2000];
    x2 = df2["Year"];
    y2 = df2["CSIRO Adjusted Sea Level"];
    result2 = linregress(x2, y2);
    x_pred2 = pd.Series([i for i in range(2000, 2051)]);
    y_pred2 = result2.slope * x_pred2 + result2.intercept;
    plt.plot(x_pred2, y_pred2, "blue");
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()