from django.shortcuts import render
from search.models import City, CollectLocation, Zone, Garbage, GarbageType

import random

def game(request, dest_resulat=None):

    # get image of one garbage randomly
    selected_garbage = random.choice(Garbage.objects.all())
    image = selected_garbage.image
    good_answer = selected_garbage.destination

    # get all the garbages
    garbages = Garbage.objects.all()

    # get all destinations without duplicates 
    destinations = []
    for dest in garbages:
        destinations.append(dest.destination)
    destinations = list(dict.fromkeys(destinations))

    resultat = ""

    if request.method == "POST":
        selected_destination = request.POST.get ("selected_destination", None)
        dest_resulat = True
        if selected_destination == good_answer:
            resultat = "C'est gagné !"
        else:
            resultat = "Perdu"


    return render(
        request, 
        'game/game.html',
        {
            "Garbages" : garbages,
            "Destinations" : destinations,
            "Selected_garbage" : selected_garbage,
            "Image" : image,
            "Dest_resultat" : dest_resulat,
            "Resultat" : resultat,

        })


# if __name__ == '__main':
#     game()


###################### ALAIN #######################

# def Game(request, id=None):
#     """
#         Mini game
# #!        @ -> Redirect to login if not already logged (and back to game)
#         if not plant_id draw random plant from Vegetal collection
#         else check for selected answer
#     """
# #!
#     # # get current user
#     # CurrentUser = request.user
#     # # get friendly user name (first_name if exists, else username)
#     # CurrentUserName = CurrentUser.first_name if CurrentUser.first_name.strip() else CurrentUser.username
# #!
#     # get plant (random choice or by plant_id)
#     CurrentPlant = random.choice(Vegetal.objects.all())
#     if plant_id:
#         CurrentPlant = get_object_or_404(
#             Vegetal, 
#             pk=plant_id)
    
#     # get all existing colors
#     Colors = Color.objects.all()

#     # Define default message
#     Message = f"OK {CurrentUserName}, voici la question : \nDans la liste ci-dessous, sélectionne une couleur dominante de cette plante."

#     # if action is post (plant_id is passed in parameters)
#     if plant_id:
#         # get post result for Color input (radio button) or none if no button was selected
#         SelectedColorID = request.POST.get("Color", None)
#         if SelectedColorID is None:
#             # no button was selected
#             Message = f"{CurrentUserName}, tu dois sélectionner une couleur dans la liste."
#         else:
#             # a button was selected
#             try:
#                 # get plant color matching selected answer
#                 PlantColor = CurrentPlant.color.get(
#                     pk=SelectedColorID)
#                 # success
#                 # update user data
#                 CurrentUser.userdata.good_answers += 1
#                 CurrentUser.userdata.save()
#                 # define message
#                 Message = f"BRAVO {CurrentUserName},\n{PlantColor.name} est bien une couleur dominante de {CurrentPlant.name} !\n\nCette bonne réponse est ajoutée à ton profil."
#                 # reset Colors so form won't be displayed anymore in view
#                 Colors = None
#             except (KeyError, Color.DoesNotExist):
#                 # error, this plant don't have this color
#                 # get color object
#                 SelectedColor = Color.objects.get(
#                     pk=SelectedColorID)
#                 # update user data
#                 CurrentUser.userdata.bad_answers += 1
#                 CurrentUser.userdata.save()
#                 # define message
#                 Message = f"Désolé {CurrentUserName},\n{SelectedColor.name} n'est pas une couleur dominante de {CurrentPlant.name}.\nLes bonnes réponses sont {', '.join(Color.name for Color in CurrentPlant.color.all())}\n\nMalheureusement, cette mauvaise réponse est ajoutée à ton profil."
#                 # reset Colors so form won't be displayed anymore in view
#                 Colors = None
            
#             # update message with score overview
#             Message += f"\nTu as donc au total : {CurrentUser.userdata.good_answers} bonnes réponses et {CurrentUser.userdata.bad_answers} mauvaises réponses."

#     # render template with appropriate context :
#     #   - Message to show to user
#     #   - Current plant object
#     #   - List of colors to create form with radio buttons
#     #       (None if answer was found -> no form will be created)
#     return render(
#         request,
#         f"game/game.html",
#         {
#             "Message" : Message,
#             "Plant" : CurrentPlant,
#             "Colors" : Colors
#         })
