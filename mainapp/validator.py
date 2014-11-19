import re

def __re_validation(pattern,data,error_msg) :
	if re.match(pattern, data) is not None :
		return True
	else :
		return error_msg

def validate(data,*constraints) :
	errorList = []
	for constraint in constraints :
		result = constraint(data)
		if result != True :
			errorList.append(result)
			print result

	if len(errorList) == 0 :
		return True
	else :
		return errorList

#------------------------------------------------------------------------------------------

def V_is_in_DB(aclass):
	def inner(data) :
		try :
			aclass.objects.get(id=data)
			return True
		except :
			return 'ERROR MESSAGE V_is_in_DB'
	return inner

def V_is_unique(aclass,field):
	def inner(data) :
		filter_dict = {field:data}
		objects = aclass.objects.filter(**filter_dict)
		if len(objects) == 0 : return True
		else : return "ERROR MESSAGE V_is_unique"
	return inner

def V_len_more_than(amount):
	def inner(data) :
		if len(data) > amount : return True
		else : return "ERROR MESSAGE V_len_more_than"
	return inner

def V_len_less_than(amount):
	def inner(data) :
		if len(data) < amount : return True
		else : return "ERROR MESSAGE V_len_less_than"
	return inner

def V_alphanumeric() :
	def inner(data) :
		return __re_validation(r'^\w+$', data, "ERROR MESSAGE V_alphanumeric")
	return inner

def V_numeric() :
	def inner(data) :
		return __re_validation(r'^\d+$', data, "ERROR MESSAGE V_numeric")
	return inner

def V_alphabet() :
	def inner(data) :
		return __re_validation(r'^[a-zA-Z]+$', data, "ERROR MESSAGE V_alphabet")
	return inner

def V_isEmail() :
	def inner(data) :
		print data
		return __re_validation(r'^[a-zA-Z]\w+@\w+\.\w+$', data, "ERROR MESSAGE V_isEmail")
	return inner

def V_name() :
	def inner(data) :
		return __re_validation(r'^[a-zA-Z]\w+ ?\w+$', data, "ERROR MESSAGE V_name")
	return inner

def V_date() :
	def inner(data) :
		return 	
	return inner

def V_file_isJPG() :
	def inner(data) :
		if data._name.split('.')[-1].lower() != 'jpg' : return "ERROR MESSAGE V_file_isJPG"
		if data.content_type.lower() != 'image/jpeg' : return "ERROR MESSAGE V_file_isJPG"
		return True
	return inner