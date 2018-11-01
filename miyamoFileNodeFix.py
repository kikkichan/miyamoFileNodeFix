#------------
#
#last update 18/11/01
#Fixed bug function stops when occured connectAttr error
#
#------------

import maya.cmds as mc

p2dAttrs = ['coverage','translateFrame','rotateFrame','mirrorU','mirrorV','stagger','wrapU','wrapV','repeatUV','offset','rotateUV','noiseUV','vertexUvOne','vertexUvTwo','vertexUvThree','vertexCameraOne','outUV','outUvFilterSize']
fileAttrs = ['coverage','translateFrame','rotateFrame','mirrorU','mirrorV','stagger','wrapU','wrapV','repeatUV','offset','rotateUV','noiseUV','vertexUvOne','vertexUvTwo','vertexUvThree','vertexCameraOne','uvCoord','uvFilterSize']

def reconnect_p2d(file, p2d):
	f = file
	p = p2d
	#Reconnect file nodes to p2d node
	for i in range(len(f)):
		#To avoid error that already connected p2d to file node
		if mc.isConnected(str(p[0]+'.'+p2dAttrs[0]), str(f[i]+'.'+fileAttrs[0])) == False:
			#connect every attribute
			for attrIndex in range(len(fileAttrs)):
				mc.connectAttr(p[0]+'.'+p2dAttrs[attrIndex], f[i]+'.'+fileAttrs[attrIndex], f=True)

def main():
	obj = mc.ls(sl=True)
	file = []
	p2d = []

	#Separate selected nodes file from p2d
	for i in obj:
		type = mc.nodeType(i)
		if type == 'file':
			file.append(i)
		if type == 'place2dTexture':
			p2d.append(i)


	#Create new p2d node if no p2d nodes selected
	if len(p2d) == 0:
		p2d.append(mc.shadingNode('place2dTexture', n='p2d_1', au=True))

	#reconnect progress
	reconnect_p2d(file, p2d)
	print('Reconnection Done')
