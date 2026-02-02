import bpy

class UI_Panel(bpy.types.Panel): # case sensitive - not panel but Panel
    bl_label = "LOD Generator" # name in the UI 
    bl_idname = "LODPanel"     # id to identify later ( i think ) 
    bl_space_type = 'VIEW_3D'  # Space that it will be in VIEW_3D for in the view tab / PROPERTIES - its to go in the properties tab
    bl_region_type = 'UI'      # Again for which region will it go in 
    bl_category = 'LOD Generator'  # If you create a new name = new category / If you use a new name it will just add to an used Category that already exists
    
    def draw(self, context ):
        _layout = self.layout
#        _row = _layout.row()     - With row, everything is in the same line? Separator didnt work to do a break 
        
        _layout.label(text="Select an Object to create an LOD,")
#       _layout.separator()       -  This creates a break in the UI text 
        _layout.label(text="Then select how many LOD's you want")
        _layout.label(text="Then Finnaly press the button Start")
        
        _data = context.scene.my_tool    #grabs the stuff inside of my_tool
        _layout.prop(_data, "targetSelection")   # draws the box 
        
        
        
        
class SelectionBox(bpy.types.PropertyGroup):  
        targetSelection: bpy.props.PointerProperty(   # targetSelection -- bpy.props.PointerProperty = the water drop thing to select the object 
        name="Select Object for an LOD",    # display text in that box 
        type=bpy.types.Object
    )        
        
def register():                            # register the classes / We got to register every class 
    bpy.utils.register_class(UI_Panel)
    bpy.utils.register_class(SelectionBox)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=SelectionBox)   # saves the picked object 
    
def unregister():                          # unregister the class / reverse of registering text  
    bpy.utils.unregister_class(UI_Panel)
    bpy.utils.unregister_class(SelectionBox)
    del bpy.types.Scene.my_too
    
if __name__ == "__main__":                 # exec the script
    register()