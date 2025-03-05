# pylint: disable=fixme, import-error
import bpy
import os
import json

###########################
file = "test.json"
templateString = "tmp"
alwaysInclude = "studio"
prefix = ""
collectionsToEnable = ["studio_environment", "walls", "floor/ceiling"]

# opens json file to get all the variations
def getJson(json_file):
    data = {}
    directory = bpy.path.abspath("//")
    jasonFile = os.path.join(directory, json_file)
    with open(jasonFile) as data_file:
        data = json.load(data_file)

    return data

# generates both the rendersets and collections
def getAllTemplateCollections():
    templates = {}
    for collection in bpy.data.collections:
        if (templateString in collection.name):
            templates[collection.name] = collection

    return templates


 # create objects with all necessary variables to then generate rendersets and collections
def generateSets(variations, collections):
    generatedRendersets = []

    for variation in variations:
        for template in variations[variation]["materials"]:
            varName = f'{prefix}{variation.removeprefix(f"{templateString}_")}_{template}'
            varCamera = variations[variation]["camera"]
            varViewLayer = variations[variation]["viewlayer"]
            varScene = variations[variation]["scene"]
            varWorld = variations[variation]["world"]
            varCollection = collections[variation]
            varTemplate = template
            varMaterials = variations[variation]["materials"][template]
            
            
            setInfo = {"parent": variation, "renderset": varName, "template": varTemplate, "materials": varMaterials,
                    "camera": varCamera, "viewlayer": varViewLayer, "scene": varScene, "world": varWorld, "collection": varCollection}
            generatedRendersets.append(setInfo)

    return generatedRendersets

# generates both the rendersets and collections
def generateRendersetsCollections():
    variations = getJson(file)
    templates = getAllTemplateCollections()
    setPairs = generateSets(variations, templates)
    
    contexts = bpy.context.scene.renderset_contexts
    contexts.clear()
    
    # exclude all collections with the prefix from rendering
    for collection in bpy.context.scene.view_layers["View Layer"].layer_collection.children:
        if (collection.name not in collectionsToEnable):
            collection.exclude = True
            
    totalTemplates = len(templates)
    totalUsedTemplates =len(variations)
    totalSetPair = len(setPairs)
    
    print(f"Creating {totalSetPair} collections and rendersets from {totalUsedTemplates} template of {totalTemplates} available templates")
    
    
    hasSibling = variations.get('sibling', None)
    if hasSibling != None:
        print(f"****{variations['sibling']}")
    
    for idx, setPair in enumerate(setPairs):
        # create the rendersets
        newContext = contexts.add()
        newContext.custom_name = setPair["renderset"]
        contexts.update()


        # create the collections
        newCollection = bpy.data.collections.new(setPair["renderset"])
        bpy.context.scene.collection.children.link(newCollection)
        bpy.context.scene.view_layers["View Layer"].layer_collection.children[newCollection.name].exclude = True
        
        # assign collections to rendersets
        scene = setPair['scene']
        viewlayer = setPair['viewlayer']
        camera = setPair['camera']
        materials = setPair['materials']
        world = setPair['world']
        contexts = bpy.data.scenes[scene].renderset_contexts
        collections = bpy.data.scenes[scene].id_data.view_layers[viewlayer].layer_collection.children

        for idx, context in enumerate(contexts.values()):
            # not sure why we had this before
            # if(idx == 0):
            #     continue
            bpy.data.scenes[scene].renderset_context_index = idx
            bpy.context.scene.camera = bpy.data.objects[camera]
            bpy.context.scene.world = bpy.data.worlds[world]
            rcName = context.custom_name
            
            for jdx, collection in enumerate(collections.values()):
                cName = collection.name
                collection.exclude = True
                if(rcName == cName or alwaysInclude in cName):
                    collection.exclude = False
                bpy.data.scenes[scene].id_data.view_layers[viewlayer].update()
        
        # copy objects from the source collection to the new target collection
        sourceCollection = setPair["collection"]
        targetCollection = newCollection
        objects = sourceCollection.objects

        for obj in objects:
            tempObjData = obj.data.copy() # copies object data
            newObj = obj.copy() # instances object to keep modifiers and transforms
            newObj.data = tempObjData # replaces instanced data with new object data
            targetCollection.objects.link(newObj)
            
            # replace dummy materials with materials
            for slot in newObj.material_slots:
                if (slot.name in materials.keys() and materials[slot.name] in bpy.data.materials.keys()):
                    newMaterial = bpy.data.materials[materials[slot.name]]
                    slot.material = newMaterial
        print(f"--- finished creating renderset/collection {idx+1} of {totalSetPair}")
    return None


def swapper(generate, printTemplates, printVariations, printSetPairs):
    print(chr(27) + "[2J")
    if(printTemplates):
        templates = getAllTemplateCollections()
        print("################################### ALL TEMPLATES ###################################")
        for template in templates:
            print(template)
            
    if(printVariations):
        variations = getJson(file)
        print("################################### TEMPLATES TO GENERATE ###################################")
        for variation in variations:
            print(variation)
            
    if(printSetPairs):
        setPairs = generateSets(variations, templates)
        print("################################### SET PAIRS ###################################")
        for setPair in setPairs:
            print(f"{setPair['parent']} --- {setPair['renderset']}")
    
    if(generate):
        print("################################### STARTING ###################################")
        generateRendersetsCollections()
        print("################################### FINISHED ###################################")


swapper(True, False, False, False)