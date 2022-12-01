from dataclasses import dataclass 

@dataclass
class nodetype:
    parent:int=None
    depth:int=None

@dataclass
class edge:
    first:int=None
    second:int=None
    weight:int=None

a=edge(1,2,3)
b=nodetype(1,3)
print(b)
