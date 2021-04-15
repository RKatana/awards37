from django.test import TestCase
from .models import Projects, Profile, Votes
from django.contrib.auth.models import User

# Create your tests here
class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User(username = 'janedoe' ,email = 'janedoe@gmail.com', password = '123456')
        self.profile = Profile(image = '/path/jefflogo.svg', user = self.user, bio ='Talk is cheap, show me the code',)
        
        
    def test_save_profile(self):
        self.user.save()
        self.profile.save()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Projects.objects.all().delete()


class ProjectsTestCase(TestCase):
    '''
    Test Class for Project Model
    '''
    # Set up method
    def setUp(self):
        self.user = User(username = 'janedoe' ,email = 'janedoe@gmail.com', password = '123456')
        self.user.save()

        self.profile = Profile(image = '/path/jefflogo.svg' ,user = self.user, bio = "I love coding")
        self.profile.save()

        self.project = Projects(name = 'Testing', image = '/path/jefflogo.svg', description = 'Project one', link = '/path/jefflogo.svg')
        self.project.save()

        # Creating a new project
        self.project.profile.user.add(self.profile)
    
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Projects.objects.all().delete()
        

class VotesTestCase(TestCase):
    def setUp(self):
        self.user = User(username = 'John Doe', email = 'johndoe@gmail.com', password = '123456')
        self.user.save()

        self.profile = Profile(image = '/path/jefflogo.svg' ,user = self.user, bio = "I love coding")
        self.profile.save()

        self.project = Projects(name = 'Testing', image = '/path/jefflogo.svg', description = 'Project one', link = '/path/jefflogo.svg')
        self.project.save()

        self.vote = Votes(design = '7', usability = '7', content = '6', user=self.user, project = 'Testing')
        self.vote.save_vote()
