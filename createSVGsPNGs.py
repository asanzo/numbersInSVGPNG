#!/usr/bin/python
import os

currentPath = os.path.dirname(os.path.realpath(__file__))
modelSvgPath = os.path.join(currentPath, '999.svg')

def threeDigits(number, filling):
	if(number < 10):
		return filling + filling + str(number)
	if(number < 100):
		return filling + str(number)
	return str(number)

def outputPath(extension):
	return os.path.join(currentPath, 'images', threeDigits(number, '0') + '.' + extension)

def makeNumberSVG(stringNumber):
	modelFile = open(modelSvgPath, "r")
	content = modelFile.read().replace('999',stringNumber)
	modelFile.close()

	svgOut = open(outputPath('svg'), "w+")
	svgOut.write(content)
	svgOut.close()


import subprocess

for number in range(0,1000):	
	makeNumberSVG(threeDigits(number,' '))
	subprocess.call(['/usr/bin/inkscape','-z','-f',outputPath('svg'),'-w','40','-h','40','-e',outputPath('png')])