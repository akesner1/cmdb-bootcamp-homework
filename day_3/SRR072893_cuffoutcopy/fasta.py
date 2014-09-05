import sys     #this lets you read the stdin and stdout 

class FASTAReader(object):      # makine a new type of thing, FASTAReader is not a "normal" thing, so we're making it
    def __init__( self, file ):   #initializes state of object... YOU ALWAYS pass self as the first arguement, then file is what we need to keep track of
        self.file = file
        self.last_sid = None
    def next( self ):
        if self.last_sid is None:
            line = sys.stdin.readline()   #read first line in the file
            assert line.startswith( ">" )  # makes sure this is the line we expect
            sid = line[1:].rstrip("\r\n")  # take first character off string, and strip new line characters off end of thestring
        else:
            sid = self.last_sid


        sequences = []                  # creat a lsit to acuumulate data into
        while True:
            line = sys.stdin.readline()  #keep reading lines of the file
            if line == "" and not sequences:
                raise StopIteration     #special break when using iterators
            if line.startswith(">") or line == "":
                self.last_sid = line[1:].rstrip("\r\n")    #saves on our object this last id line
                break                      #if the line begins with a header, stop
            else:
                sequences.append( line.strip() )   #strips all white space from sequence
            sequence = "".join( sequences )          #joins all things in the list, concatonates the list
        return sid, sequence
    def __iter__( self ):
        return self


#### this is now a fasta parser module