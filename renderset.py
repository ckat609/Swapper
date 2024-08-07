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
camera = "mainCamera"
###########################
templateString = "tmp"
alwaysInclude = 'studio'
prefix = ""
##

def getJson(json_file):
    data = {}
    script_file = os.path.realpath(__file__)
    directory = os.path.dirname(script_file)
    jasonFile = os.path.join(directory, json_file)
    with open(jasonFile) as data_file:
        data = json.load(data_file)

    return data

variations = getJson('decorplus_spaces.json')


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
        # newObj.location = obj.location
        # targetCollection.objects.link(newObj)

        # replace materials
        for slot in obj.material_slots:
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
        # print(f"***** template: {template.name}")
        # print(f"***** keys: { list(variations.keys())}")
        # print(f"***** template: {template.name}")
        if(template.name in list(variations.keys())):
            # print(f"*************** IM IN!!!!: {template.name}")
            for variation in variations[f"{template.name}"]["materials"]:
                #collections
                prefixStr = f"{prefix}_" if len(prefix) > 0 else""
                newCollectionName = f"{prefixStr}{template.name.removeprefix(f'{templateString}_')}_{variation}"
                newCollection = template.copy()
                newCollection.name = newCollectionName
                # bpy.data.scenes[scene].collection.children.link(newCollection)
                
                bpy.context.scene.collection.children.link(newCollection)
                generatedCollections.append(newCollection)
                
                bpy.context.view_layer.layer_collection.children[newCollectionName].exclude = True

                # objects
                duplicateObjectsInCollectionAssignModify(template, newCollection, variations)
                    

    return generatedCollections


def generateRendersets(collections):
    generatedRendersets = []
    prefixStr = f"{prefix}_" if len(prefix) > 0 else""
    
    for collection in collections:
        newContext = bpy.context.scene.renderset_contexts.add()
        bpy.context.scene.renderset_contexts.update()

        newContext.custom_name = collection.name
        generatedRendersets.append(newContext)

        bpy.data.scenes[scene].camera = bpy.data.objects[camera]

    return generatedRendersets


def resetAll():
    contexts = bpy.data.scenes[scene].renderset_contexts
    collections = bpy.data.scenes[scene].id_data.view_layers[viewlayer].layer_collection.children
    templateToSearch = f"{prefix}_{templateString}"

    for idx, context in enumerate(contexts.values()):
        print(f"{context.custom_name}")
        if(context.custom_name != 'New Context'):
            contexts.remove(idx)
    
    contexts.update()
    return False
            

def assignCollectionToRenderset():
    contexts = bpy.data.scenes[scene].renderset_contexts
    collections = bpy.data.scenes[scene].id_data.view_layers[viewlayer].layer_collection.children

    for idx in range(len(contexts.values())):
        if(idx == 0):
            continue
        bpy.data.scenes[scene].renderset_context_index = idx
        rcName = contexts[idx].custom_name
        print(f"************************ {rcName}")
        for jdx, collection in enumerate(collections.values()):
            cName = collection.name
            collection.exclude = True
            print(f"******************* {alwaysInclude in cName}")
            if(rcName == cName or alwaysInclude in cName):
                collection.exclude = False
            bpy.data.scenes[scene].id_data.view_layers[viewlayer].update()



    return False



templates = getAllTemplateCollections()
generatedCollections = generateCollections(templates)
generatedRendersets = generateRendersets(generatedCollections)

assignCollectionToRenderset()


# resetAll()


print("HELLO WORLD")
#lala()