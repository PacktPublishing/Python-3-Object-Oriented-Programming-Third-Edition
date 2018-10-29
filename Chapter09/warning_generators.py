import sys

# generator expression
inname, outname = sys.argv[1:3]

with open(inname) as infile:
    with open(outname, "w") as outfile:
        warnings = (
            l.replace("\tWARNING", "") for l in infile if "WARNING" in l
        )
        for l in warnings:
            outfile.write(l)

# normal loop
with open(inname) as infile:
    with open(outname, "w") as outfile:
        for l in infile:
            if "WARNING" in l:
                outfile.write(l.replace("\tWARNING", ""))


# object-oriented
class WarningFilter:
    def __init__(self, insequence):
        self.insequence = insequence

    def __iter__(self):
        return self

    def __next__(self):
        l = self.insequence.readline()
        while l and "WARNING" not in l:
            l = self.insequence.readline()
        if not l:
            raise StopIteration
        return l.replace("\tWARNING", "")


with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = WarningFilter(infile)
        for l in filter:
            outfile.write(l)


# Generator with yield
def warnings_filter(insequence):
    for l in insequence:
        if "WARNING" in l:
            yield l.replace("\tWARNING", "")


with open(inname) as infile:
    with open(outname, "w") as outfile:
        filter = warnings_filter(infile)
        for l in filter:
            outfile.write(l)


# Generator with yield from
def warnings_filter(infilename):
    with open(infilename) as infile:
        yield from (
            l.replace("\tWARNING", "") for l in infile if "WARNING" in l
        )


filter = warnings_filter(inname)
with open(outname, "w") as outfile:
    for l in filter:
        outfile.write(l)
