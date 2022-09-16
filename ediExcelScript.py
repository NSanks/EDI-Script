
"""
Nate Sanks 6/16/22
Excel EDI form manipulation script
v0.1
"""

import pandas as pd
import sys
import tkinter as tk
from tkinter import *


def fromCSV(filename):
    #open csv file, add columns, clean head
    df = pd.read_csv(filename)
    
    df.columns = ['CustPo#', 'DC', 'Order Ref', 'Code', 'Qty', 'total']
    df = df.drop(columns=['total'])
    df = df.iloc[1:,:]
    
    #insert two new cols
    df.insert(1, 'Prep', '')
    #df.insert(2, 'DC','')

    df['BoxQty']  = ''
    df['Box#'] = ''
    df['L'] = ''
    df['W'] = ''
    df['H'] = ''
    df['Cube'] = ''

    return df

def csvOut(df, filename):
    df.to_csv(filename, index = False)


def getLength():
    pass

def getWidth():
    pass
def getHeight():
    pass

def getType():
    pass


def main():
    
    def manip():
        inFile = inputtxt.get("1.0", 'end-1c')
        outFile = outputtxt.get("1.0", 'end-1c')
        dframe = fromCSV(inFile)
        csvOut(dframe, outFile)
        mainWindow.destroy()

    #create tkinter window
    mainWindow = tk.Tk()
    mainWindow.title('EDI modifier')
    mainWindow.geometry("300x200")
    
    
    #in/out textboxes
    l1 = Label(text = "Input filename")
    inputtxt = Text(mainWindow, height = 1, width = 25)
    l2 = Label(text = "Output filename")
    outputtxt = tk.Text(mainWindow, height = 1, width = 25)

    

    #manipulate button
    manipulate = Button(mainWindow, text = "Generate EDI file", command = lambda: manip())
    #get filename from command line

    # infile = sys.argv[1]
    # outfile = sys.argv[2]

    #ask user for filename

    csvFrame = fromCSV("newtestedi.csv")
    for col in csvFrame.columns:
        print(col)

    print(csvFrame)

    #output/save file
    #csvFrame.to_csv("testOut2Csv.csv", index=False)

    #change file

    #pack elements
    l1.pack()
    inputtxt.pack()
    l2.pack()
    outputtxt.pack()
    manipulate.pack()

    #keep tkinter window open
    mainWindow.mainloop()

    
if __name__ == "__main__":
    main()