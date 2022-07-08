from django.test import TestCase
from Dzellalsys.views import MainPage
from Dzellalsys.models import Registration
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from .models import Registration

#from .model import d1, d2, d3 - multiple models

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')
	
	def test_save_post_request(self):
		response = self.client.post('/', {'FirstName': 'Jalalodin',
		 'Middlename' : 'Paguia',
		 'Surname' : 'Rascal',
		 'Age' : '17',
		 'RegVote' : 'Yes',
		 'What' : 'Pogi',
		 'basis': 'Television',
		 'Pres': 'Ping Lacson',
		 'VPres': 'Vicente Sotto'})	

		self.assertEqual(Registration.objects.count(),1)
		
		checkData = Registration.objects.first()
		self.assertEqual(checkData.NewFirstName, 'Jalalodin')
		self.assertEqual(checkData.NewMiddleName, 'Paguia')
		self.assertEqual(checkData.NewSurname, 'Rascal')
		self.assertEqual(checkData.NewAge, '17')
		self.assertEqual(checkData.Rdbtn, 'Yes')
		self.assertEqual(checkData.NewQstn1, 'Pogi')
		self.assertEqual(checkData.DrpbxBasis, 'Television')
		self.assertEqual(checkData.DrpbxElection, 'Ping Lacson')
		self.assertEqual(checkData.DrpboxVC, 'Vicente Sotto')

	def test_models(self):
		self.client.get('/')
		self.assertEqual(Registration.objects.count(), 0)

class ORMtest(TestCase):
	def test_retrieveModels(self):
		Models = Registration()
		Models.NewFirstName = 'Jalalodin'
		Models.NewMiddleName = 'Paguia'
		Models.NewSurname = 'Rascal'
		Models.NewAge = '17'
		Models.Rdbtn = 'Yes'
		Models.NewQstn1 = 'Pogi'
		Models.DrpbxBasis = 'Television'
		Models.DrpbxElection = 'Ping Lacson'
		Models.DrpboxVC = 'Vicente Sotto'
		Models.save()

		Models2 = Registration()
		Models2.NewFirstName = 'Alemon'
		Models2.NewMiddleName = 'Daluma'
		Models2.NewSurname = 'Lomabao'
		Models2.NewAge = '26'
		Models2.Rdbtn = 'Yes'
		Models2.NewQstn1 = 'Cute'
		Models2.DrpbxBasis = 'Research'
		Models2.DrpbxElection = 'Isko Moreno'
		Models2.DrpboxVC = 'Willie Ong'
		Models2.save()

		RegList = Registration.objects.all()

		self.assertEqual(RegList.count(), 2)

		Info1 = RegList[0]
		Info2 = RegList[1]

		self.assertEqual(Info1.NewFirstName, 'Jalalodin')
		self.assertEqual(Info1.NewMiddleName, 'Paguia')
		self.assertEqual(Info1.NewSurname, 'Rascal')
		self.assertEqual(Info1.NewAge, '17')
		self.assertEqual(Info1.Rdbtn, 'Yes')
		self.assertEqual(Info1.NewQstn1, 'Pogi')
		self.assertEqual(Info1.DrpbxBasis, 'Television')
		self.assertEqual(Info1.DrpbxElection, 'Ping Lacson')
		self.assertEqual(Info1.DrpboxVC, 'Vicente Sotto')

		self.assertEqual(Info2.NewFirstName, 'Alemon')
		self.assertEqual(Info2.NewMiddleName, 'Daluma')
		self.assertEqual(Info2.NewSurname, 'Lomabao')
		self.assertEqual(Info2.NewAge, '26')
		self.assertEqual(Info2.Rdbtn, 'Yes')
		self.assertEqual(Info2.NewQstn1, 'Cute')
		self.assertEqual(Info2.DrpbxBasis, 'Research')
		self.assertEqual(Info2.DrpbxElection, 'Isko Moreno')
		self.assertEqual(Info2.DrpboxVC, 'Willie Ong')

	def test_template(self):
		Registration.objects.create(NewFirstName = 'Jalalodin',
		NewMiddleName = 'Paguia',
		NewSurname = 'Rascal',
		NewAge = '17',
		Rdbtn = 'Yes',
		NewQstn1 = 'Pogi',
		DrpbxBasis = 'Television',
		DrpbxElection = 'Ping Lacson',
		DrpboxVC = 'Vicente Sotto'
		)

		Registration.objects.create(NewFirstName = 'Alemon',
		NewMiddleName = 'Daluma',
		NewSurname = 'Lomabao',
		NewAge = '26',
		Rdbtn = 'Yes',
		NewQstn1 = 'Cute',
		DrpbxBasis = 'Research',
		DrpbxElection = 'Isko Moreno',
		DrpboxVC = 'Willie Ong'
		)

		response = self.client.get('/')
		self.assertIn('1: Jalalodin, Paguia, Rascal, Yes, Pogi, Television, Ping Lacson, Vicente Sotto', response.content.decode())
		self.assertIn('2: Alemon, Daluma, Lomabao, Yes, Cute, Research, Isko Moreno, Willie Ong', response.content.decode())
		






	

	


	



		
   		

