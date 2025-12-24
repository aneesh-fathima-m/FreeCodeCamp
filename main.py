from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# Generate and save line plot
print("Generating line plot...")
line_fig = draw_line_plot()
print("Line plot saved as 'line_plot.png'")

# Generate and save bar plot
print("Generating bar plot...")
bar_fig = draw_bar_plot()
print("Bar plot saved as 'bar_plot.png'")

# Generate and save box plots
print("Generating box plots...")
box_fig = draw_box_plot()
print("Box plots saved as 'box_plot.png'")

print("All plots generated successfully!")
