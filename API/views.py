from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

"""
Cette page contient deux fonctions, une fonction de vue my_view(request) est la fonction API_controller(request) utilisée pour simplifier la programmation

La fonction API_controller prend un seul paramètre qu'est la requête envoyée par le client, et elle renvoie un dictionnaire dont 
les clés sont des chaines de caracètre représentant les noms des champs du formulaire (paramètres + résultat), 
et les valeurs du dictionnaire sont les valeurs des champs du formulaire
 
La fonction my_view prend un seul paramètre qu'est la requête envoyée par le client,
puis, la fonction teste si la requête est du type POST ou non, c'est si le cas, elle fait appel à la fonction API_controller pour récupérer le résultat
sinon, elle crée un dictionnaire contenant les résultats obtenus en utilisant les paramètres par défaut.
Ensuite, la fonction envoie le dictionnaire au client (index.html) par l'intermédiaire de la fonction render

"""

@csrf_exempt
def my_view(request):

    if request.method == 'POST':
        reponse = API_controller(request)

    else:
        reponse ={
            "multiple" : 7,
            "seuil_max" : 100 ,
            "frequence" : 5,
            "mot_a_afficher" : "Alter Way",
            "list_div" : [],
            "est_afficher" : False
        }

    return render( request, 'index.html', context= reponse )



def API_controller(request):

    if "Multiple" in request.POST.keys():
        multiple = int(request.POST["Multiple"])
    else:
        multiple=7

    if "seuil_max" in request.POST.keys():
        seuil_max= int(request.POST["seuil_max"])
    else:
        seuil_max= 100

    if "frequence" in request.POST.keys():
        frequence= int(request.POST["frequence"])
    else:
        frequence=5

    if "mot_a_afficher" in request.POST.keys():
        mot_a_afficher= request.POST["mot_a_afficher"]
        if mot_a_afficher == "":
            mot_a_afficher="Alter Way"
    else:
        mot_a_afficher="Alter Way"

    list_div=[]
    for i in range(0, seuil_max+1 ):
        if i%multiple==0:
            list_div.append(i)

    if len(list_div)>= frequence :
        est_afficher= True
    else:
        est_afficher= False

    reponse= {
        "multiple" :multiple ,
        "seuil_max":seuil_max,
        "frequence":frequence,
        "mot_a_afficher":mot_a_afficher,
        "list_div": list_div,
        "est_afficher":est_afficher
    }
    return reponse
