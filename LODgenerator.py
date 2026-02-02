import bpy

class UI_Panel(bpy.types.Panel): # case sensitive - not panel but Panel
    bl_label = "LOD Generator" # name in the UI 
    bl_idname = "LODPanel"     # id to identify later ( i think ) 
    bl_space_type = 'VIEW_3D'  # Space that it will be in VIEW_3D for in the view tab / PROPERTIES - its to go in the properties tab
    bl_region_type = 'UI'      # Again for which region will it go in 
    bl_category = 'LOD Generator'  # If you create a new name = new category / If you use a new name it will just add to an used Category that already exists
    
    def draw(self, context ):
        _layout = self.layout
        
        
        
def register():                            # register the panels 
    bpy.utils.register_class(UI_Panel)
    
def unregister():                          # unregister the panels 
    bpy.utils.unregister_class(UI_Panel)
    
if __name__ == "__main__":                 # exec the script
    register()