#DriverTypedef.py file

from array import *
from dataclasses import dataclass

@dataclass
class color565_t:

    b:int
    g:int
    r:int
    color:int
                 
    
class font_t:
    width = 0
    height = 0
    first_char = 0
    last_char = 0
    chars = array('i',[])
    
#class image_t:
    #width = 0
    #height = 0
    #bytes_per_pix = 0
    #px_per_bytes = 0
    #pixels = array('i',[])