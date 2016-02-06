from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import PhoneForm
from .models import Phone
from twilio.rest import TwilioRestClient
import json

class IndexView (View):
	def get(self,request):
		phone_form = PhoneForm()
		return render(request,"index.html",{"form":phone_form})

	def post(self,request):
		phone_form = PhoneForm(request.POST)
		phone_form.save()
		return redirect("/")


class SendMessage (View):
	def get(self, request):
		print("send message")
		with open('app/twilio.json')as data_file:
			twilio_settings = json.load(data_file)
		account_sid = twilio_settings["account_sid"]
		auth_token = twilio_settings["auth_token"]
		number = twilio_settings["number"]
		client = TwilioRestClient(account_sid, auth_token)
		textMessage = "Hi loser, you won!"
		for i in Phone.objects.all():
			print i.number
			message = client.messages.create(to="+"+i.number, from_=number,body=textMessage)
		return redirect("/")