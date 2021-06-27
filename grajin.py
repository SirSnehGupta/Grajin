import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import time
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def main():
    print('Welcome to Grajin!\nA CLI based graph generator.')
    print("\nWhich type of graph would you like?")
    print('1. Bar Graph\n2. Line Chart\n3. Pie Chart')
    print('0. Quit')
    graph_type = input("Enter your choice- ")
    if int(graph_type) == 1:
        bar_plot()
    elif int(graph_type) == 2:
        line_plot()
    elif int(graph_type) == 3:
        pie_plot()
    elif int(graph_type) == 0:
        sys.exit()
    else:
        pass

def bar_plot():
    bar_type = input("What type of bar graph would you like to create?\n1. Single\n2. Double\n--> ")
    cust = input("Customise plot?[Y/n] ")
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
        if cust.lower() == 'y' or cust == '':
            color = input('Choose from the following colors:\nBlue[b]\nCyan[c]\nGreen[g]\nBlack[k]\nMagenta[m]\nRed[r]\nWhite[w]\nYellow[y]\nEnter color code--> ')
            width = input('Enter width(default 0.8): ')
            if width == '' or type(float(width)) != float:
                print('Choosing default.')
                width = 0.8
            edcol = input('Choose from the following edge/border colors:\nBlue[b]\nCyan[c]\nGreen[g]\nBlack[k]\nMagenta[m]\nRed[r]\nWhite[w]\nYellow[y]\nEnter color code--> ')
            try:
                plt.bar(x, y, color = color, width = float(width), edgecolor = edcol)
            except ValueError:
                print('Errors in customisation detected, plotting with default constraints.')
                plt.bar(x, y)
        else:
            plt.bar(x, y)
        plt.xlabel(xlb)
        plt.ylabel(ylb)
        plt.title(title)
        print("Your graph has been opened in a new window, you can save it from there")
        time.sleep(1.5)
        plt.show()

    elif int(bar_type) == 2:
        x_raw = input("Enter comma separated values for X Axis(common set): ")
        y_raw = input("Enter comma separated values for Y Axis(1st set): ")
        y_raw2 = input("Enter comma separated values for Y Axis(2nd set): ")
        x = np.arange(len(x_raw.strip().strip(',').split(',')))

        y = pd.Series(y_raw.strip().strip(',').split(','), dtype = float)
        y2 = pd.Series(y_raw2.strip().strip(',').split(','), dtype = float)
        legend = input('Enable Legend?[Y/n] ')
        if cust.lower() == 'y' or cust == '':
            color1 = input('Choose from the following colors(Set-1):\nBlue[b]\nCyan[c]\nGreen[g]\nBlack[k]\nMagenta[m]\nRed[r]\nWhite[w]\nYellow[y]\nEnter color code--> ')
            edcol1 = input('Choose from the following edge/border colors(Set-1):\nBlue[b]\nCyan[c]\nGreen[g]\nBlack[k]\nMagenta[m]\nRed[r]\nWhite[w]\nYellow[y]\nEnter color code--> ')
            color2 = input('Choose from the following colors(Set-2):\nBlue[b]\nCyan[c]\nGreen[g]\nBlack[k]\nMagenta[m]\nRed[r]\nWhite[w]\nYellow[y]\nEnter color code--> ')
            edcol2 = input('Choose from the following edge/border colors(Set-2):\nBlue[b]\nCyan[c]\nGreen[g]\nBlack[k]\nMagenta[m]\nRed[r]\nWhite[w]\nYellow[y]\nEnter color code--> ')
            if legend.lower() == 'y' or legend == '':
                try:
                    lb1 = input('Label for 1st set: ')
                    lb2 = input('Label for 2st set: ')
                    plt.bar(x-0.2, y, width = 0.4, color = color1, edgecolor = edcol1, label = lb1)
                    plt.bar(x+0.2, y2, width = 0.4, color = color2, edgecolor = edcol2, label = lb2)
                except ValueError:
                    print('Errors in customisation detected, plotting with default constraints.')
                    lb1 = input('Label for 1st set: ')
                    lb2 = input('Label for 2st set: ')
                    plt.bar(x-0.2, y, width = 0.4, label = lb1)
                    plt.bar(x+0.2, y2, width = 0.4, label = lb2)
            else:
                try:
                    plt.bar(x-0.2, y, width = 0.4, color = color1, edgecolor = edcol1)
                    plt.bar(x+0.2, y2, width = 0.4, color = color2, edgecolor = edcol2)
                except ValueError:
                    print('Errors in customisation detected, plotting with default constraints.')
                    plt.bar(x-0.2, y, width = 0.4)
                    plt.bar(x+0.2, y2, width = 0.4)
        else:
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
        print("Your graph has been opened in a new window, you can save it from there")
        time.sleep(1.5)
        plt.show()
    clear()
    main()
        
def line_plot():
    cust = input("Customise plot?[Y/n] ")
    cycle = int(input("Enter no. of entries: "))
    for i in range(cycle):
        x_raw = input("Enter comma separated values for X Axis(Set-"+str(i+1)+"): ")
        y_raw = input("Enter comma separated values for Y Axis(Set-"+str(i+1)+"): ")
        try:
            x = eval(x_raw)
        except NameError: 
            x = x_raw.strip().strip(',').split(',')
        y = pd.Series(y_raw.strip().strip(',').split(','), dtype = float)
        lb = input("Label for this set: ")
        if cust.lower() == 'y' or cust == '':
            color = input("Choose from the following colors:\nBlue[b]\nCyan[c]\nGreen[g]\nBlack[k]\nMagenta[m]\nRed[r]\nWhite[w]\nYellow[y]\nEnter color code --> ")
            marker = input("Choose from the following list of markers:\n1. Point\n2. Circle\n3. Upward Triange\n4. Downward Triangle\n5. Star\n0. None\n--> ")
            if marker == '' or type(int(marker)) != int:
                print('Choosing default.')
                marker = 1
            mkr = {1:'.', 2:'o', 3:'^', 4:'v', 5:'*', 6:None}
            sty = {1:'-', 2:'--', 3:':', 4:'-.'}
            width = input('Enter width(default = 1): ')
            if width == '' or type(float(width)) != float:
                print('Choosing default.')
                width = 1
            style = input('Choose Linestyle:\n1. Solid\n2. Dashed\n3. Dotted\n4. Dash-Dot\n--> ')
            if style == '' or type(int(style)) != int:
                print('Choosing default.')
                style = 1
            try:
                plt.plot(x,y, label = lb, color = color, marker = mkr[int(marker)], linewidth = float(width), linestyle = sty[int(style)])
            except ValueError:
                print('Errors in customisation detected, plotting with default constraints.')
                plt.plot(x,y, label = lb)
        else:
            plt.plot(x,y, label = lb)
    xlb = input('Label for X Axis: ')
    ylb = input('Label for Y Axis: ')
    title = input('Title for the plot: ')
    plt.xlabel(xlb)
    plt.ylabel(ylb)
    plt.title(title)
    plt.legend()
    print("Your graph has been opened in a new window, you can save it from there")
    time.sleep(1.5)
    plt.show()
    clear()
    main()

def pie_plot():
    cust = input("Customise plot?[Y/n] ")
    categories = input("Enter categories(comma separated): ")
    labels = categories.strip().strip(',').split(',')
    sizes=[]
    colrs=[]
    for i in labels:
        size = input('Enter size for '+i+' category: ')
        if cust.lower() == 'y' or cust == '':
            color = input("Choose from the following colors:\nBlue[b]\nCyan[c]\nGreen[g]\nBlack[k]\nMagenta[m]\nRed[r]\nWhite[w]\nYellow[y]\nEnter color code --> ")
            colrs.append(color)
            
        try:
            sizes.append(float(size))
        except ValueError:
            print("Not a Number")

    if cust.lower() == 'y' or cust == '':
        shad = input("Enable shadow?[Y/n] ")
        if shad.lower() == 'y' or shad == '':
            shad = True
        else:
            shad = False
        try:
            plt.pie(sizes, labels = labels, colors = colrs, shadow = shad)
        except ValueError:
            plt.pie(sizes, labels = labels)
    else:    
        plt.pie(sizes, labels = labels)
    print("Your graph has been opened in a new window, you can save it from there")
    time.sleep(1.5)
    plt.show()
    clear()
    main()
      
if __name__ == '__main__':
    main()