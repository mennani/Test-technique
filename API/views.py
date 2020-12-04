from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):

    if request.method == 'POST':
        reponse = API(request)
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



def API(request):
    """

    :param Multiple:
    :param seuil_max:
    :param frequence:
    :return:
    """
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
