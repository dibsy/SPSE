#!/usr/bin/python

import immlib

DESC = "FastLogHook Demo"
NAME = "StrcpyFastLogHook"

def main(args) :

    imm = immlib.Debugger()

    fastHook = imm.getKnowledge(NAME)

    if fastHook :
        loggingResults = fastHook.getAllLog()
        imm.log(str(loggingResults))

        # let us parse the results now!

        (functionAddress, (esp, esp_4, esp_8)) = loggingResults[0]

        dataReceived = imm.readString(esp_8)

        imm.log(dataReceived)
        
        return "[+] Finished Fetching Results"
    
    
    # find strcpy address
    functionToHook = "msvcrt.strcpy"

    functionAddress = imm.getAddress(functionToHook)

    fastHook = immlib.FastLogHook(imm)

    fastHook.logFunction(functionAddress)

    fastHook.logBaseDisplacement('ESP', 0)
    fastHook.logBaseDisplacement('ESP', 4)
    fastHook.logBaseDisplacement('ESP', 8)

    fastHook.Hook()
    
    imm.addKnowledge(NAME, fastHook, force_add = 1)

    return "[+] Hook Added"


    
