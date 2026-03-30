bl_info = {
        'name': 'ToggleDefaultWeights',
        'author': 'bay raitt',
        'version': (0, 2),
        'blender': (5, 0, 0),
        'category': 'View',
        'location': 'View > Weights > Toggle Default Weights',
        'wiki_url': ''}


import bpy


def main(context):
    for b in bpy.data.brushes:
        w = bpy.data.brushes[b.name].weight
        bpy.data.brushes[b.name].weight = 1.0 - w


class BR_OT_toggle_weights(bpy.types.Operator):
    """Toggle Default Weights"""
    bl_idname = "view3d.toggle_default_weights"
    bl_label = "Toggle Default Weights"

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_draw(self, context):
    self.layout.operator(BR_OT_toggle_weights.bl_idname)


def register():
    bpy.utils.register_class(BR_OT_toggle_weights)
    bpy.types.VIEW3D_MT_paint_weight.prepend(menu_draw)  


def unregister():
    bpy.utils.unregister_class(BR_OT_toggle_weights)
    bpy.types.VIEW3D_MT_paint_weight.remove(menu_draw)  

    if __name__ != "__main__":
        bpy.types.VIEW3D_MT_paint_weight.remove(menu_draw)


if __name__ == "__main__":
    register()
