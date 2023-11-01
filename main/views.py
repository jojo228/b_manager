from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q,Sum,Avg,OuterRef,Subquery
from django.db.models.functions import Coalesce
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from main.decorators import auth_users
from .forms import *
from .models import Entrepreneur, Entreprise, FicheAutoEvaluation
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from formtools.wizard.views import SessionWizardView, WizardView
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.

@auth_users
def home(request):
    montant_total_approuve = Entreprise.objects.aggregate(Sum('montant_approuve'))["montant_approuve__sum"]
    beneficiaires = Entreprise.objects.count()
    ent = Entreprise.objects.all()
    
    #Montants approuvés par region

    montant_reg_savane = Entreprise.objects.filter(entrepreneur__region="SAV").aggregate(Sum('montant_approuve'))["montant_approuve__sum"]
    montant_reg_kara = Entreprise.objects.filter(entrepreneur__region="KA").aggregate(Sum('montant_approuve'))["montant_approuve__sum"]
    montant_reg_centrale = Entreprise.objects.filter(entrepreneur__region="CEN").aggregate(Sum('montant_approuve'))["montant_approuve__sum"]
    montant_reg_plateaux = Entreprise.objects.filter(entrepreneur__region="PLA").aggregate(Sum('montant_approuve'))["montant_approuve__sum"]
    montant_reg_grand_lome = Entreprise.objects.filter(entrepreneur__region="GDL").aggregate(Sum('montant_approuve'))["montant_approuve__sum"]
    montant_reg_maritime = Entreprise.objects.filter(entrepreneur__region="MAR").aggregate(Sum('montant_approuve'))["montant_approuve__sum"]

    #Recap par region
    femmes_reg_savane = Entrepreneur.objects.filter(region="SAV",sexe="F").count()
    hommes_reg_savane = Entrepreneur.objects.filter(region="SAV",sexe="M").count()
    femmes_et_hommes_savane = int(femmes_reg_savane+hommes_reg_savane)
    
    femmes_reg_kara = Entrepreneur.objects.filter(region="KA",sexe="F").count()
    hommes_reg_kara = Entrepreneur.objects.filter(region="KA",sexe="M").count()
    femmes_et_hommes_kara = int(femmes_reg_kara+hommes_reg_kara)

    femmes_reg_centrale = Entrepreneur.objects.filter(region="CEN",sexe="F").count()
    hommes_reg_centrale = Entrepreneur.objects.filter(region="CEN",sexe="M").count()
    femmes_et_hommes_centrale = int(femmes_reg_centrale+hommes_reg_centrale)

    femmes_reg_plateaux = Entrepreneur.objects.filter(region="PLA",sexe="F").count()
    hommes_reg_plateaux = Entrepreneur.objects.filter(region="PLA",sexe="M").count()
    femmes_et_hommes_plateaux = int(femmes_reg_plateaux+femmes_reg_plateaux)

    femmes_reg_maritime = Entrepreneur.objects.filter(region="MAR",sexe="F").count()
    hommes_reg_maritime = Entrepreneur.objects.filter(region="MAR",sexe="M").count()
    femmes_et_hommes_maritime = int(femmes_reg_maritime+hommes_reg_maritime)

    femmes_reg_grand_lome = Entrepreneur.objects.filter(region="GDL",sexe="F").count()
    hommes_reg_grand_lome = Entrepreneur.objects.filter(region="GDL",sexe="M").count()
    femmes_et_hommes_grand_lome = int(femmes_reg_grand_lome+hommes_reg_grand_lome)



    
  
    

    # Créez une sous-requête pour obtenir la date de post la plus récente pour chaque entrepreneur
    latest_evaluation_dates = FicheAutoEvaluation.objects.filter(
        entrepreneur=OuterRef('pk')
    ).order_by('-date').values('date')[:1]

    # Utilisez la sous-requête pour obtenir le montant total du champ "montant_recu" pour chaque entrepreneur
    entrepreneurs_with_total_amount = Entrepreneur.objects.annotate(
        latest_evaluation_date=Subquery(latest_evaluation_dates)
    ).annotate(
        total_montant_recu=Sum('ficheautoevaluation__montant_recu', filter=Q(ficheautoevaluation__date=OuterRef('latest_evaluation_date')))
    )

    # Maintenant, entrepreneurs_with_total_amount contient le montant total pour chaque entrepreneur


    # Maintenant, total_amounts contient le montant total du champ "montant_recu" pour chaque entrepreneur


    # Maintenant, total_amounts contient le montant total du champ "montant_recu" pour chaque entrepreneur


    # Maintenant, total_amounts contient le montant total du champ "montant_recu" pour chaque entrepreneur


    # montant_decaisser = FicheAutoEvaluation.objects.aggregate(Sum('montant_recu'))['montant_recu__sum']
    pourcentage_consommer = FicheAutoEvaluation.objects.aggregate(ma_myenne=Avg('pourcentage_consommer'))['ma_myenne']

    total_hommes = Entrepreneur.objects.filter(sexe="M").count()
    total_femmes = Entrepreneur.objects.filter(sexe="F").count()
    total_communes = Entrepreneur.objects.values("commune").distinct().count()
    entreprises = Entreprise.objects.all()[:7]
    fiches = FicheAutoEvaluation.objects.all()

    return render(request, "dashboard.html",locals())


def beneficiaire(request):
    entrepreneur = Entrepreneur.objects.all()
    return render(request, "beneficiaire.html",locals())


def profil(request):
    user = request.user
    ent = Entrepreneur.objects.get(user=user)
    fiches = FicheAutoEvaluation.objects.filter(entrepreneur=ent)
    return render(request,"profil_entrep.html", locals())


def fiche_auto_evaluation(request):
    return render(request,"fiche-auto-evaluation.html")


def initiative_ftai(request):
    return render(request,"initiative-ftai.html")

def initiative_cnp(request):
    return render(request,"initiative-cnp.html")

def initiative_jeufzone(request):
    return render(request,"initiative-JeufZone.html")

def initiative_seafoundation(request):
    return render(request,"initiative-seafoundation.html")

def initiative_younthconnect(request):
    return render(request,"initiative-younthconnect.html")

def add_beneficiaire(request):
    return render(request,"ajouter-beneficiaire.html")

# -----------------------------------------------------------------------------
#### Super Admin Filter

class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return (
            self.request.user.is_superuser
            or self.request.user.is_staff
            or (self.request.user.staff_type == "ENT")
            or (self.request.user.staff_type == "SFP")
            or (self.request.user.staff_type == "DEV")
        )

### Entrepreneur ###

# List


class EntrepreneurListView(AdminStaffRequiredMixin, ListView):
    model = Entrepreneur
    template_name = "beneficiaire.html"

    def get_queryset(self):
        entrepreneur = Entrepreneur.objects.all() # this line
        
        return entrepreneur
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
#FTAI LIST
class EntrepreneurFTAIListView(AdminStaffRequiredMixin, ListView):
    model = Entreprise
    template_name = "initiative-ftai.html"

    def get_queryset(self):
        object_list = Entreprise.objects.filter(Q(initiative__nom="FTAI"))  # this line
        
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



#CNP LIST
class EntrepreneurCNPListView(AdminStaffRequiredMixin, ListView):
    model = Entreprise
    template_name = "initiative-cnp.html"

    def get_queryset(self):
        object_list = Entreprise.objects.filter(Q(initiative__nom="CNP"))  # this line
        
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

#JeufZone LIST
class EntrepreneurJeufZoneListView(AdminStaffRequiredMixin, ListView):
    model = Entreprise
    template_name = "initiative-JeufZone.html"

    def get_queryset(self):
        object_list = Entreprise.objects.filter(Q(initiative__nom="JeufZone"))  # this line
        
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


#SeaFoundation LIST

class EntrepreneurSeaFoundationListView(AdminStaffRequiredMixin, ListView):
    model = Entreprise
    template_name = "initiative-SeaFoundation.html"

    def get_queryset(self):
        object_list = Entreprise.objects.filter(Q(initiative__nom="SEA FOUNDATION"))  # this line
        
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
#YounthConnect LIST
class EntrepreneurYounthConnectListView(AdminStaffRequiredMixin, ListView):
    model = Entreprise
    template_name = "initiative-younthconnect.html"

    def get_queryset(self):
        object_list = Entreprise.objects.filter(Q(initiative__nom="YounthConnect"))  # this line
        
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context    



################################ ENTREPRENEUR VIEWS START #######################################

# create
class EntrepreneurCreateView(AdminStaffRequiredMixin, CreateView):
    success_url = reverse_lazy("beneficiaire")
    form_class = EntrepreneurMultiForm
    template_name = "entrepreneur_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# read
class EntrepreneurDetailView(AdminStaffRequiredMixin, DetailView):
    model = Entreprise
    template_name = "entrepreneur_read.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["entreprise"] = Entreprise.objects.get(id=self.kwargs["pk"])
        context["object_list"] = FicheAutoEvaluation.objects.filter(entrepreneur_id=self.kwargs["pk"])
        
        return context


# update
class EntrepreneurUpdateView(AdminStaffRequiredMixin, UpdateView):
    model = Entrepreneur
    form_class = EntrepreneurForm
    success_url = reverse_lazy("list_entrepreneur")
    template_name = "entrepreneur_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# delete
class EntrepreneurDeleteView(AdminStaffRequiredMixin, DeleteView):
    model = Entrepreneur
    success_url = reverse_lazy("list_entrepreneur")
    context_object_name = "entrepreneur"
    template_name = "entrepreneur_confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    


################################ ENTREPRENEUR VIEWS END #######################################



################################### FICHE AUTO EVALUATION VIEWS START #########################

FAE = "Fiche Auto Evaluation"

# CREATE
class FAEWizardView(SessionWizardView):
    login_url = reverse_lazy("login")
    template_name = "fiche-auto-evaluation.html"

    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'media'))


    def done(self, form_list, **kwargs):
        user = self.request.user

        # Create a new instance of your model
        instance = FicheAutoEvaluation()  # Replace 'YourModelName' with the actual name of your model

        # Set common fields
        instance.user = user
        instance.entrepreneur_id = user.id

        # Iterate through the forms and assign cleaned data to the instance
        for form in form_list:
            cleaned_data = form.cleaned_data

            if form == form_list[0]:
                instance.montant_recu = form_list[0].cleaned_data["montant_recu"]
                instance.pourcentage_consommer	= form_list[0].cleaned_data["pourcentage_consommer"]
                instance.pourcentage_activite_realiser= form_list[0].cleaned_data["pourcentage_activite_realiser"]
                instance.montant_restant	= form_list[0].cleaned_data["montant_restant"]
                instance.performance	= form_list[0].cleaned_data["performance"]
                instance.changement_enregistre	= form_list[0].cleaned_data["changement_enregistre"]
                instance.attente_comblee	= form_list[0].cleaned_data["attente_comblee"]
                instance.gap_a_combler	= form_list[0].cleaned_data["gap_a_combler"]
                instance.confirmation_des_cibles = form_list[0].cleaned_data["confirmation_des_cibles"]

            elif form == form_list[1]:
                instance.connaissances_acquise = form_list[1].cleaned_data["connaissances_acquise"]
                instance.lecon_apprise	= form_list[1].cleaned_data["lecon_apprise"]
                instance.apport= form_list[1].cleaned_data["apport"]
                instance.difficulte	= form_list[1].cleaned_data["difficulte"]
                instance.utilisation_des_acquis	= form_list[1].cleaned_data["utilisation_des_acquis"]

            elif form == form_list[2]:
                instance.visite_incubateur = form_list[2].cleaned_data["visite_incubateur"]
                instance.visite_cabinet = form_list[2].cleaned_data["visite_cabinet"]
                instance.visite_faiej = form_list[2].cleaned_data["visite_faiej"]
                instance.autre_visite = form_list[2].cleaned_data["autre_visite"]
                instance.emploi_actuel_cree_homme = form_list[2].cleaned_data["emploi_actuel_cree_homme"]
                instance.emploi_actuel_cree_femme = form_list[2].cleaned_data["emploi_actuel_cree_femme"]
                instance.emploi_futur_cree_homme = form_list[2].cleaned_data["emploi_futur_cree_homme"]
                instance.emploi_futur_cree_femme = form_list[2].cleaned_data["emploi_futur_cree_femme"]
                instance.mesure_changement_climatique = form_list[2].cleaned_data["mesure_changement_climatique"]
                instance.mesure_egalite_genre = form_list[2].cleaned_data["mesure_egalite_genre"]
                instance.autre_info = form_list[2].cleaned_data["autre_info"]

            elif form == form_list[3]:
                instance.message_visibilite = form_list[3].cleaned_data["message_visibilite"]
                instance.video = form_list[3].cleaned_data["video"]
                instance.images = form_list[3].cleaned_data["images"]

            elif form == form_list[4]:
                instance.partenariat_etabli = form_list[4].cleaned_data["partenariat_etabli"]
                instance.partenariat_futur = form_list[4].cleaned_data["partenariat_futur"]

            elif form == form_list[5]:
                instance.resultat_esperer = form_list[5].cleaned_data["resultat_esperer"]
                instance.recommandations = form_list[5].cleaned_data["recommandations"]

        # Save the instance to the database
        instance.save()

        messages.success(self.request, 'Votre formulaire a été soumis avec succès.')

        return redirect('profil')


# LIST
class FAEListView(AdminStaffRequiredMixin, ListView):
    model = FicheAutoEvaluation
    context_object_name = "fae"
    template_name = "entrepreneur_read.html"

    def get_queryset(self):
        user = self.request.user
        object_list = FicheAutoEvaluation.objects.filter(use=user)

        return object_list


# DETAIL
class FAEDetailView(AdminStaffRequiredMixin, DetailView):
    model = FicheAutoEvaluation
    context_object_name = "fae"
    template_name = "staff_account/staff_account_detail.html"


# UPDATE
class FAE1UpdateView(LoginRequiredMixin, UpdateView):
    model = FicheAutoEvaluation
    context_object_name = "fae"
    form_class = FicheAutoEvaluationForm1
    template_name = "staff_account/staff_account_identity_information_update.html"

    def get_success_url(self):
        return reverse_lazy(
            "fae_detail",
            kwargs={"pk": FicheAutoEvaluation.objects.get(user_id=self.kwargs["pk"]).id},
        )


class FAE2UpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = FicheAutoEvaluation
    context_object_name = "fae"
    form_class = FicheAutoEvaluationForm2
    template_name = "staff_account/staff_account_personal_information_update.html"

    def get_success_url(self):
        return reverse_lazy("fae_detail", kwargs={"pk": self.kwargs["pk"]})


class FAE3UpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = FicheAutoEvaluation
    context_object_name = "fae"
    form_class = FicheAutoEvaluationForm3
    template_name = "staff_account/staff_account_address_update.html"

    def get_success_url(self):
        return reverse_lazy("fae_detail", kwargs={"pk": self.kwargs["pk"]})
    

class FAE4UpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = FicheAutoEvaluation
    context_object_name = "fae"
    form_class = FicheAutoEvaluationForm4
    template_name = "staff_account/staff_account_address_update.html"

    def get_success_url(self):
        return reverse_lazy("fae_detail", kwargs={"pk": self.kwargs["pk"]})
    

class FAE5UpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = FicheAutoEvaluation
    context_object_name = "staff"
    form_class = FicheAutoEvaluationForm5
    template_name = "staff_account/staff_account_address_update.html"

    def get_success_url(self):
        return reverse_lazy("fae_detail", kwargs={"pk": self.kwargs["pk"]})
    

class FAE6UpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("login")
    model = FicheAutoEvaluation
    context_object_name = "staff"
    form_class = FicheAutoEvaluationForm6
    template_name = "staff_account/staff_account_address_update.html"

    def get_success_url(self):
        return reverse_lazy("fae_detail", kwargs={"pk": self.kwargs["pk"]})


# DELETE
class FAEDeleteView(AdminStaffRequiredMixin, DeleteView):
    model = FicheAutoEvaluation
    success_url = reverse_lazy("fae_delete")

#FAE DETAILS

def FAEDetail(request,id):
        details = FicheAutoEvaluation.objects.get(id=id)
        context={"x":details,}
        return render(request,"fiche-detail.html",context)
    
#FAE PRINT
def FAEPrint(request,id):
    fiche = FicheAutoEvaluation.objects.get(id=id)
    return render(request,"fae_print.html",locals())


################################### FICHE AUTO EVALUATION VIEWS END #########################


def live_search(request):
    query = request.GET.get('query', '')
    results = Entrepreneur.objects.filter(Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query)| Q(entreprise__raison_sociale__icontains=query))
    data = [{'id': ent.user.id, 'first_name': ent.user.first_name, 'last_name': ent.user.last_name, 'entreprise': ent.entreprise.raison_sociale} for ent in results]
    return JsonResponse(data, safe=False)