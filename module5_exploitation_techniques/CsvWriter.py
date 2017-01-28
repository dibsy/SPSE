#!/usr/bin/env python

import immlib, csv

DESC = "Write Process List Data to CSV File"

def main(args) :

    imm = immlib.Debugger()

    csvWriter = csv.writer(open("C:\Program Files\Immunity Inc\Immunity Debugger\PyCommands\ps.csv", "wb"))
    # Write column names

    csvWriter.writerow(["PID", "Process", "Path"])
    psList = imm.ps()

    for process in psList :
        csvWriter.writerow([ str(process[0]), str(process[1]), str(process[2]) ])
        

    return "[+] Process Listing dumped to ps.csv"

