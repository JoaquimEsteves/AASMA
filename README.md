# AASMA

Default car velocity: FIX ME
Default pawn velocity: FIX ME (probably 1 or 0,5)

Sensor: 
        -see all positions untill a wall is met or the end of the map;
        -check x number of positions ahead
        -to check if there are people near the zebra, must check "diagonal positions" ie +1 in the car's orientation and 
        +1/-1 on the other orientation
        
 Define critical zones such as: zebras, crossings (use right hand rule), roundabouts, walls
 
 Handling critical zones:
    
    Roundabouts: define max velocity, eg, in each cycle it will only run 2 or 1 positions
                 slow down before arriving to the roundabout (1 position). At the entrance check for cars in the position (+1, -1), 
                 if a car exists, stop for 2 cycles, recheck again in the next 2 cycles.
                 elif check if car ahead (+1), wait for 1 cycle if there is and recheck in the next cycle
                 else move
                 
                 inside it, move freely
                 
    Walls:
                always turn left when finding an obstacle in the position ahead.
                
    Crossings:
                all cars slow down.
                if car wants to turn right, check position ahead, if car wait for 1 cycle and recheck
                else move
                
                if car wants to go forward, check if there's car in the position before the entrance on the right (+2, +1)
                     or a car ahead of him (+1,+0) THERES A HUGE DEMON HERE: IF 4 CARS APPEAR AT THE SAME TIME IN DIFFERENT
                                                    ENTRANCES!!!!!
                     
                     
                if car wants to turn left-> check position ahead, if car wait for 1 cycle and recheck or if there's car                                                         in the position before the entrance on the right (+2, +1), wait 1 cycle and recheck, or there's a car in the position (+3, -1) wait 1 cycle at the entrance
                  HANDLE CHECKLIGHTS AFTER ALL THIS IS DONE (some more ifs getters nothing hard)
                  
                
             
                
 
