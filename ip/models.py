from django.db import models

# Create your models here.

class iplist(models.Model):
    group_choices = (
        ('IP_filter_bw_open', 'IP_filter_bw_open'),
        ('GIMA_IT', 'GIMA_IT'),
        ('Lan', 'Lan'),
        ('GIMA_Mohotas','GIMA_Mohotas'),
        ('Gima_mac_filter_bw_open','Gima_mac_filter_bw_open'),
        ('MAC_users_512_login','MAC_users_512_login'),
        ('MAC_users_256_login','MAC_users_256_login'),
        ('gima_wireless_macs','gima_wireless_macs'),
        )

    site_choices = (
        ('HGT', 'HGT'),
        ('WANI', 'WANI'),
        ('WVG', 'WVG'),
        ('WVG-OE', 'WVG-OE'),
        ('GIMABIO', 'GIMABIO'),
        ('BELA-SPG', 'BELA-SPG'),
        ('Yerla','Yerla'),
        ('Wander','Wander'),
        ('HITPL','HITPL')

    )

    placeholder=(
        ('group','Group'),
    
    )
        
    # group = models.CharField(max_length=120)
    group=models.CharField(choices=group_choices,max_length=120)
    ip_address = models.CharField(max_length=120)
    site = models.CharField(choices=site_choices,max_length=50)
    dept = models.CharField(max_length=80)
    user_name = models.CharField(max_length=120)
    mac_address = models.CharField(max_length=120,blank=True,null=True)

    def __srt__(self):
        return self.user_name

    
 

