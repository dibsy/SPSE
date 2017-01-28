#!/usr/bin/env python

import immlib
from immlib import BpHook

DESC = "BpHook Basic Demonstration for the SPSE course"

class StrcpyBpHook(BpHook) :

    def __init__(self) :
        BpHook.__init__(self)

    def run(self, regs):

        imm = immlib.Debugger()
        imm.log("StrcpyBpHook Called!")

        # strcpy(char *destination, char *source)

        eipOnStack = imm.readLong(regs['ESP'])
        strcpyFirstArg = imm.readLong(regs['ESP'] + 4)
        strcpySecondArg = imm.readLong(regs['ESP'] + 8)

        imm.log("EIP on Stack: 0x%08x  First Arg: 0x%08x Second Arg: 0x%08x " %(eipOnStack, strcpyFirstArg, strcpySecondArg))
        
        # pring the source string

        receivedString = imm.readString(strcpySecondArg)

        imm.log(receivedString)

        imm.log("Received String: %s with length %d" % (str(receivedString), len(receivedString)))
        



def main(args) :
    imm = immlib.Debugger()

    # find strcpy address
    functionToHook = "msvcrt.strcpy"

    functionAddress = imm.getAddress(functionToHook)

    newHook = StrcpyBpHook()

    newHook.add(functionToHook, functionAddress)


    imm.log("Hook for %s : 0x%08x added successfully!" % (functionToHook, functionAddress))
    
    return "Hook Installed"

    
