from random import *

start = '''
***************************************************************************************
                                                                                         
                                                                                         

                         __       ___        ___                                                 
        /\              /  \     /   \      /   \       |                                    
       /  \            /        /     \    /     \      |                                                                    
      /____\          |         |     |    |     |      |                                   
     /      \          \        \     /    \     /      |                                    
    /        \          \__/     \___/      \___/       |_____                                        
                                                                                         



           __                                     ______                                          
          /  \         /\        |\        /|    |               |                             
         /            /  \       | \      / |    |               |                                                                                                                      
         |   __      /____\      |  \    /  |    |----           |                                                                                                                             
         \    |     /      \     |   \  /   |    |                                          
          \__/     /        \    |    \/    |    |______         #                                       
                                                                                       

                                                                                                                                                                                  
                                                                                         

***************************************************************************************
'''
town_map1 = '''
                                                                                                                                                                                                         
                                                                                           
                                                                                         
     /\                 /\           /\          /\          /\                                                 
    /  \               /  \         /  \        /  \        /  \                                              
   /    \             /    \       /    \      /    \      /    \                                             
  /|    |\           /|    |\     /|    |\    /|    |\    /|    |\                                                       
   |    |             |    |       |    |      |    |      |    |                                                         
   |    |             |    |       |    |      |    |      |    |




'''
                                                                                     
                                                                                         
town_map2 = '''
                                                                                                                                                                                                         
                                                                                           
                                                                                         
     /\                  /\           /\          /\          /\                                                 
    /  \                /  \         /  \        /  \        /  \                                              
   /    \              /    \       /    \      /    \      /    \                                             
  /|    |\            /|    |\     /|    |\    /|    |\    /|    |\       ____                                                
   |    |              |    |       |    |      |    |      |    | - - - |    |                                                 
   |    |              |    |       |    |      |    |      |    |       |____|
                                                                           |
                                                                           |
                                                                          ___
                                                                         |   |
                                                                         |___|

'''
import time

sword = False
slingshot = False
ammo = 0
torch = False
enemy_1_dead = False
enemy_2_dead = False
key_1 = False
key_2 = False
locked_1_open = False
locked_2_open = False
food = False
houses_visited = []


while True:
    if '1' not in houses_visited:
        print("You stumble into your house, you open the door and you find one


                                                                                                                                                                                                                                         
