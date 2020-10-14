#!/usr/bin/env python3
# This is the solution provided by instructor

def read_pgm(filename):
    with open(filename,'r') as fp:
        content = fp.read()
        content = content.split()
    return (content[0:4],content[4:])


def write_pgm(filename,content):
    with open(filename,'w') as fp:
        for line in content[0]+content[1]:
            fp.write('{}\n'.format(line))


def invert_helper(input_string):
    return str(255-int(input_string))
  

# This probably won't work with check.py's unittest, but it is a correct solution
def invert(content):
    #content = (content[0],list(map(invert_helper,content[1])))
    content[1][:] = map(invert_helper,content[1])
    
    
if __name__ == '__main__':
    pass
