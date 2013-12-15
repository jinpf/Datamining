#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jinpf
# @Date:   2013-12-14 22:49:12
# @Last Modified by:   jinpf
# @Last Modified time: 2013-12-15 18:35:54
# @Email: jpflcj@sina.com

"""
# @comment here:

"""
import random

if __name__ == '__main__':
	with open('Email-EuAll.txt','r') as data:
		lines=data.readlines()
	
	sampleline=random.sample(lines,2400)
	'''
	后面的数字代表抽样的大小
	'''
	'''
	注释掉写入节点
	nodes=[]
	for line in sampleline:
		temp=line.replace('\n','').split('\t')
		for node in temp:
			if node not in nodes:
				nodes.append(node)
#	nodes.sort()
#	print (nodes)
	'''

	with open('graf.gv','w') as graf:
		graf.write('digraph G {\n')
		'''
		注释掉写入节点
		for node in nodes:
			graf.write('\t'+node+';\n')
		'''

		graf.write('\n')
		for line in sampleline:
			temp=line.replace('\n','').split('\t')
			graf.write('\t'+temp[0]+' -> '+temp[1]+' ;\n')
		graf.write('}')