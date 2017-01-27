import os

def traverse(dir_path,seperator):
  #print list_contents
  dir_count=0
  for f in os.listdir(dir_path):
    if os.path.isdir(dir_path+"/"+f):
      dir_count+=1
      
    #print str(dir_count)
  if dir_count==0:
    return "x"
    
    
  temp = os.listdir(dir_path)
  dir_contents = []
  for f in temp:
    dir_contents.append(dir_path+"/"+f)
    
  for f in dir_contents:
    
    i=f.rfind("/")
    print seperator+f[i+1:]
    
    #print seperator+f
    if os.path.isdir(f):
      traverse(f,seperator*2)
    
      
  

  

  


dir_path="/etc"
seperator = "----"
print dir_path
traverse(dir_path,seperator)
    

#def traverse(dir_path,sep):
#  for f in os.listdir(dir_path):
#    if os.path.isdir(f):  

#recursive version 
#base condition should be there should be no directories in the list 


                                                                                                                                                                                                                                  
