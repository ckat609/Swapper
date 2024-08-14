import bpy
import os
import json
import time

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


# these values can probably be retrieved from the current scene and view layer
###########################
scene = "Scene"
viewlayer = "View Layer"
camera = "mainCamera"
###########################
file = "shelves.json"
templateString = "tmp"
alwaysInclude = 'studio'
prefix = ""

##


def getJson(json_file):
    data = {}
    directory = bpy.path.abspath("//")
    jasonFile = os.path.join(directory, json_file)
    with open(jasonFile) as data_file:
        data = json.load(data_file)

    return data


# def addObjectToCollection(obj, collection):
#     # col = bpy.data.collections
#     # collectionName = collection.name
#     collection.objects.link(obj)

# def duplicateObjectsInCollectionAssignModify(sourceCollection, targetCollection, variations):
#     prefixStr = f"{prefix}_" if len(prefix) > 0 else""
#     templateToRemove = f"{prefixStr}{sourceCollection.name.removeprefix(f'{templateString}_')}"
#     # col = bpy.data.collections
#     objects = sourceCollection.objects

#     for obj in objects:
#         newObj = obj.copy()
#         # newObj.location = obj.location
#         # targetCollection.objects.link(newObj)

#         # replace materials
#         for slot in obj.material_slots:
#             pref = targetCollection.name.removeprefix(f"{templateToRemove}_")
#             if (pref in variations[sourceCollection.name]['materials'] and slot.material.name in variations[sourceCollection.name]['materials'][pref]):
#                 mat = variations[sourceCollection.name]['materials'][pref][slot.material.name]
#                 slot.link = 'OBJECT'
#                 slot.material = bpy.data.materials[mat]


# def getAllTemplateCollections():
#     templates = []
#     for collection in bpy.data.collections:
#         if (templateString in collection.name):
#             templates.append(collection)

#     return templates


# def generateCollections(templates):
#     col = bpy.data.collections
#     generatedCollections = []

#     for template in templates:
#         # print(f"***** template: {template.name}")
#         # print(f"***** keys: { list(variations.keys())}")
#         # print(f"***** template: {template.name}")
#         if(template.name in list(variations.keys())):
#             # print(f"*************** IM IN!!!!: {template.name}")
#             for variation in variations[f"{template.name}"]["materials"]:
#                 #collections
#                 prefixStr = f"{prefix}_" if len(prefix) > 0 else""
#                 newCollectionName = f"{prefixStr}{template.name.removeprefix(f'{templateString}_')}_{variation}"
#                 newCollection = template.copy()
#                 newCollection.name = newCollectionName
#                 # bpy.data.scenes[scene].collection.children.link(newCollection)

#                 bpy.context.scene.collection.children.link(newCollection)
#                 generatedCollections.append(newCollection)

#                 bpy.context.view_layer.layer_collection.children[newCollectionName].exclude = True

#                 # objects
#                 duplicateObjectsInCollectionAssignModify(template, newCollection, variations)


#     return generatedCollections


# def generateRendersets(collections):
#     generatedRendersets = []
#     prefixStr = f"{prefix}_" if len(prefix) > 0 else""

#     for collection in collections:
#         newContext = bpy.context.scene.renderset_contexts.add()
#         bpy.context.scene.renderset_contexts.update()

#         newContext.custom_name = collection.name
#         generatedRendersets.append(newContext)

#         bpy.data.scenes[scene].camera = bpy.data.objects[camera]

#     return generatedRendersets


# def resetAll():
#     contexts = bpy.data.scenes[scene].renderset_contexts
#     collections = bpy.data.scenes[scene].id_data.view_layers[viewlayer].layer_collection.children
#     templateToSearch = f"{prefix}_{templateString}"

#     for idx, context in enumerate(contexts.values()):
#         print(f"{context.custom_name}")
#         if(context.custom_name != 'New Context'):
#             contexts.remove(idx)

#     contexts.update()
#     return False


# def assignCollectionToRenderset():
#     contexts = bpy.data.scenes[scene].renderset_contexts
#     collections = bpy.data.scenes[scene].id_data.view_layers[viewlayer].layer_collection.children

#     for idx in range(len(contexts.values())):
#         if(idx == 0):
#             continue
#         bpy.data.scenes[scene].renderset_context_index = idx
#         rcName = contexts[idx].custom_name
#         print(f"************************ {rcName}")
#         for jdx, collection in enumerate(collections.values()):
#             cName = collection.name
#             collection.exclude = True
#             print(f"******************* {alwaysInclude in cName}")
#             if(rcName == cName or alwaysInclude in cName):
#                 collection.exclude = False
#             bpy.data.scenes[scene].id_data.view_layers[viewlayer].update()


#     return False


# templates = getAllTemplateCollections()
# generatedCollections = generateCollections(templates)
# generatedRendersets = generateRendersets(generatedCollections)

# assignCollectionToRenderset()


# resetAll()

def getAllTemplateCollections():
    templates = {}
    for collection in bpy.data.collections:
        if (templateString in collection.name):
            templates[collection.name] = collection

    return templates


def generateSets(variations, collections):
    generatedRendersets = []
    variationKeys = list(variations.keys())
    prefixStr = f"{prefix}_" if len(prefix) > 0 else ""

    for variation in variations:
        for template in variations[variation]['materials']:
            varName = f"{prefix}{variation.removeprefix(f'{templateString}_')}_{template}"
            varCamera = variations[variation]['camera']
            varViewLayer = variations[variation]['viewlayer']
            varScene = variations[variation]['scene']
            varCollection = collections[variation]
            varTemplate = template
            varMaterials = variations[variation]['materials'][template]
            generatedRendersets.append(
                {'renderset': varName, 'materials': varMaterials, 'template': varTemplate, 'camera': varCamera, 'viewlayer': varViewLayer, 'scene': varScene, 'collection': varCollection})
    # generatedRendersets.append(newContext)

    # bpy.data.scenes[scene].camera = bpy.data.objects[camera]

    return generatedRendersets


def generateRendersetsCollections(setPairs):
    contexts = bpy.context.scene.renderset_contexts
    contexts.clear()

    for setPair in setPairs:
        newContext = contexts.add()
        newContext.custom_name = setPair['renderset']
        contexts.update()

        # newCollection = bpy.data.collections.new(setPair["renderset"])
        # bpy.context.scene.collection.children.link(newCollection)

        # bpy.data.scenes[scene].id_data.view_layers[viewlayer].layer_collection.children[setPair["renderset"]].exclude = True

    return False


def assignCollectionToRendersets():
    contexts = bpy.context.scene.renderset_contexts

    for idx, context in enumerate(contexts):
        bpy.context.scene.renderset_context_index = idx

        for collection in bpy.data.scenes[scene].id_data.view_layers[viewlayer].layer_collection.children:
            isExcluded = True
            if (context.custom_name == collection.name or 'studio' in collection.name):
                isExcluded = False
            collection.exclude = isExcluded
    return False


def assignMaterials(setPairs):
    for setPair in setPairs:
        objs = bpy.data.scenes[setPair['scene']].id_data.view_layers[setPair['viewlayer']
                                                                     ].layer_collection.children[setPair['renderset']].collection.objects

        for obj in objs:
            for slot in obj.material_slots:
                if (slot.name in setPair['materials'].keys() and setPair['materials'][slot.name] in bpy.data.materials.keys()):
                    # slot.link = 'OBJECT'
                    newMaterial = bpy.data.materials[setPair['materials'][slot.name]]
                    # slot.material = newMaterial
                    # print(f"{slot.name in setPair['materials'].keys()}")
                    print(
                        f"####################### {slot.name} - {newMaterial.name}")
    return False


print("HELLO WORLD")

variations = getJson(file)
templates = getAllTemplateCollections()
sets = generateSets(variations, templates)
generateRendersetsCollections(sets)
assignCollectionToRendersets()
# assignMaterials(sets)

print("GOODBYE WORLD")
