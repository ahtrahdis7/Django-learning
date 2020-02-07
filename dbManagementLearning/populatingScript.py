import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dbManagementLearning.settings')

import django
django.setup()

##FAKE POP SCRIPT
import random
from userApp.models import users
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'MarketPlace', 'News', "Games"]


def populate(N = 5):

    for entry in range(N):

        #create the fake data for entry
        fake_name = fakegen.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        fake_email = fakegen.email()

        #create thr new webpage entry
        user = users.objects.get_or_create(fname = fake_fname, lname = fake_lname, mail = fake_email)[0]



if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete')
