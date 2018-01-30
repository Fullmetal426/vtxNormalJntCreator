"""

This script creates joints at selected vertecies with the same orientation as the vtx's normal direction.

I personally like to use this for local face rigging to make minor tweak controls.

"""

import maya.cmds as mc
import maya.mel as mel

vtx = mc.ls(sl = 1 , fl = 1)

for v in vtx:
    mc.select(cl =1 )
    jnt = mc.joint()    
    mc.select(v)   
    mc.select(jnt,tgl=True)
    mel.eval('doCreatePointOnPolyConstraintArgList 2 {   "0" ,"0" ,"0" ,"1" ,"" ,"1" ,"0" ,"0" ,"0" ,"0" };')
    mc.pickWalk(direction = 'down')
    mc.delete()
    mc.select(jnt)
    mc.makeIdentity(apply=True)
    mc.DeleteHistory