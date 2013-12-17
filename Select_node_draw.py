#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jinpf
# @Date:   2013-12-17 14:37:19
# @Last Modified by:   jinpf
# @Last Modified time: 2013-12-17 17:55:19
# @Email: jpflcj@sina.com

"""
# @comment here:
选取一定范围的点[a,b]，将该范围点所在的图的边写入画图文件.gv

"""
import random

if __name__ == '__main__':
	with open('Email-EuAll.txt','r') as sdata:
		slines=sdata.readlines()
#		lines=sdata.readlines()
	print 'total edge:',len(slines)
	lines=random.sample(slines,200000)
	la=5
	lb=5
	'''
	la,lb为选定范围
	'''
	in_node=[]	#除[la,lb]外图中的点
	in_line=[]	#图中的边
	wait_line=[]	#待重复检查的边
	for line in lines:
		temp=line.replace('\n','').split('\t')
		if (la <= int(temp[0]) <=lb) or (temp[0] in in_node) :
			if  (int(temp[1]) <la or int(temp[1]) >lb) and (temp[1] not in in_node):
				in_node.append(temp[1])
			in_line.append(temp)
		elif (la <= int(temp[1]) <=lb) or (temp[1] in in_node) :
			in_node.append(temp[0])
			in_line.append(temp)
		else:
			wline=[1,temp[0],temp[1]]
			wait_line.append(wline)

	
	i=0
	while True:
		i+=1
		print "loop:",i
		in_len=len(in_line)
		print 'edge:',in_len
		print 'vertex:',(lb-la+1+len(in_node))

		with open('Snodeg'+str(i)+'.gv','w') as graf:
			graf.write('digraph G {\n')
			for line in in_line:
				graf.write('\t'+line[0]+' -> '+line[1]+' ;\n')
			graf.write('}')

		for wline in wait_line:
			if wline[0] and (wline[1] in in_node):
				if wline[2] not in in_node:
					in_node.append(wline[2])
				line=[wline[1],wline[2]]
				in_line.append(line)
				wline[0]=0
			elif wline[0] and (wline[2] in in_node):
				in_node.append(wline[1])
				line=[wline[1],wline[2]]
				in_line.append(line)
				wline[0]=0
		
		if in_len == len(in_line):
			break

#	print in_node
#	print in_line
#	print wait_line

	with open('Snodeg.gv','w') as graf:
		graf.write('digraph G {\n')
		for line in in_line:
			graf.write('\t'+line[0]+' -> '+line[1]+' ;\n')
		graf.write('}')
		
