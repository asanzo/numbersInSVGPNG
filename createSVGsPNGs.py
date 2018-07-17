#!/usr/bin/python
import os

currentPath = os.path.dirname(os.path.realpath(__file__))
modelSvgPath = os.path.join(currentPath, '999.svg')

def threeDigits(number):
	if(number < 10):
		return '00'+str(number)
	if(number < 100):
		return '0'+str(number)
	return str(number)

def outputPath(extension):
	return os.path.join(currentPath, 'images', threeDigits(number) + '.' + extension)

def makeNumberSVG(stringNumber):
	modelFile = open(modelSvgPath, "r")
	content = modelFile.read().replace('999',stringNumber)
	modelFile.close()

	svgOut = open(outputPath('svg'), "w+")
	svgOut.write(content)
	svgOut.close()


import subprocess

for number in range(0,1000):	
	makeNumberSVG(threeDigits(number))
	subprocess.call(['/usr/bin/inkscape','-z','-f',outputPath('svg'),'-w','200','-h','200','-e',outputPath('png')])