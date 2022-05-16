The purpose of this project was to visualize the time series data by creating a line chart, bar chart, and boxplots using the pandas, matplotlib, and seaborn libraries.  The purpose of the visualizations is to help understand patterns in page visits.  

The data was used to complete the following tasks in the `time_series_visualizer.py` script:
* Use pandas to import the data from `fcc-forum-pageviews.csv`
* Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
* Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be "Daily freeCodeCamp Forum Page Views 5/2016-12/2019". The label on the x axis should be "Date" and the label on the y axis should be "Page Views".
* Create a draw_bar_plot function that draws a bar chart. It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of "Months". On the chart, the label on the x axis should be "Years" and the label on the y axis should be "Average Page Views".
* Create a draw_box_plot function that uses seaborn.  These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be "Year-wise Box Plot (Trend)" and the title of the second chart should be "Month-wise Box Plot (Seasonality)". Make sure the month labels on bottom start at "Jan" and the x and x axis are labeled correctly. 

For the test cases `test_module.py` was used. 

See `line_plot.png` `box_plot.png` `bar_plot.png` for the results produced from the `time_series_visualizer.py` script.
