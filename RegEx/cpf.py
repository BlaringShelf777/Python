import re

#validate = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
noFormat = re.compile(r'^(\d{3})\.(\d{3})\.(\d{3})-(\d{2})$')
validate = re.compile(
    r'^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$'
)


cpf1 = '090.890.410-10'
cpf2 = '111.111.111-11'


print(validate.findall(cpf1)[0][1])
print(validate.findall(cpf2))
print(noFormat.sub(r'\1\2\3\4', cpf1))