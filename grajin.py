import matplotlib.pyplot as plt

def main():
    print('Welcome to Grajin!\nA CLI based graph generator.\n')
    print("Which type of graph would you like?")
    print('1. Bar Graph\n2. Line Chart\n3. Histogram\n4. Pie Chart')
    graph_type = input("Enter your choice- ")
    if int(graph_type) == 1:
        bar_plot()
    else:
        pass

def bar_plot():
    bar_type = input("What type of bar graph would  you like to create?\n1. Default\n2.Double\n--> ")
    if int(bar_type) == 1:
        x_raw = input("Enter comma separated values for X Axis: ")
        y_raw = input("Enter comma separated values for Y Axis: ")
        try:
            x = eval(x_raw)
        except NameError: 
            x = x_raw.strip().split(',')
        try:
            y = eval(y_raw)
        except NameError:
            y = y_raw.strip().split(',')
        xlb = input('Label for X Axis: ')
        ylb = input('Label for Y Axis: ')
        title = input('Title for the plot: ')
        plt.bar(x,y)
        plt.xlabel(xlb)
        plt.ylabel(ylb)
        plt.title(title)
        print("Here's your graph")
        plt.show()
    else:
        pass

if __name__ == '__main__':
    main()