import bpy
import os
import json

# template_decorplus_wire_mesh
# template_decorplus_trim_mesh
# template_decorplus_wood_mesh
# template_decorplus_wire_solid
# template_decorplus_trim_solid
# template_decorplus_wood_solid
# template_decorplus_wire_solid_handlebar_top
# template_decorplus_wire_solid_handlebar_middle
# template_decorplus_trim_solid_handlebar_top
# template_decorplus_trim_solid_handlebar_middle
# template_decorplus_wood_solid_handlebar_top
# template_decorplus_wood_solid_handlebar_middle
# template_decorplus_wire_solid_classic_top
# template_decorplus_wire_solid_classic_middle
# template_decorplus_trim_solid_classic_top
# template_decorplus_trim_solid_classic_middle
# template_decorplus_wood_solid_classic_top
# template_decorplus_wood_solid_classic_middle
# template_decorplus_wire_solid_flat_top
# template_decorplus_wire_solid_flat_middle
# template_decorplus_trim_solid_flat_top
# template_decorplus_trim_solid_flat_middle
# template_decorplus_wood_solid_flat_top
# template_decorplus_wood_solid_flat_middle
# template_decorplus_wire_solid_modern_top
# template_decorplus_wire_solid_modern_middle
# template_decorplus_trim_solid_modern_top
# template_decorplus_trim_solid_modern_middle
# template_decorplus_wood_solid_modern_top
# template_decorplus_wood_solid_modern_middle


#these values can probably be retrieved from the current scene and view layer
###########################
scene = "Scene"
viewlayer = "View Layer"
camera = "mainCameraTop"
world = "World"
###########################
clearAllContexts = True
templateString = "tmp"
alwaysInclude = 'studio'
prefix = ""
##

def getJson(json_file):
    data = {}
    script_file = os.path.realpath(__file__)
    directory = bpy.path.abspath("//")
    jasonFile = os.path.join(directory, json_file)
    with open(jasonFile) as data_file:
        data = json.load(data_file)

    return data

variations = getJson('shelves.json')


# def addObjectToCollection(obj, collection):
#     # col = bpy.data.collections
#     # collectionName = collection.name
#     collection.objects.link(obj)

def duplicateObjectsInCollectionAssignModify(sourceCollection, targetCollection, variations):
    prefixStr = f"{prefix}_" if len(prefix) > 0 else""
    templateToRemove = f"{prefixStr}{sourceCollection.name.removeprefix(f'{templateString}_')}"
    # col = bpy.data.collections
    objects = sourceCollection.objects

    for obj in objects:
        newObj = obj.copy()
        newObj.location = obj.location
        targetCollection.objects.link(newObj)

        # replace materials
        for slot in newObj.material_slots:
            pref = targetCollection.name.removeprefix(f"{templateToRemove}_")
            if (pref in variations[sourceCollection.name]['materials'] and slot.material.name in variations[sourceCollection.name]['materials'][pref]):
                mat = variations[sourceCollection.name]['materials'][pref][slot.material.name]
                slot.link = 'OBJECT'
                slot.material = bpy.data.materials[mat]


def getAllTemplateCollections():
    templates = []
    for collection in bpy.data.collections:
        if (templateString in collection.name):
            templates.append(collection)

    return templates


def generateCollections(templates):
    col = bpy.data.collections
    generatedCollections = []

    for template in templates:
        if(template.name in list(variations.keys()) and variations[f"{template.name}"]["enabled"] == "True"):
            varies = variations[f"{template.name}"]["materials"]
            for jdx, variation in enumerate(varies):
                #collections
                prefixStr = f"{prefix}_" if len(prefix) > 0 else""
                newCollectionName = f"{prefixStr}{template.name.removeprefix(f'{templateString}_')}_{variation}"
                newCollection = bpy.data.collections.new(newCollectionName)
#                newCollection.name = newCollectionName
                bpy.data.scenes[scene].collection.children.link(newCollection)
                
#                bpy.context.scene.collection.children.link(newCollection)
                generatedCollections.append(newCollection)
                
                bpy.context.view_layer.layer_collection.children[newCollectionName].exclude = True

                # objects
                duplicateObjectsInCollectionAssignModify(template, newCollection, variations)
                    

    return generatedCollections


def generateRendersets(collections):
    if(clearAllContexts == True):
        bpy.data.scenes[scene].renderset_contexts.clear()
        bpy.data.scenes[scene].renderset_contexts.update()
    
    generatedRendersets = []
    prefixStr = f"{prefix}_" if len(prefix) > 0 else""
    
    for collection in collections:
        newContext = bpy.context.scene.renderset_contexts.add()
        bpy.context.scene.renderset_contexts.update()

        newContext.custom_name = collection.name
        generatedRendersets.append(newContext)

        

    return generatedRendersets

def del_collection(coll):
    for c in coll.children:
        del_collection(c)
    bpy.data.collections.remove(coll,do_unlink=True)

def resetAll():
    contexts = bpy.data.scenes[scene].renderset_contexts
    # contexts.clear()
    # contexts.update()

    collections = bpy.data.scenes['Scene'].id_data.view_layers['View Layer'].layer_collection.children
    filteredCollections = list(filter(lambda name: ('studio_' not in name and 'tmp_' not in name), collections))
    

    for collection in filteredCollections:
        print(f"*** {collection.name}")
    
    contexts.update()
    return False
            

def assignCollectionToRenderset():
    contexts = bpy.data.scenes[scene].renderset_contexts
    collections = bpy.data.scenes[scene].id_data.view_layers[viewlayer].layer_collection.children

    for idx in range(len(contexts.values())):
        if(idx == 0):
            continue
        bpy.data.scenes[scene].renderset_context_index = idx
        bpy.context.scene.camera = bpy.data.objects["mainCameraBottom"]
        bpy.context.scene.world = bpy.data.worlds["World"]
        rcName = contexts[idx].custom_name
        
        for jdx, collection in enumerate(collections.values()):
            cName = collection.name
            collection.exclude = True
            
            if(rcName == cName or alwaysInclude in cName):
                collection.exclude = False
            bpy.data.scenes[scene].id_data.view_layers[viewlayer].update()
        print(f"************** {idx} of {len(contexts.values())} variation")

    print(f"************** {len(contexts.values())} of {len(contexts.values())} variation")


    return False



print("HELLO WORLD")

templates = getAllTemplateCollections()
generatedCollections = generateCollections(templates)
generatedRendersets = generateRendersets(generatedCollections)

assignCollectionToRenderset()

print("GOODBYE WORLD")