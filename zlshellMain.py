v = ""
while 1:
 oopen = open('zlshell.py', 'w')

 x = input('>>> ')

 def replace1():
  global x
  if 'line' in x:
	  x = x.replace('line', 'print')
  if 'make ' in x:
	  x = x.replace('make ', '')
  if 'if ' in x and 'else if' not in x:
	  x = x.replace('if ', 'if ')
  if 'else if' in x:
	  x = x.replace('else if', 'elif')
  if 'else:' in x:
	  x = x.replace('else:', 'else:')
  if 'define ' in x and 'define run ' not in x:
	  x = x.replace('define ', 'def ')
  if 'define run ' in x:
	  x = x.replace('define run ', '')
  if 'class ' in x:
	  x = x.replace('class ', 'class ')
  if 'while ' in x:
	  x = x.replace('while ','while ')
  if 'download ' in x:
	  x = x.replace('download ','import ')
  if 'drun ' in x:
	  x = x.replace('drun ','')
  if 'for ' in x:
	  x = x.replace('for ','for ')
  if '$' in x:
	  x = x.replace('$','#')
  if 'take_input' in x:
	  x = x.replace('take_input','input')
  if '' in x:
    pass
 replace1()
 v += x
 v += '\n'
 oopen.write(v)
 output = input('want to have output yet? y/n>>')
 if output == 'y':
  v = ''
  x = ''
  oopen.close()
  exec(open('zlshell.py', 'r').read())
  exec(open("main.py").read())

