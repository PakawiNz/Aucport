from django.db import models
from django.core import validators
import re
import hashlib
import datetime

def member_file_name(instance, filename):
	filename = hashlib.sha224(instance.email).hexdigest()
	return '/'.join(['profilepic', filename + '.jpg'])

def product_file_name(instance, filename):
	filename = hashlib.sha224(filename).hexdigest()
	return '/'.join(['productpic', filename + '.jpg'])

class RegexField(models.CharField):
	def __init__(self, regex=r'.*', **kwargs) :
		self.regex = regex
		super(RegexField,self).__init__(**kwargs)

	def clean(self, value, model_instance):
		value = super(RegexField,self).clean(value, model_instance)
		if not re.match(self.regex, value):
			raise validators.ValidationError('Data not match with following regex (%s).'%(self.regex))
		return value

class CharField(models.CharField):
	def __init__(self, min_length=0, **kwargs) :
		super(CharField,self).__init__(**kwargs)
		self.validators.append(validators.MinLengthValidator(min_length))

class AlphaNumericField(CharField):
	def clean(self, value, model_instance):
		value = super(AlphaNumericField,self).clean(value, model_instance)
		if not re.match(r'\w+$', value):
			raise validators.ValidationError('AlphaNumeric characters only.')
		return value

class BirthdateField(models.DateField):
	def __init__(self, minimum_age=0, **kwargs) :
		self.minimum_age = minimum_age
		super(BirthdateField,self).__init__(**kwargs)

	def clean(self, value, model_instance):
		value = super(BirthdateField,self).clean(value, model_instance)
		maxdate = datetime.date.today()
		maxdate = maxdate.replace(year=maxdate.year - self.minimum_age)
		if maxdate < value:
			raise validators.ValidationError('Ages is less than minimum requirement (Born before %s).'%(maxdate.strftime("%d %b %Y")))
		return value


