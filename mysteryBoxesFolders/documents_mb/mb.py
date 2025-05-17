# author : Tidjani D.
# date : 16-04-2024

monNombreDePiecesCachees = []
mesCasesCachees = []
mesCasesVoisines = []
mesCasesCacheestemp = []
casesVides = []

# La fonction "init()" est la fonction qui déclenche tout le processus de mise 
# en place du jeu. Elle est appelée lorsque la page se charge ou lorsque
# l'on clique sur le bouton "Nouvelle partie" ou encore pour relancer le jeu 
# lorsque le joueur a gagné ou perdu une partie.

def init():
    global mesCasesCacheestemp 
    global casesVides
    monNombreDePiecesCachees.append(nombreDePiecesCachees())
    mesCasesCachees.append(casesCachees())
    mesCasesCacheestemp = mesCasesCachees[len(mesCasesCachees)-1].copy()
    mesCasesVoisines.append(casesVoisines())
    main = document.querySelector("#main")
    main.innerHTML = monHTML()
    placerPiecesCachees()
    indices()
    casesVides = []


# La fonction "monHTML()" permet tout simplement de charger le contenu HTML
# du jeu, avec le tableau, les images, le nombre d'erreurs, de sous cachées,
# etc.

def monHTML():
    monHTMLtemp = []
    monHTMLtemp.append('<div class="bouton">')
    monHTMLtemp.append('<button onclick="init()">New game</button>')
    monHTMLtemp.append('</div>')
    monHTMLtemp.append('<div class="play">')
    monHTMLtemp.append('<h3 class="infos">Play!</h3>')
    monHTMLtemp.append('</div>')
    monHTMLtemp.append('<div class="headRules">')
    monHTMLtemp.append('<div>Read the rules <a href="guide.html">here</a>.')
    monHTMLtemp.append('</div>')
    monHTMLtemp.append('</div>')
    monHTMLtemp.append('<div class="theHead">')
    monHTMLtemp.append('<div>')
    errorOpen = '<h4><span class="errorTitle">Errors</span> :'
    monHTMLtemp.append(errorOpen)
    pOpen1 = '<p class="error">'
    monHTMLtemp.append(pOpen1)
    monHTMLtemp.append(str(0))
    pClose1 = '</p>'
    monHTMLtemp.append(pClose1)
    errorClose = '</h4>'
    monHTMLtemp.append(errorClose)
    sousCacheesOpen = '<h4><span class="nombreTitle">Number of hidden coins</span> :'
    monHTMLtemp.append(sousCacheesOpen)
    pOpen2 = '<p class="nombre">'
    monHTMLtemp.append(pOpen2)
    monHTMLtemp.append(str(monNombreDePiecesCachees[len(monNombreDePiecesCachees)-1]))
    pClose2 = '</p>'
    monHTMLtemp.append(pClose2)
    sousCacheesClose = '</h4>'
    monHTMLtemp.append(sousCacheesClose)
    monHTMLtemp.append('</div>')
    monHTMLtemp.append('</div>')
    monHTMLtemp.append('<div class="headJeu">')
    monHTMLtemp.append('<div id="jeu" class="centered">')
    monHTMLtemp.append('<div class="theTable">')
    tableOpen = '<table>'
    monHTMLtemp.append(tableOpen)
    for i in range(10):
        unTR = '<tr>'
        monHTMLtemp.append(unTR)
        for j in range(10):
            if i == 0:
              unTD = '<td onclick="clic('+str(j)+')"' + 'id="case' + str(j) + '">' +'</td>'
              monHTMLtemp.append(unTD)
            else:
              unTD = '<td onclick="clic('+str(i)+str(j)+')"' 'id="case' + str(i) + str(j) + '">' +'</td>'
              monHTMLtemp.append(unTD)
        unTRclose = '</tr>'
        monHTMLtemp.append(unTRclose)
    tableClose = '</table>'
    monHTMLtemp.append(tableClose)
    monHTMLtemp.append('</div>')
    monHTMLtemp.append('</div>')
    monHTMLtemp.append('</div>')
    monHTMLtemp.append('<div class="headCopyright">')
    monHTMLtemp.append('<div class="copyright">© 2024 Mystery Boxes™ | Built by Tidjani. All rights reserved.')
    monHTMLtemp.append('</div>')
    monHTMLtemp.append('</div>')
    monHTMLtemp.append('<div class="logo">')
    monHTMLtemp.append('<img src="symboles/logo2.png">')
    monHTMLtemp.append('</div>')
    monHTML = '\n'.join(monHTMLtemp)
    return monHTML


# La fonction "nombreDePiecesCachees()" permet de déterminer le nombre aléatoire
# de pièces cachées à chaque nouvelle partie.

def nombreDePiecesCachees():
    nombre = math.floor(random()*16)
    while nombre < 10 or nombre >16:
        nombre = math.floor(random()*16)
    return nombre

# La fonction "testNombreDePiecesCachees()" est la fonction de tests unitaires de la fonction
# "nombreDePiecesCachees()"

def testNombreDePiecesCachees():
    possibilites = [15,16,17,18,19,20]
    assert nombreDePiecesCachees() in possibilites
    assert nombreDePiecesCachees() in possibilites
    assert nombreDePiecesCachees() in possibilites
    assert nombreDePiecesCachees() in possibilites
    assert nombreDePiecesCachees() in possibilites

# La fonction "casesCachees()" permet de déterminer les places des pièces 
# cachées dans le tableau tout en respectant les exigences du jeu.

def casesCachees():
    randomNumbers = []
    while len(randomNumbers) != monNombreDePiecesCachees[len(monNombreDePiecesCachees)-1]:
        randomNumber = math.floor(random()*100)
        if randomNumber not in randomNumbers:
            forbiddenPlace1 = randomNumber -1
            forbiddenPlace2 = randomNumber +1
            forbiddenPlace3 = randomNumber +9
            forbiddenPlace4 = randomNumber +10
            forbiddenPlace5 = randomNumber +11
            forbiddenPlace6 = randomNumber -9
            forbiddenPlace7 = randomNumber -10
            forbiddenPlace8 = randomNumber -11
            if not(forbiddenPlace1 in randomNumbers or forbiddenPlace2 in randomNumbers \
            or forbiddenPlace3 in randomNumbers or forbiddenPlace4 in randomNumbers \
            or forbiddenPlace5 in randomNumbers or forbiddenPlace6 in randomNumbers \
            or forbiddenPlace7 in randomNumbers or forbiddenPlace8 in randomNumbers) :
                randomNumbers.append(randomNumber)
    return randomNumbers
 

# La fonction "placerPiecesCachees()" permet de placer les pièces cachées.

def placerPiecesCachees():
    for j in mesCasesCachees[len(mesCasesCachees)-1]:
      temp = str(j)
      uneCase = document.querySelector("#case"+temp)
      uneCase.innerHTML = '<img src="symboles/coste.svg" id ="piece'+ temp + '" onclick="clic(' + temp+ ')" hidden="hidden"/>'


# Les fonctions suivantes représentent un découpage fonctionnel de la fonction
# "casesVoisines()". Nous avons créé une fonction pour chaque cas particulier
# et une fonction "randomCase(index)" pour le cas général.    
          
def case0(index):
    mesCasesVoisinesPourCase0 = []
    case1 = index+1
    mesCasesVoisinesPourCase0.append(case1)
    case5 = index+10
    mesCasesVoisinesPourCase0.append(case5)
    case7 = index+11
    mesCasesVoisinesPourCase0.append(case7)
    return mesCasesVoisinesPourCase0

def case9(index):
    mesCasesVoisinesPourCase9 = []
    case2 = index-1
    mesCasesVoisinesPourCase9.append(case2)
    case3 = index+9
    mesCasesVoisinesPourCase9.append(case3)
    case5 = index+10
    mesCasesVoisinesPourCase9.append(case5)
    return mesCasesVoisinesPourCase9

def case90(index):
    mesCasesVoisinesPourCase90 = []
    case1 = index+1
    mesCasesVoisinesPourCase90.append(case1)
    case4 = index-9
    mesCasesVoisinesPourCase90.append(case4)
    case6 = index-10
    mesCasesVoisinesPourCase90.append(case6)
    return mesCasesVoisinesPourCase90

def case99(index):
    mesCasesVoisinesPourCase99 = []
    case2 = index-1
    mesCasesVoisinesPourCase99.append(case2)
    case6 = index-10
    mesCasesVoisinesPourCase99.append(case6)
    case8 = index-11
    mesCasesVoisinesPourCase99.append(case8)
    return mesCasesVoisinesPourCase99

def ligne1(index):
    mesCasesVoisinesPourLigne1 = []
    case1 = index+1
    mesCasesVoisinesPourLigne1.append(case1)
    case2 = index-1
    mesCasesVoisinesPourLigne1.append(case2)
    case3 = index+9
    mesCasesVoisinesPourLigne1.append(case3)
    case5 = index+10
    mesCasesVoisinesPourLigne1.append(case5)
    case7 = index+11
    mesCasesVoisinesPourLigne1.append(case7)
    return mesCasesVoisinesPourLigne1

def ligne2(index):
    mesCasesVoisinesPourLigne2 = []
    case1 = index+1
    mesCasesVoisinesPourLigne2.append(case1)
    case2 = index-1
    mesCasesVoisinesPourLigne2.append(case2)
    case4 = index-9
    mesCasesVoisinesPourLigne2.append(case4)
    case6 = index-10
    mesCasesVoisinesPourLigne2.append(case6)
    case8 = index-11
    mesCasesVoisinesPourLigne2.append(case8)
    return mesCasesVoisinesPourLigne2


def ligne3(index):
    mesCasesVoisinesPourLigne3 = [] 
    case1 = index+1
    mesCasesVoisinesPourLigne3.append(case1)
    case4 = index-9
    mesCasesVoisinesPourLigne3.append(case4)
    case6 = index-10
    mesCasesVoisinesPourLigne3.append(case6)
    case5 = index+10
    mesCasesVoisinesPourLigne3.append(case5)
    case7 = index+11
    mesCasesVoisinesPourLigne3.append(case7)
    return mesCasesVoisinesPourLigne3

def ligne4(index):
    mesCasesVoisinesPourLigne4 = []
    case2 = index-1
    mesCasesVoisinesPourLigne4.append(case2)
    case3 = index+9
    mesCasesVoisinesPourLigne4.append(case3)
    case6 = index-10
    mesCasesVoisinesPourLigne4.append(case6)
    case5 = index+10
    mesCasesVoisinesPourLigne4.append(case5)
    case8 = index-11
    mesCasesVoisinesPourLigne4.append(case8)
    return mesCasesVoisinesPourLigne4

def randomCase(index):
    mesCasesVoisinesPourRandomCase = []
    case1 = index+1
    mesCasesVoisinesPourRandomCase.append(case1)
    case2 = index-1
    mesCasesVoisinesPourRandomCase.append(case2)
    case3 = index+9
    mesCasesVoisinesPourRandomCase.append(case3)
    case4 = index-9
    mesCasesVoisinesPourRandomCase.append(case4)
    case5 = index+10
    mesCasesVoisinesPourRandomCase.append(case5)
    case6 = index-10
    mesCasesVoisinesPourRandomCase.append(case6)
    case7 = index+11
    mesCasesVoisinesPourRandomCase.append(case7)
    case8 = index-11
    mesCasesVoisinesPourRandomCase.append(case8)
    return mesCasesVoisinesPourRandomCase


# La fonction "casesVoisines()" est une fonction intermédiaire permettant de
# renvoyer le nombre de fois que chaque case "a été une case voisine". Cela
# nous permet dans la prochaine fonction, de ne récupérer que le nombre de fois
# qu'une case est présente dans le tableau renvoyé par "casesVoisines()" pour
# obtenir les valeurs des indices.

def casesVoisines():
    mesCasesVoisines = []
    for i in mesCasesCachees[len(mesCasesCachees)-1]:
        if i==0:
            mesCasesVoisines += case0(i)
        elif i==9:
            mesCasesVoisines += case9(i)
        elif i==90:
            mesCasesVoisines += case90(i)
        elif i == 99:
            mesCasesVoisines += case99(i)
        elif i>=1 and i<=8:
            mesCasesVoisines += ligne1(i)
        elif i>=91 and i<=98:
            mesCasesVoisines += ligne2(i)
        elif i>=10 and int(str(i)[1]) == 0 and (int(str(i)[0])>=1 and int(str(i)[0])<=8):
            mesCasesVoisines += ligne3(i)
        elif i>=10 and int(str(i)[1]) == 9 and (int(str(i)[0])>=1 and int(str(i)[0])<=8):
            mesCasesVoisines += ligne4(i)
        else:
            mesCasesVoisines += randomCase(i)
    return mesCasesVoisines
            

# La fonction "valeurPieceVoisine(case)" permet de déterminer la valeur de 
# toutes les cases voisines afin de détermier les indices.

def valeurPieceVoisine(case):
    valeurEnHTMLtemp = []
    baliseOuvrante = '<p>'
    valeurEnHTMLtemp.append(baliseOuvrante)
    valeurIndice = str(mesCasesVoisines[len(mesCasesVoisines)-1].count(case))
    valeurEnHTMLtemp.append(valeurIndice)
    baliseFermante = '</p>'
    valeurEnHTMLtemp.append(baliseFermante)
    valeurEnHTML = ''.join(valeurEnHTMLtemp)
    return valeurEnHTML


# La fonction "indices()" permet d'afficher les valeurs des indices sur le
# tableau.

def indices():
    for i in mesCasesVoisines[len(mesCasesVoisines)-1]:
      index = str(i)
      maCaseVoisine = document.querySelector("#case"+index)
      maCaseVoisine.innerHTML = valeurPieceVoisine(i)


# La fonction "element(id)" est une fonction intermédiaire permettant de 
# récupérer un élément en fonction de son id.

def element(id):
    return document.querySelector('#piece' + str(id))


# La fonction "check()" vérifie le nombre d'erreurs et de sous cachées à chaque
# clic pour déterminer la victoire ou la défaite du joueur. Le cas échéant,
# elle permet de maintenir l'image pendant 10s et de relancer le jeu.

def check():
    if len(casesVides) == 3:
        loser = document.querySelector(".infos")
        loser.innerHTML = "You lost!"
        sleep(5)
        init()
    elif len(mesCasesCachees[len(mesCasesCachees)-1]) == 0:
        winner = document.querySelector(".infos")
        winner.innerHTML = "You won!"
        sleep(5)
        init()


# La fonction "clic(index)" est appelée à chaque clic du joueur sur une case
# contenant une image ou une case vide. S'il y'a une pièce cachée sur la case
# on enlève l'attribut "hidden" à l'image et on décrémente la valeur du nombre
# de sous cachées. Si c'est une case vide, on incrémente la valeur des erreurs.
    
def clic(index):
    if index in mesCasesCachees[len(mesCasesCachees)-1]:
        element(index).removeAttribute("hidden")
        mesCasesCachees[len(mesCasesCachees)-1].remove(index)
        monNombre = document.querySelector(".nombre")
        monNombre.innerHTML = str(len(mesCasesCachees[len(mesCasesCachees)-1]))
        check()
    elif index not in mesCasesVoisines[len(mesCasesVoisines)-1] and index not in casesVides :
        if index not in mesCasesCacheestemp:
            casesVides.append(index)
            myError = document.querySelector(".error")
            myError.innerHTML = str(len(casesVides))
            check()