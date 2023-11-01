from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from .managers import UserManager


ENTREPRENEURSHIP_TYPE = (
    ("ENTREPRENEURIAT SOCIAL (ODD 1-6)","ENTREPRENEURIAT SOCIAL (ODD 1-6)"),
    ("ENTREPRENEURIAT PRODUCTIF (ODD 7-12)","ENTREPRENEURIAT PRODUCTIF (ODD 7-12)"),
    ("ENTREPRENEURIAT ENVIRONNEMENTAL (ODD 13-15)","ENTREPRENEURIAT ENVIRONNEMENTAL (ODD 13-15)"),
    ("ENTREPRENEURIAT NUMÉRIQUE, INSTITUTIONNEL ET DE SERVICE (ODD 16)","ENTREPRENEURIAT NUMÉRIQUE, INSTITUTIONNEL ET DE SERVICE (ODD 16)"),
)

class User(AbstractUser):
    DEVELOPPEURS = "DEV"
    STAFF_PNUD = "SFP"
    ENTREPRENEUR = "ENT"

    STAFF_TYPE_CHOICES = (
        (DEVELOPPEURS, "Développeurs"),
        (STAFF_PNUD, "Staff PNUD"),
        (ENTREPRENEUR, "Entrepreneur"),
    )
    username = None
    contact = models.PositiveIntegerField(unique=True)
    staff_type = models.CharField(max_length=3, choices=STAFF_TYPE_CHOICES)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "contact"

    objects = UserManager()

    def __str__(self):
        return str(self.get_full_name()) 

class Entrepreneur(models.Model):
    MALE = "M"
    FEMALE = "F"
    SEX_CHOICES = (
        (MALE, "Masculin"),
        (FEMALE, "Feminin"),
    )

    SAVANES = "SAV"
    KARA = "KAR"
    CENTRALE = "CEN"
    PLATEAUX = "PLA"
    GRAND_LOME = "GDL"
    MARITIME = "MAR"
    REGION_CHOICES = (
        (SAVANES, "Savanes"),
        (KARA, "Kara"),
        (CENTRALE, "Centrale"),
        (PLATEAUX, "Plateaux"),
        (GRAND_LOME, "Grand Lomé"),
        (MARITIME, "Maritime"),
    )
    
    CINKASSE1 = "CINKASSE1"  
    CINKASSE2 = "CINKASSE2"
    TONE1     = "TONE1"
    TONE2     = "TONE2"
    TONE3     = "TONE3"
    TONE4     = "TONE4"
    KPENDJAL1 =   "KPENDJAL1"
    KPENDJAL2 =  "KPENDJAL2"
    KPENDJALOUEST1 = "KPENDJALOUEST1"
    KPENDJAL1OUEST2 = "KPENDJAL1OUEST2"
    OTI1 = "OTI1"
    OTI2 = "OTI2"
    OTISUD1 = "OTISUD1"
    OTI2SUD2 = "OTI2SUD2"
    TANDJOUARE1 = "TANDJOUARE1"
    TANDJOUARE2 = "TANDJOUARE2"
    KERAN1 = "KERAN1"
    KEARN2 = "KERAN2"
    KEARN3 = "KERAN3"
    BASSAR1 = "BASSAR1"
    BASSAR2 = "BASSAR2"
    BASSAR3 = "BASSAR3"
    BASSAR4 = "BASSAR4"
    DAKPEN1 = "DAKPEN1"
    DAKPEN2 = "DAKPEN2"
    DAKPEN3 = "DAKPEN3"
    KOZAH1 = "KOZAH1"
    KOZAH2 = "KOZAH2"
    KOZAH3 = "KOZAH3"
    KOZAH4 = "KOZAH4"
    BINAH1 = "BINAH1"
    BINAH2 = "BINAH2"
    DOUFELGOU1 = "DOUFELGOU1"
    DOUFELGOU2 = "DOUFELGOU2"
    DOUFELGOU3 = "DOUFELGOU3"
    ASSOLI1 = "ASSOLI1"
    ASSOLI2 = "ASSOLI2"
    ASSOLI3 = "ASSOLI3"
    TCHAOUDJO1 = "TCHAOUDJO1"
    TCHAOUDJO2 = "TCHAOUDJO2"
    TCHAOUDJO3 = "TCHAOUDJO3"
    TCHAOUDJO4 = "TCHAOUDJO4"
    SOTOUBOUA1 = "SOTOUBOUA1"
    SOTOUBOUA2 = "SOTOUBOUA2"
    SOTOUBOUA3 = "SOTOUBOUA3"
    MO1  =  "MO1"
    MO1  =  "MO1"
    TCHAMA1 = "TCHAMA1"
    TCHAMBA1 = "TCHAMBA1"
    TCHAMBA2 = "TCHAMBA2"
    TCHAMBA3 = "TCHAMBA2"
    BLITTA1 = "BLITTA1"
    BLITTA2 = "BLITTA2"
    BLITTA3 = "BLITTA3"
    ANIE1 = "ANIE1"
    ANIE2 = "ANIE2"
    ESTMONO1 = "EST-MONO1"
    ESTMONO2 = "EST-MONO2"
    MOYENMONO1 = "MOYEN-MONO1"
    MOYENMONO2 = "MOYEN-MONO2"
    AGOU1 = "AGOU1"
    AGOU2 = "AGOU2"
    DANYI1 = "DANYI1"
    DANYI2 = "DANYI2"
    AKEBOU1 = "AKEBOU1"
    AKEBOU2 = "AKEBOU2"
    KPELE1 = "KPELE1"
    KPELE2 = "KPELE2"
    KLOTO1 = "KLOTO1"
    KLOTO2 = "KLOTO2"
    KLOTO3 = "KLOTO3"
    OGOU1 = "OGOU1"
    OGOU2 = "OGOU2"
    OGOU3 = "OGOU3"
    OGOU4 = "OGOU4"
    AMOU1 = "AMOU1"
    AMOU2 = "AMOU2"
    AMOU3 = "AMOU3"
    WAWA1 ="WAWA1"
    WAWA2 ="WAWA2"
    WAWA3 ="WAWA3"
    HAHO1 ="HAHO1"
    HAHO2 = "HAHO2"
    HAHO3 = "HAHO3"
    AVE1 = "AVE1"
    AVE2 = "AVE2"
    BASMONO1 ="BASMONO1"
    BASMONO1 ="BASMONO1"
    YOTO1 = "YOTO1"
    YOTO2 = "YOTO2"
    YOTO3 = "YOTO3"
    VO1 = "VO1"
    VO2 = "VO2"
    VO3 = "VO3"
    VO4 = "VO4"
    LACS1 = "LACS1"
    LACS2 = "LACS2"
    LACS3 = "LACS3"
    LACS4 = "LACS4"
    ZIO1 = "ZIO1"
    ZIO2 = "ZIO2"
    ZIO3 = "ZIO3"
    ZIO4 = "ZIO4"
    AGOENYEVE1 = "AGOENYEVE1"
    AGOENYEVE2 = "AGOENYEVE2"
    AGOENYEVE3 = "AGOENYEVE3"
    AGOENYEVE4 = "AGOENYEVE4"
    AGOENYEVE5 = "AGOENYEVE5"
    AGOENYEVE6 = "AGOENYEVE6"
    GOLFE1 = "GOLFE1"
    GOLFE2 = "GOLFE2"
    GOLFE3 = "GOLFE3"
    GOLFE4 = "GOLFE4"
    GOLFE5 = "GOLFE5"
    GOLFE6 = "GOLFE6"
    GOLFE7 = "GOLFE7"

    COMMUNE_CHOICES = (
        (CINKASSE1 , "CINKASSE1"), 
        (CINKASSE2 , "CINKASSE2"),
        (TONE1     ,"TONE1"),
        (TONE2     , "TONE2"),
        (TONE3     , "TONE3"),
        (TONE4     , "TONE4"),
        ( KPENDJAL1 ,  "KPENDJAL1"),
        (KPENDJAL2 , "KPENDJAL2"),
        (KPENDJALOUEST1 , "KPENDJALOUEST1"),
        (KPENDJAL1OUEST2 , "KPENDJAL1OUEST2"),
        (OTI1 , "OTI1"),
        (OTI2 , "OTI2"),
        (OTISUD1 , "OTISUD1"),
        (OTI2SUD2 , "OTI2SUD2"),
        (TANDJOUARE1 , "TANDJOUARE1"),
        (TANDJOUARE2 , "TANDJOUARE2"),
        (KERAN1 , "KERAN1"),
        (KEARN2 , "KERAN2"),
        (KEARN3 , "KERAN3"),
        (BASSAR1 , "BASSAR1"),
        (BASSAR2 , "BASSAR2"),
        (BASSAR3 , "BASSAR3"),
        (BASSAR4 , "BASSAR4"),
        (DAKPEN1 , "DAKPEN1"),
        (DAKPEN2 , "DAKPEN2"),
        (DAKPEN3 , "DAKPEN3"),
        (KOZAH1 , "KOZAH1"),
        (KOZAH2 , "KOZAH2"),
        (KOZAH3 , "KOZAH3"),
        (KOZAH4 , "KOZAH4"),
        (BINAH1 , "BINAH1"),
        (BINAH2 , "BINAH2"),
        (DOUFELGOU1 , "DOUFELGOU1"),
        (DOUFELGOU2 , "DOUFELGOU2"),
        (DOUFELGOU3 , "DOUFELGOU3"),
        (ASSOLI1 , "ASSOLI1"),
        (ASSOLI2 , "ASSOLI2"),
        (ASSOLI3 , "ASSOLI3"),
        (TCHAOUDJO1 , "TCHAOUDJO1"),
        (TCHAOUDJO2 , "TCHAOUDJO2"),
        (TCHAOUDJO3 , "TCHAOUDJO3"),
        (TCHAOUDJO4 , "TCHAOUDJO4"),
        (SOTOUBOUA1 , "SOTOUBOUA1"),
        (SOTOUBOUA2 , "SOTOUBOUA2"),
        (SOTOUBOUA3 , "SOTOUBOUA3"),
        (MO1  ,  "MO1"),
        (MO1  ,  "MO1"),
        (TCHAMA1 , "TCHAMA1"),
        (TCHAMBA1 , "TCHAMBA1"),
        (TCHAMBA2 , "TCHAMBA2"),
        (TCHAMBA3 , "TCHAMBA2"),
        (BLITTA1 , "BLITTA1"),
        (BLITTA2 , "BLITTA2"),
        (BLITTA3 , "BLITTA3"),
        (ANIE1 , "ANIE1"),
        (ANIE2 , "ANIE2"),
        (ESTMONO1 , "EST-MONO1"),
        (ESTMONO2 , "EST-MONO2"),
        (MOYENMONO1 , "MOYEN-MONO1"),
        (MOYENMONO2 , "MOYEN-MONO2"),
        (AGOU1 , "AGOU1"),
        (AGOU2 , "AGOU2"),
        (DANYI1 , "DANYI1"),
        (DANYI2 , "DANYI2"),
        (AKEBOU1 , "AKEBOU1"),
        (AKEBOU2 , "AKEBOU2"),
        (KPELE1 , "KPELE1"),
        (KPELE2 , "KPELE2"),
        (KLOTO1 , "KLOTO1"),
        (KLOTO2 , "KLOTO2"),
        (KLOTO3 , "KLOTO3"),
        (OGOU1 , "OGOU1"),
        (OGOU2 , "OGOU2"),
        (OGOU3 , "OGOU3"),
        (OGOU4 , "OGOU4"),
        (AMOU1 , "AMOU1"),
        (AMOU2 , "AMOU2"),
        (AMOU3 , "AMOU3"),
        (WAWA1 ,"WAWA1"),
        (WAWA2 ,"WAWA2"),
        (WAWA3 ,"WAWA3"),
        (HAHO1 ,"HAHO1"),
        (HAHO2 , "HAHO2"),
        (HAHO3 , "HAHO3"),
        (AVE1 , "AVE1"),
        (AVE2 , "AVE2"),
        (BASMONO1 ,"BASMONO1"),
        (BASMONO1 ,"BASMONO1"),
        (YOTO1 , "YOTO1"),
        (YOTO2 , "YOTO2"),
        (YOTO3 , "YOTO3"),
        (VO1 , "VO1"),
        (VO2 , "VO2"),
        (VO3 , "VO3"),
        (VO4 , "VO4"),
        (LACS1 , "LACS1"),
        (LACS2 , "LACS2"),
        (LACS3 , "LACS3"),
        (LACS4 , "LACS4"),
        (ZIO1 , "ZIO1"),
        (ZIO2 , "ZIO2"),
        (ZIO3 , "ZIO3"),
        (ZIO4 , "ZIO4"),
        (AGOENYEVE1 , "AGOENYEVE1"),
        (AGOENYEVE2 , "AGOENYEVE2"),
        (AGOENYEVE3 , "AGOENYEVE3"),
        (AGOENYEVE4 , "AGOENYEVE4"),
        (AGOENYEVE5 , "AGOENYEVE5"),
        (AGOENYEVE6 , "AGOENYEVE6"),
        (GOLFE1 , "GOLFE1"),
        (GOLFE2 , "GOLFE2"),
        (GOLFE3 , "GOLFE3"),
        (GOLFE4 , "GOLFE4"),
        (GOLFE5 , "GOLFE5"),
        (GOLFE6 , "GOLFE6"),
        (GOLFE7 , "GOLFE7"),
        
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="staff")
    email = models.EmailField( max_length=50)
    sexe = models.CharField(max_length=3, choices=SEX_CHOICES,)
    commune = models.CharField(max_length=50,choices=COMMUNE_CHOICES) 
    region = models.CharField(max_length=50, choices=REGION_CHOICES) 
    niveau_education =  models.CharField(max_length=50)
    photo_profil = models.ImageField(null=True, blank=True, upload_to="photo_profil")
    profession_actuelle = models.CharField(max_length=50)
    
    def __str__(self):
     return self.user.first_name
    
    def get_absolute_url(self):
        return reverse("read_entrepreneur", kwargs={"pk": self.pk})

    @property
    def update_absolute_url(self):
        return reverse("update_entrepreneur", kwargs={"pk": self.pk})

    @property
    def del_absolute_url(self):
        return reverse("delete_entrepreneur", kwargs={"pk": self.pk})

    def delete(self, *args, **kwargs):
        self.user.delete()
        super(Entrepreneur, self).delete(*args, **kwargs)


   
class Initiative(models.Model):
    nom = models.CharField(max_length=50) 
    description = models.TextField(max_length=2000)
      
    def __str__(self):
        return self.nom
    

class Entreprise(models.Model):
    entrepreneur = models.OneToOneField(Entrepreneur, on_delete=models.CASCADE, related_name="entreprise")
    raison_sociale = models.CharField(max_length=250)
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE, related_name="ense_initiative")
    description_activite = models.TextField(max_length=300)
    attentes_recherchees= models.TextField(max_length=2000)
    type_entrepreneuriat = models.CharField(max_length=200,choices=ENTREPRENEURSHIP_TYPE)
    montant_approuve = models.IntegerField()
 
    def __str__(self):
        return self.raison_sociale
    
    def get_absolute_url(self):
        return reverse("read_entrepreneur", kwargs={"pk": self.pk})

    @property
    def update_absolute_url(self):
        return reverse("update_entrepreneur", kwargs={"pk": self.pk})

    @property
    def del_absolute_url(self):
        return reverse("delete_entrepreneur", kwargs={"pk": self.pk})

    def delete(self, *args, **kwargs):
        self.user.delete()
        super(Entreprise, self).delete(*args, **kwargs)
     

class EntrepriseLocation(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)
    longitude = models.FloatField(null=True, blank=True) 
    latitude = models.FloatField(null=True, blank=True) 
    

    def __str__(self):
        return self.entreprise.raison_sociale
    

    
class FicheAutoEvaluation(models.Model):
    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    montant_recu =models.IntegerField() 
    pourcentage_consommer= models.IntegerField()
    pourcentage_activite_realiser = models.IntegerField()
    montant_restant = models.IntegerField()
    performance =models.TextField(max_length=2000)
    changement_enregistre =models.TextField(max_length=2000)
    attente_comblee =models.TextField(max_length=2000)
    gap_a_combler = models.TextField(max_length=2000)
    connaissances_acquise = models.TextField(max_length=2000)
    lecon_apprise = models.TextField(max_length=2000)
    apport=models.TextField(max_length=2000)
    difficulte = models.TextField(max_length=2000)
    utilisation_des_acquis = models.TextField(max_length=2000)
    visite_incubateur = models.IntegerField()
    visite_cabinet = models.IntegerField()
    visite_faiej = models.IntegerField()
    autre_visite = models.IntegerField()
    emploi_actuel_cree_homme = models.IntegerField()
    emploi_actuel_cree_femme = models.IntegerField()
    emploi_futur_cree_homme = models.IntegerField()
    emploi_futur_cree_femme = models.IntegerField()
    mesure_changement_climatique = models.TextField(max_length=2000)
    mesure_egalite_genre = models.TextField(max_length=2000)
    autre_info = models.TextField(max_length=2000)
    message_visibilite = models.TextField(max_length=2000)
    video = models.FileField(upload_to='videos/', max_length=254)
    images= models.ImageField(upload_to='photos/', max_length=254)
    partenariat_etabli=models.TextField(max_length=2000)
    partenariat_futur=models.TextField(max_length=2000)
    resultat_esperer = models.TextField(max_length=2000)
    recommandations = models.TextField(max_length=2000)
    date = models.DateField(auto_now_add=True)
    confirmation_des_cibles = models.TextField(max_length=2000)
    
    def __str__(self):
        return f"Fiche Auto-Evaluation {self.id} de {self.entrepreneur.user.get_full_name()}"
    
    def get_absolute_url(self):
        return reverse("fiche_details", kwargs={"id": self.id})


