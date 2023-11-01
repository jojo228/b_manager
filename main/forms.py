from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Entrepreneur,FicheAutoEvaluation
from django import forms
from betterforms.multiform import MultiModelForm
from django.forms import ModelForm, ClearableFileInput





class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta(UserCreationForm):
        model = User
        fields = (
            "contact",
            "staff_type",
            "first_name",
            "last_name",
        )

        labels = {
            "staff_type": "Type d'utilisateur",
            "first_name": "Prénoms",
            "last_name": "Nom",
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("contact",)


# This is form for adding and creating detail of a new employee
class EntrepreneurForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EntrepreneurForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = " "

    class Meta:
        model = Entrepreneur
        exclude = [
            "user",
        ]
        labels = {
            "sexe": "Sexe",
            "commune": "Commune",
            "email": "Email",
            "region": "Région",
            "niveau_education": "Niveau d'éducation",
            "photo_profil": "Photo de profil",
        }


class EntrepreneurMultiForm(MultiModelForm):
    
    form_classes = {
        "user": CustomUserCreationForm,
        "entrepreneur": EntrepreneurForm,
    }

    def save(self, commit=True):
        objects = super(EntrepreneurMultiForm, self).save(commit=False)

        if commit:
            user = objects["user"]
            entrepreneur = objects["entrepreneur"]
            user.username = user.contact
            user.save()
            entrepreneur.user = user
            entrepreneur.save()

        return objects
    

class FicheAutoEvaluationForm1(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FicheAutoEvaluationForm1, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = " "    
    class Meta:
        model = FicheAutoEvaluation
        fields = (
                "montant_recu",	
                "pourcentage_consommer",	
                "pourcentage_activite_realiser",
                "montant_restant",	
                "performance"	,
                "changement_enregistre"	,
                "attente_comblee"	,
                "gap_a_combler"	,
                "confirmation_des_cibles" ,
                )
        labels = {
            "montant_recu":"Montant des tranches déjà reçues",	
            "pourcentage_consommer":"% de consommation de tranche reçue",	
            "pourcentage_activite_realiser":"% des activités réalisées",
            "montant_restant":"Montant (restant) à recevoir",	
            "performance":"Description des performances, résultats concrets de votre activité et rentabilité"	,
            "changement_enregistre":"Changement enregistré dans la mise en œuvre et/ou réponse aux besoins identifiés"	,
            "attente_comblee":"Attente comblée (oui/non) à décrire/préciser"	,
            "gap_a_combler":"Gap à combler"	,
            "confirmation_des_cibles":"Confirmations des cibles des ODD couverts par le projet (aller au-delà de l'objectif principal SVP)",
        }
    

class FicheAutoEvaluationForm2(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FicheAutoEvaluationForm2, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = " "   

    class Meta:
        model = FicheAutoEvaluation
        fields = (
            "connaissances_acquise"	,
            "lecon_apprise"	,
            "apport", 	
            "difficulte",	
            "utilisation_des_acquis",	

        )
        labels = {
            "connaissances_acquise": "Connaissance additionnelles acquises (à décrire/préciser)",
            "lecon_apprise":"Leçons apprises (à décrire/préciser)",
            "apport":"Apport concret réalisé par le projet en matière d’innovation",
            "difficulte":"Difficultés rencontrées (techniques, logistiques, temps, financière, etc.)",
            "utilisation_des_acquis":"Utilisation des acquis dans vos activités (comment adapter ou internaliser les outils dans votre activité)",
        }

class FicheAutoEvaluationForm3(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FicheAutoEvaluationForm3, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = " "

    class Meta:
        model = FicheAutoEvaluation
        fields = (
            "visite_incubateur",
            "visite_cabinet",
            "visite_faiej",
            "autre_visite",
            "emploi_actuel_cree_homme",
            "emploi_actuel_cree_femme",
            "emploi_futur_cree_homme",
            "emploi_futur_cree_femme",
            "mesure_changement_climatique",
            "mesure_egalite_genre",
            "autre_info",
            )
        
        labels={
            "visite_incubateur":"Nombre de visites de suivi réalisées par Incubateur :",
            "visite_cabinet":"Nombre de visites de suivi réalisées par Cabinet : ",
            "visite_faiej":"Nombre de visites de suivi réalisées par FAIEJ : ",
            "autre_visite":"Nombre de visites de suivi réalisées par Autres  :",
            "emploi_actuel_cree_homme":"Nombre actuel de staffs/emplois créés depuis le début de l’appui (Hommes) :",
            "emploi_actuel_cree_femme":"Nombre actuel de staffs/emplois créés depuis le début de l’appui (Femmes) : ",
            "emploi_futur_cree_homme":"Nombre futur de staffs/emplois à créer (Hommes) : ",
            "emploi_futur_cree_femme":"Nombre futur de staffs/emplois à créer (Femmes) : ",
            "mesure_changement_climatique":"Mesure prise pour l’atténuation aux Changements climatiques ou d’entreprises vertes",
            "mesure_egalite_genre":"Mesures prises pour l'égalité genre",
            "autre_info":"Autres informations supplémentaires pertinentes sur le projet",
        }


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class FicheAutoEvaluationForm4(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FicheAutoEvaluationForm4, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = " "

    class Meta:
        model = FicheAutoEvaluation
        fields = (
            "message_visibilite",
            "video",
            "images",
        )

        labels = {
            "message_visibilite":"Message/texte proposé pour la visibilité de communication",
            "video":"Vidéo réalisée (Oui/non) Partager la vidéo SVP",
            "images":"Images disponibles à partager pour le site du PNUD",
        }
        # widgets = {
        #     "video": MultipleFileInput(),
        #     "images": MultipleFileInput(),
        # }
        

class FicheAutoEvaluationForm5(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FicheAutoEvaluationForm5, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = " "

    class Meta:
        model = FicheAutoEvaluation
        fields = ("partenariat_etabli", "partenariat_futur",)

class FicheAutoEvaluationForm6(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FicheAutoEvaluationForm6, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            visible.field.widget.attrs["placeholder"] = " "  

    class Meta:
        model = FicheAutoEvaluation
        fields = (
           "resultat_esperer",
           "recommandations",
        )

        labels = {
            "resultat_esperer":"Résultats à atteindre dans les 6 prochains mois",
            "recommandations":"Recommandations pour améliorer le dispositif d’appui",
        }
   