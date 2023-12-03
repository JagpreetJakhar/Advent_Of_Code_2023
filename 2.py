
#----Part 1----#
# which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

with open('d:\\work\\Advent_Of_Code_2023\\2_input.txt') as f:
    lines = f.readlines()
game_id_sum = 0
red_lim = 12
green_lim = 13
blue_lim = 14
run = 3
for line in lines:
    #print(line)
    game_id = 0
    red_balls =0
    green_balls =0
    blue_balls =0
    line = line.split()
    #print(line)
    for s,j in enumerate(line):
        #print(s,j)
        #print(s,j)
        if 'Game' in j:
            game_id = line[s+1].split(':')[0]
            #print(game_id)
        if 'red' in j:
            red_balls +=int(line[s-1])
            #print('red_balls:',red_balls)
        if 'green' in j:
            green_balls += int(line[s-1])
           
        if 'blue' in j:
            blue_balls += int(line[s-1])
        if red_balls > red_lim or green_balls > green_lim or blue_balls > blue_lim:
            #print('breaked',game_id)
            game_id =0
            break
        if ';' in j:
            red_balls =0
            green_balls =0
            blue_balls =0
        #print(red_balls, green_balls, blue_balls)
        if red_balls > red_lim or green_balls > green_lim or blue_balls > blue_lim:
            #print('breaked',game_id)
            game_id =0
            break
            
    
    #print(game_id)
    game_id_sum += int(game_id)
    
  
    #print(red_balls, green_balls, blue_balls, game_id)
    #print(line)
    
print(game_id_sum)

# ans : 2061


#----Part 2----#    

powers = 0
power_sum =0
for line in lines:
    #print(line)
    min_red, min_green, min_blue = None, None, None
    game_id = 0
    red_balls =0
    green_balls =0
    blue_balls =0
    line = line.split()
    #print(line)
    for s,j in enumerate(line):
        #print(s,j)
        #print(s,j)
        if 'red' in j:
            red_balls +=int(line[s-1])
            #print('red_balls:',red_balls)
        if 'green' in j:
            green_balls += int(line[s-1])
           
        if 'blue' in j:
            blue_balls += int(line[s-1])
        
        if ';' in j or s == len(line)-1:
            if min_red == None:
                min_red = red_balls
            if min_green == None:
                min_green = green_balls
            if min_blue == None:
                min_blue = blue_balls
            if red_balls > min_red:
                min_red = red_balls
            if green_balls > min_green:
                min_green = green_balls
            if blue_balls > min_blue:
                min_blue = blue_balls
            # 
            red_balls =0
            green_balls =0
            blue_balls =0
    #print(min_red, min_green, min_blue)
        #print(red_balls, green_balls, blue_balls)
         
    powers = min_red*min_green*min_blue
    #print(powers)
    power_sum += powers
    #print(power_sum)
    #break
print(power_sum)
# ans : 72596