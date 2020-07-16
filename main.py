import os
def main():
 #opens files
 openshell = input('<<Would you like to use ZScript shell? y/n>>')
 if openshell == 'y':
   exec(open('zlshellMain.py').read())
 makefile = input('<<Would you like to make a file? y/n>>')
 if makefile == 'y':
   name = input('<<What would you like to name your file?>>')
   f= open(name + ".zsc","w+")
   f.close()
   main()
 mathyon = input('<<would you like to do math? y/n>>')
 if mathyon == 'y':
	 exec(open('math.py', 'r').read())
 directory = input('<<directory>>')
 IF_input = input('<<name of zl file>>') + '.zsc'
 print('the ZScript file', IF_input, 'has now be opened')
 IF = open(os.path.join(directory)+ IF_input, "rt")
 OF = open("out.py", "wt")
 #list of the "commands"
 clist = ['line ','make ','if ','define ','class ','while ','download ']
 #changes words
 for line in IF:
	 if 'line' in line:
		 OF.write(line.replace('line', 'print'))
	 if 'make ' in line:
		 OF.write(line.replace('make ', ''))
	 if 'if ' in line and 'else if' not in line:
		 OF.write(line.replace('if ', 'if '))
	 if 'else if' in line:
		 OF.write(line.replace('else if', 'elif'))
	 if 'else: ' in line:
		 OF.write(line.replace('else: ', 'else:'))
	 if 'define ' in line and 'define run ' not in line:
		 OF.write(line.replace('define ', 'def '))
	 if 'define run ' in line:
		 OF.write(line.replace('define run ', ''))
	 if 'class ' in line:
		 OF.write(line.replace('class ', 'class '))
	 if 'while ' in line:
		 OF.write(line.replace('while ','while '))
	 if 'download ' in line:
		 OF.write(line.replace('download ','import '))
	 if 'drun ' in line:
		 OF.write(line.replace('drun ',''))	
	 if 'for ' in line:
		 OF.write(line.replace('for ','for '))
	 if '$' in line:
		 OF.write(line.replace('$','#'))
 #closes files
 IF.close()
 OF.close()
 #runs python file
 exec(open("out.py").read())
 main()

main()
