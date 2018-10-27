import maya.cmds as mc

p2dAttrs=['coverage','translateFrame','rotateFrame','mirrorU','mirrorV','stagger','wrapU','wrapV','repeatUV','offset','rotateUV','noiseUV','vertexUvOne','vertexUvTwo','vertexUvThree','vertexCameraOne','outUV','outUvFilterSize']
fileAttrs=['coverage','translateFrame','rotateFrame','mirrorU','mirrorV','stagger','wrapU','wrapV','repeatUV','offset','rotateUV','noiseUV','vertexUvOne','vertexUvTwo','vertexUvThree','vertexCameraOne','uvCoord','uvFilterSize']

def reconnect_p2d(file, p2d):
    f=file
    p=p2d
    #Reconnect file nodes to p2d node
    for i in range(len(f)):
        for attrIndex in range(len(fileAttrs)):
            mc.connectAttr(p[0]+'.'+p2dAttrs[attrIndex], f[i]+'.'+fileAttrs[attrIndex], f=True)

    #Display selected nodes in hypershade graph

def main():
    obj=mc.ls(sl=True)
    file=[]
    p2d=[]

    #Separate Selected Nodes
    for i in obj:
        type=mc.nodeType(i)
        if type=='file':
            file.append(i)
        if type=='place2dTexture':
            p2d.append(i)


    #Create new p2d node if no p2d node selected
    if len(p2d)==0:
        p2d.append(mc.shadingNode('place2dTexture', n='p2d_1', au=True))

    #reconnect progress
    reconnect_p2d(file, p2d)
    print('Reconnection Done')
