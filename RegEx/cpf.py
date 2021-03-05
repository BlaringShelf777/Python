import re

validate = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
noFormat = re.compile(r'^(\d{3})\.(\d{3})\.(\d{3})-(\d{2})$')


cpf = '090.890.410-10'


print(validate.findall(cpf))
print(noFormat.sub(r'\1\2\3\4', cpf))