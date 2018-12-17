import socket,datetime

print("""
 _______  _______  _______ _________ _______  _______  _______  _         
(  ____ )(  ___  )(  ____ )\__   __/(  ____ \(  ____ \(  ___  )( (    /|  
| (    )|| (   ) || (    )|   ) (   | (    \/| (    \/| (   ) ||  \  ( |  
| (____)|| |   | || (____)|   | |   | (_____ | |      | (___) ||   \ | |  
|  _____)| |   | ||     __)   | |   (_____  )| |      |  ___  || (\ \) |  
| (      | |   | || (\ (      | |         ) || |      | (   ) || | \   |  
| )      | (___) || ) \ \__   | |   /\____) || (____/\| )   ( || )  \  |  
|/       (_______)|/   \__/   )_(   \_______)(_______/|/     \||/    )_)                                                                          
""")
print("Auteur : Lucas")
print("------------------------------------------------------------------------")
print("Cet outil permet de faire un scan de port sur un range de port et une IP")
print("------------------------------------------------------------------------")

#--------------------------------------------------------------------------------
#On demande l'ip et le range de ports � l'utilisateur
#--------------------------------------------------------------------------------
rHost = str(raw_input("\n\nIP a scanner (10.101.200.28) : "))
rPortMin = int(raw_input("D�but de la plage de port � scanner : "))
rPortMax = int(raw_input("Fin de la plage de port � scanner : "))


#--------------------------------------------------------------------------------
#Fonction qui ouvre un socket sur l'ip et le port pass�s en param�tres
#--------------------------------------------------------------------------------
def scan (Host, Port) :
    ip = Host
    port = Port
    #d�nition des ports principaux
    ports={21:"FTP",22:"FTP",23:"SSH",25:"SMTP",53:"DNS",80:"HTTP",111:"ONCRPC",139:"NetBIOS"}
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, port))
        print ("Port {} ouvert ".format(port) + ports[port])#si le port est ouvert on l'affiche
    except socket.error:
        print "Port {} ferm� ".format(port)                 #si le port est ferm� on l'affiche


#--------------------------------------------------------------------------------
#Boucle qui lance la fonction scan avec ip et port en argument
#--------------------------------------------------------------------------------
heure=datetime.datetime.now()   #mise en variable de l'heure avant l'�x�cution du scan

while rPortMin <= rPortMax :    
    scan (rHost,rPortMin)       
    rPortMin=rPortMin+1         #incr�menetation du port � scanner


#--------------------------------------------------------------------------------
#on calcul et on affiche le temps d'�x�cution du programme
#--------------------------------------------------------------------------------
temps=datetime.datetime.now()-heure         
print("\nTemps d'execution : " + str(temps))
