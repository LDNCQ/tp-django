from django.db import models

class Train(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.TimeField()
    destination = models.CharField(max_length=100)
    

# train_1 = Train(name='Train 1', schedule='12:00:00', destination='Marseille')
# train_2 = Train(name='Train 2', schedule='13:00:00', destination='Paris')
# train_3 = Train(name='Train 3', schedule='14:00:00', destination='Lyon')
# train_4 = Train(name='Train 4', schedule='15:00:00', destination='Nice')
# train_5 = Train(name='Train 5', schedule='16:00:00', destination='Bordeaux')
# train_6 = Train(name='Train 6', schedule='17:00:00', destination='Toulouse')
# train_1.save()
# train_2.save()
# train_3.save()
# train_4.save()
# train_5.save()
# train_6.save()

# tous_les_objets = Train.objects.all()
# print (tous_les_objets)

