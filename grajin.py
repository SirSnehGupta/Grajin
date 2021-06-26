import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    print('Welcome to Grajin!\nA CLI based graph generator.\n')
    print("Which type of graph would you like?")
    print('1. Bar Graph\n2. Line Chart\n3. Histogram\n4. Pie Chart')
    graph_type = input("Enter your choice- ")
    if int(graph_type) == 1:
        bar_plot()
    elif int(graph_type) == 2:
        line_plot()
    else:
        pass

def bar_plot():
    bar_type = input("What type of bar graph would you like to create?\n1. Single\n2. Double\n--> ")
    if int(bar_type) == 1:
        x_raw = input("Enter comma separated values for X Axis: ")
        y_raw = input("Enter comma separated values for Y Axis: ")
        try:
            x = eval(x_raw)
        except NameError: 
            x = x_raw.strip().strip(',').split(',')
        try:
            y = eval(y_raw)
        except NameError:
            y = y_raw.strip().strip(',').split(',')
        xlb = input('Label for X Axis: ')
        ylb = input('Label for Y Axis: ')
        title = input('Title for the plot: ')
        plt.bar(x, y)
        plt.xlabel(xlb)
        plt.ylabel(ylb)
        plt.title(title)
        print("Here's your graph")
        plt.show()
    elif int(bar_type) == 2:
        x_raw = input("Enter comma separated values for X Axis(common set): ")
        y_raw = input("Enter comma separated values for Y Axis(1st set): ")
        y_raw2 = input("Enter comma separated values for Y Axis(2nd set): ")
        x = np.arange(len(x_raw.strip().strip(',').split(',')))

        y = pd.Series(y_raw.strip().strip(',').split(','), dtype = float)
        y2 = pd.Series(y_raw2.strip().strip(',').split(','), dtype = float)
        legend = input('Enable Legend?[Y/n] ')
        if legend.lower() == 'y' or legend == '':
            lb1 = input('Label for 1st set: ')
            lb2 = input('Label for 2st set: ')
            plt.bar(x-0.2, y, width = 0.4, label = lb1)
            plt.bar(x+0.2, y2, width = 0.4, label = lb2)
        else:
            plt.bar(x-0.2, y, width = 0.4)
            plt.bar(x+0.2, y2, width = 0.4)
        plt.xticks(x, x_raw.strip().strip(',').split(','))
        xlb = input('Label for X Axis: ')
        ylb = input('Label for Y Axis: ')
        title = input('Title for the plot: ')
        plt.xlabel(xlb)
        plt.ylabel(ylb)
        plt.title(title)
        plt.legend()
        print("Here's your graph")
        plt.show()
        
def line_plot():
    cycle = int(input("Enter no. of entries: "))
    for i in range(cycle):
        x_raw = input("Enter comma separated values for X Axis: ")
        y_raw = input("Enter comma separated values for Y Axis: ")
        try:
            x = eval(x_raw)
        except NameError: 
            x = x_raw.strip().strip(',').split(',')
        y = pd.Series(y_raw.strip().strip(',').split(','), dtype = float)
        lb = input("Label for this set: ")
        plt.plot(x,y, label = lb)
    xlb = input('Label for X Axis: ')
    ylb = input('Label for Y Axis: ')
    title = input('Title for the plot: ')
    plt.xlabel(xlb)
    plt.ylabel(ylb)
    plt.title(title)
    plt.legend()
    print("Here's your graph")
    plt.show()
        


if __name__ == '__main__':
    main()