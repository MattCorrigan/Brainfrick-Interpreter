import sys, os, os.path

import termios
import fcntl


# credit for this function goes to the internet
# reads one character from stdin
def getch():
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    try:        
        while 1:            
            try:
                c = sys.stdin.read(1)
                break
            except IOError: pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
    return c




if len(sys.argv) < 2:
    print("Please specify an input file.")
    sys.exit()

filename = sys.argv[1]
   
if not os.path.exists(filename):
    print("Could not open file.")
    sys.exit()

lines = open(filename, "r").readlines()

class Program:
    def __init__(self):
        self.data = []
        self.data.append(0)
        self.pointer = 0
        
        self.skipping = True
        self.matching_num = 0
        
        self.chars = []
        self.char_num = 0
        
    def addchar(self, c):
        self.chars.append(c)
        
    def run(self):
        while self.char_num < len(self.chars):
            self.process(self.chars[self.char_num])
            self.char_num += 1
    
    def process(self, c):
        if c == "+":
            self.data[self.pointer] += 1
        elif c == "-":
            self.data[self.pointer] -= 1
        elif c == ",":
            input_c = getch()
            self.data[self.pointer] = ord(input_c)
        elif c == ".":
            print(chr(self.data[self.pointer]), end="")
        elif c == ">":
            self.pointer += 1
            if len(self.data) - 1 < self.pointer:
                self.data.append(0)
        elif c == "<":
            self.pointer -= 1
            if self.pointer == -1:
                self.data.insert(0, 0)
                self.pointer = 0
        elif c == "[":
            if not self.data[self.pointer] == 0:
                return
            while self.matching_num >= 0:
                self.char_num += 1
                if self.chars[self.char_num] == "[":
                    self.matching_num += 1
                elif self.chars[self.char_num] == "]":
                    self.matching_num -= 1
            self.matching_num = 0
        elif c == "]":
            if self.data[self.pointer] == 0:
                return
            while self.matching_num >= 0:
                self.char_num -= 1
                if self.chars[self.char_num] == "[":
                    self.matching_num -= 1
                elif self.chars[self.char_num] == "]":
                    self.matching_num += 1
            self.matching_num = 0
p = Program()
for line in lines:
    for c in list(line):
        p.addchar(c)
p.run()
