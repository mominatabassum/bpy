import bpy
import math

def update_bone_rotation(bone_name, x_deg, y_deg, z_deg):
    armature = bpy.data.objects['Armature']
    bone = armature.pose.bones[bone_name]
    bone.rotation_mode = 'XYZ'
    x_rad = math.radians(x_deg)
    y_rad = math.radians(y_deg)
    z_rad = math.radians(z_deg)
    bone.rotation_euler = (x_rad, y_rad, z_rad)

def set_all_bones_default_pose():
    armature = bpy.data.objects['Armature']
    for bone in armature.pose.bones:
        update_bone_rotation(bone.name, 0, 0, 0)



set_all_bones_default_pose()

update_bone_rotation("mixamorig:Head", 0, 0, 0)
update_bone_rotation("mixamorig:Spine", 0, 0, 0) 

update_bone_rotation("mixamorig:LeftArm", 0, 0, 90)
update_bone_rotation("mixamorig:LeftForeArm", 0, 0, 0)

update_bone_rotation("mixamorig:RightArm", 0, 0, -90)
update_bone_rotation("mixamorig:RightForeArm", 0, 0, 0)

update_bone_rotation("mixamorig:LeftUpLeg", 0, 0, 0)
update_bone_rotation("mixamorig:LeftLeg", 0, 0, 0)
update_bone_rotation("mixamorig:LeftFoot", 0, 0, 0)

update_bone_rotation("mixamorig:RightUpLeg", 0, 0, 0)
update_bone_rotation("mixamorig:RightLeg", 0, 0, 0)
update_bone_rotation("mixamorig:RightFoot", 0, 0, 0)

