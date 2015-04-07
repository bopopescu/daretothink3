from django.contrib.admin.sites import AdminSite

class AdminProfile(AdminSite):
    pass
    #or overwrite some methods for different functionality

admin = AdminProfile()