import re

class DiffCommands:
    def __init__(self,diff_file):
        self.diff_file = diff_file
        
        
        previous_positions=[]
        new_positions=[]
        half_1=[]
        haf_2=[]
        half_1_f=[]
        half_2_f=[]
        current_l=[]
        current_r=[]
        global lines
        lines=[]
        comp_positions_left=[0,0]
        positions_left=[]
        positions_right=[]
        comp_positions_right=[0,0]

        
        
##        with open(self.diff_file, 'r') as file:
##            lines = file.readlines().splitlines()
        lines=open(self.diff_file).read().splitlines()      

        for line in lines:
            delete=1
            change=1
            add=1
            change=re.match('^(\d+)(?:,(\d+))?c(\d+)(?:,(\d+))?$', line)
            add=re.match('^(\d+)a(\d+)(?:,(\d+))?$', line)
            delete=re.match('^(\d+)(?:,(\d+))?d(\d+)$', line)
            
            
            if delete==None and change==None and add==None:
                raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')
            
            all_checks = re.match('^(\d+)(?:,(\d+))?[acd](\d+)(?:,(\d+))?$', line)  
            line_values=list(all_checks.groups())
            half_1=line_values[0:int(len(line_values)/2)]#changed for you, see :)  
            half_2=line_values[int(len(line_values)/2):]
            half_1_f=[]
            half_2_f=[]
##                print(half_1,half_2)
            for i in range(len(half_1)):
                if half_1[i]!=None:
                    half_1_f.append(int(half_1[i]))
                else:
                    half_1_f.append((half_1[i]))
            for j in range(len(half_2)):
                if half_2[j]!=None:
                    half_2_f.append(int(half_2[j]))
                else:
                    half_2_f.append((half_2[i]))
            
            
        
            if delete:
                for i in range(2):
                    if i==0:
                        current_l.append(half_1_f[i]-1)
                    elif i==1 and half_1_f[i]!=None:
                        current_l.append((half_1_f[i]))
                    elif i==1 and half_1_f[i]==None:
                        current_l.append((half_1_f[i-1]))
                    if i==0:
                        current_r.append(half_2_f[i])
                    if i==1 and half_2_f[i]==None:
                        current_r.append(half_2_f[i-1])
                    
                
                               
                
            if add:
                for i in range(2):
                    if i==0:
                        current_l.append(half_1_f[i])
                        current_r.append(half_2_f[i]-1)
                    if i==1 and half_1_f[i]==None:
                        current_l.append(half_1_f[i-1])
                        
                    if i==1 and half_2_f[i]!=None:
                        current_r.append(half_2_f[i])
                    elif i==1 and half_2_f[i]==None:
                        current_r.append((half_2_f[i-1]))
                        

            if change:
                for i in range(2):
                    if i==0:
                        current_l.append(half_1_f[i]-1)
                    if i==1 and half_1_f[i]!=None:
                        current_l.append(half_1_f[i])
                    elif i==1 and half_1_f[i]==None:
                        current_l.append(half_1_f[i-1])

                    if i==0:
                        current_r.append(half_2_f[i]-1)
                    if i==1 and half_2_f[i]!=None:
                        current_r.append(half_2_f[i])
                    elif i==1 and half_2_f[i]==None:
                        current_r.append(half_2_f[i-1])
                        
                  
                

            if comp_positions_left[1]==0 and comp_positions_right[1]==0:
                if not (current_l[0]-comp_positions_left[1]==current_r[0]-comp_positions_right[1]):
                    raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')
                    
            else:
                if not (current_l[0]-comp_positions_left[1]==current_r[0]-comp_positions_right[1] and current_l[0]-comp_positions_left[1]>0):
                    raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')

            comp_positions_left=current_l
            comp_positions_right=current_r
            current_l=[]
            current_r=[]


                
    def __str__(str):
        commands=''
        for line in range(len(lines)):
            if line!=len(lines)-1:
                commands+=lines[line]+'\n'
            else:
                commands+=lines[line]
        return commands
            
                    
class DiffCommandsError(Exception):
    def __init__(self, message):
        self.message = message                    
                    
                    
                    

        
            
            
        



            
            
            
       
        
        
        
