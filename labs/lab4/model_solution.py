try:
    f = open ('c:/users/bbrel/basicpython/labs/lab4/data/albb.salaries.2003.formatted.csv')
except FileNotFoundError:
    print ("Invalid file!")
    quit()
    
team_dict = {}
try:
    for line in f:
        if len(line) == 4:
            break
        data = line.strip().split(',')
        try:
            if data[0] not in team_dict:
                team_dict[data[0]] = int(data[3])
            else:
                team_dict[data[0]] += int(data[3])
        except ValueError:
            continue
except IOError:
    print ("I/O Error raised!")
    quit()
finally:
    f.close()
    
team_name = input("Please enter a team name: ")
#if team_name not in team_dict:
#    print ("Invalid name! ", team_name)
#else:
#    print (team_dict[team_name])

try:
    print (team_dict[team_name])
except KeyError:
    print ("Invalid team name", team_name)
    