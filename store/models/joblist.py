from django.db import models
from .skillcat import Skillcat
from .ecat import Ecat
from .lcat import Lcat
from .icat import Icat
from .scat import Scat

class Joblist(models.Model):
     
    company_name = models.CharField(max_length = 1500)
    education = models.CharField(max_length = 1700, default='', null = True, blank = True)
    experience = models.CharField(max_length = 130, default='', null = True, blank = True)
    industry = models.CharField(max_length = 1200, default='', null = True, blank = True)
    description = models.CharField(max_length = 9000, default='', null = True, blank = True)
    location = models.CharField(max_length = 1200, default='', null = True, blank = True)
    payrate = models.CharField(max_length = 1500, default='', null = True, blank = True)
    date = models.DateField(auto_now_add = False, blank = True)
    skills = models.CharField(max_length = 1200, default='', null = True, blank = True)
    skillcat = models.ForeignKey(Skillcat, on_delete = models.CASCADE)
    ecat = models.ForeignKey(Ecat, on_delete = models.CASCADE)
    lcat = models.ForeignKey(Lcat, on_delete = models.CASCADE)
    icat = models.ForeignKey(Icat, on_delete = models.CASCADE)
    scat = models.ForeignKey(Scat, on_delete = models.CASCADE)

    @staticmethod
    def get_all_joblists():
        return Joblist.objects.all()

    @staticmethod
    def get_all_joblists_by_skillcatid(skillcat_id):
        if skillcat_id:
            return Joblist.objects.filter(skillcat = skillcat_id)
        else:
            return Joblist.get_all_joblists()

    @staticmethod
    def get_all_joblists_by_ecatid(ecat_id):
        if ecat_id:
            return Joblist.objects.filter(ecat = ecat_id)
        else:
            return Joblist.get_all_joblists()

    @staticmethod
    def get_all_joblists_by_lcatid(lcat_id):
        if lcat_id:
            return Joblist.objects.filter(lcat = lcat_id)
        else:
            return Joblist.get_all_joblists()

    @staticmethod
    def get_all_joblists_by_icatid(icat_id):
        if icat_id:
            return Joblist.objects.filter(icat = icat_id)
        else:
            return Joblist.get_all_joblists()
 
    @staticmethod
    def get_all_joblists_by_scatid(scat_id):
        if scat_id:
            return Joblist.objects.filter(scat = scat_id)
        else:
            return Joblist.get_all_joblists()

    @staticmethod
    def get_joblists_by_id(ids):
        return Joblist.objects.filter(id__in = ids)

    def __str__(self): 
        return self.company_name