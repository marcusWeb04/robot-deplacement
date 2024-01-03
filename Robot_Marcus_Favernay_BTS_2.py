# il faut utiliser la version 3.10 au minimum

# On enregistre les valeurs à l'intérieur d'une liste
with open("instruction.txt") as file:
    lines = file.readlines()

# on initialise nos varibles
    
# les valeurs que l'on va afficher
robot = None
ord = None

# les valeurs x et y de notre robot
robot_x = None
robot_y = None


# les valeurs max x et y
max_x = lines [0][0]
max_y = lines [0][1]

max_x = int(max_x)
max_y = int(max_y)


# on parcours les instructions
for position in lines:

    # on affiche les coordonées et l'orientation si robot n'est pas num
    if robot is not None:
        print(robot,ord)

    # on parcours notre tableau position
    for i in range(len(position)):
        #si notre case est vide on récupère les 2 valeurs précédents et la valeurs suivants via aux indices
            if position[i] == " ":
                robot_x = position[i-2] 
                robot_y = position[i-1]
                robot_x = int(robot_x)
                robot_y = int(robot_y)
                ord = position[i+1]

            #si la valeur est égal à D, l'on change la valeurs dans ord
            elif position[i] == "D":
                match ord:
                    case "N":
                        ord = "E"
                    case "E":
                        ord = "S"
                    case "S":
                        ord = "W"
                    case "W":
                        ord = "N"

            # #si la valeur est égal à G, l'on change la valeurs dans ord
            elif position[i] == "G":
                match ord:
                    case "N":
                        ord = "W"
                    case "W":
                        ord = "S"
                    case "S":
                        ord = "E"
                    case "E":
                        ord = "N"

            #si la valeur est égal à A, l'on change la valeurs à l'interieur de nos variables
            elif position[i] == "A":

                # si les coordonnée x de mon robot sont supérieur 0 et inférieur à x
                if robot_x > 0 and robot_x < max_x:
                    match ord:
                        case "W":
                            robot_x-=1
                        case "E":
                            robot_x+=1
                
                # si les coordonnées y de mon robot sont supérieur 0 et inférieur à u
                if robot_y > 0 and robot_y < max_y:
                    match ord:
                        case "S":
                            robot_y-=1
                        case "N":
                            robot_y+=1

                # si les coordonnées de mon robot x sont égal à 0
                if robot_x == 0:
                    match ord:
                        case 'E' :
                                robot_x +=1

                # si les coordonnées de mon robot y sont égal à 0
                if robot_y == 0:
                    match ord:
                        case 'N':
                                robot_y +=1

                # si les coordonnées de mon robot x sont égal à x
                if robot_x == max_x:
                    match ord:
                        case "W":
                            robot_x-=1

                # si les coordonnées de mon robot y sont égal à 0
                if robot_y == max_y:
                    match ord:
                        case "S":
                            robot_y-=1



            # si les coordonnées de mon robot en x et y ne sont pas null
            if robot_x is not None and robot_y is not None:
                robot = f"{robot_x}{robot_y}"
                robot = int(robot)
            
            

# on affiche les coodonnées final et l'orientation
print(robot,ord)

# fin du traitement du programme / L'utilisateur doit appuyer sur le bouton entrer afin que le programme puisse se fermer
input("Fin du traitement")