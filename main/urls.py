from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import *
from .forms import *


urlpatterns = [
    ######## Authentication urls ########
    path("",auth_views.LoginView.as_view(template_name="sign-in.html",),name="login",),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    ######## Entrepreneur CRUDL urls ########
    path("entrepreneur", views.EntrepreneurListView.as_view(), name="list_entrepreneur"),
    path("entrepreneur_ftai", views.EntrepreneurFTAIListView.as_view(), name="entrepreneur_ftai"),
    path("entrepreneur_cnp", views.EntrepreneurCNPListView.as_view(), name="entrepreneur_cnp"),
    path("entrepreneur_JeufZone", views.EntrepreneurJeufZoneListView.as_view(), name="entrepreneur_JeufZone"),
    path("entrepreneur_seafoundation", views.EntrepreneurSeaFoundationListView.as_view(), name="entrepreneur_seafoundation"),
    path("entrepreneur_younthconnect", views.EntrepreneurYounthConnectListView.as_view(), name="entrepreneur_younthconnect"),
    path("entrepreneur/create",views.EntrepreneurCreateView.as_view(),name="create_entrepreneur",),
    path("entrepreneur/read/<int:pk>",views.EntrepreneurDetailView.as_view(),name="read_entrepreneur",),
    path("entrepreneur/update/<int:pk>",views.EntrepreneurUpdateView.as_view(),name="update_entrepreneur",),
    path("entrepreneur/delete/<int:pk>",views.EntrepreneurDeleteView.as_view(),name="delete_entrepreneur",),

    ######## FAE CRUDL urls ########
    # create
    path("fae/create",views.FAEWizardView.as_view(
            [
                FicheAutoEvaluationForm1,
                FicheAutoEvaluationForm2,
                FicheAutoEvaluationForm3,
                FicheAutoEvaluationForm4,
                FicheAutoEvaluationForm5,
                FicheAutoEvaluationForm6,
            ]
        ),name="fae_create",),
    # list
    path("fae", views.FAEListView.as_view(), name="fae_list"),
    path("fae/list", views.FAEListView.as_view(), name="fae_list"),
    # read
    path("fae/<int:pk>",views.FAEDetailView.as_view(),name="fae_detail",),
    path("fae/detail/<int:pk>",views.FAEDetailView.as_view(),name="fae_detail",),
    # update
    path("fae/update/<int:pk>/identity_information",views.FAE1UpdateView.as_view(),name="fae_update1",),
    path("fae/update/<int:pk>/personal_information",views.FAE2UpdateView.as_view(),name="fae_update2",),
    path("fae/update/<int:pk>/address",views.FAE3UpdateView.as_view(),name="fae_update3",),
    path("fae/update/<int:pk>/address",views.FAE4UpdateView.as_view(),name="fae_update4",),
    path("fae/update/<int:pk>/address",views.FAE5UpdateView.as_view(),name="fae_update5",),
    path("fae/update/<int:pk>/address",views.FAE6UpdateView.as_view(),name="fae_update6",),
    path("fiche_details/<int:id>",views.FAEDetail,name="fiche_details",),
    path("fiche_print/<int:id>",views.FAEPrint,name="fae_print",),
    # delete
    path("fae/delete/<int:pk>",views.FAEDeleteView.as_view(),name="fae_delete",),


    ######## Inititatives urls ########
    path("ftai/", views.initiative_ftai,name="ftai"),
    path("cnp/", views.initiative_cnp,name="cnp"),
    path("sea-foundation/", views.initiative_seafoundation,name="sea"),
    path("JeufZone/", views.initiative_jeufzone,name="jeuf"),
    path("Younth-connect/", views.initiative_younthconnect,name="younth"),

    ######## Others urls ########
    path("dashboard/", views.home, name="dashboard"),
    path("beneficiaire/", views.beneficiaire, name="beneficiaire"),
    path("fiche/", views.fiche_auto_evaluation, name="fiche"),
    path("profil/", views.profil, name="profil"),
    
    # path("add beneficiaire/", views.add_beneficiaire,name='add'),


    path('live-search/', views.live_search, name='live_search'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
