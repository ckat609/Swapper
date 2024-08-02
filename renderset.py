# context.area: EMPTY
import bpy
import time



#these values can probably be retrieved from the current scene and view layer
###########################
scene = "Scene"
viewlayer = "View Layer"
###########################
filename = bpy.path.basename(
    bpy.context.blend_data.filepath).removesuffix('.blend')
templateString = "template"
alwaysInclude = 'studio'
prefix = "decorplus"
variations = {
    "template_classic_ventilated_closet_style_card": {
    "white_white": {"dummyMetal": "metalPaintedWhite", "dummyPlastic": "plasticWhite"},
    "white_grey": {"dummyMetal": "metalPaintedWhite", "dummyPlastic": "plasticWhite"},
    "white_birch": {"dummyMetal": "metalPaintedWhite", "dummyPlastic": "plasticWhite"},
    "white_walnut": {"dummyMetal": "metalPaintedWhite", "dummyPlastic": "plasticWhite"},
    "platinum_white": {"dummyMetal": "metalPaintedPlatinum", "dummyPlastic": "plasticGray"},
    "platinum_grey": {"dummyMetal": "metalPaintedPlatinum", "dummyPlastic": "plasticGray"},
    "platinum_birch": {"dummyMetal": "metalPaintedPlatinum", "dummyPlastic": "plasticGray"},
    "platinum_walnut": {"dummyMetal": "metalPaintedPlatinum", "dummyPlastic": "plasticGray"},
    },
    "template_classic_trim_closet_style_card": {
    "white_white": {"dummyMetal": "metalPaintedWhite", "dummyWood": "woodWhite", "dummyPlastic": "plasticWhite"},
    "white_grey": {"dummyMetal": "metalPaintedWhite", "dummyWood": "woodGrey", "dummyPlastic": "plasticWhite"},
    "white_birch": {"dummyMetal": "metalPaintedWhite", "dummyWood": "woodBirch", "dummyPlastic": "plasticWhite"},
    "white_walnut": {"dummyMetal": "metalPaintedWhite", "dummyWood": "woodWalnut", "dummyPlastic": "plasticWhite"},
    "platinum_white": {"dummyMetal": "metalPaintedPlatinum", "dummyWood": "woodWhite", "dummyPlastic": "plasticGray"},
    "platinum_grey": {"dummyMetal": "metalPaintedPlatinum", "dummyWood": "woodGrey", "dummyPlastic": "plasticGray"},
    "platinum_birch": {"dummyMetal": "metalPaintedPlatinum", "dummyWood": "woodBirch", "dummyPlastic": "plasticGray"},
    "platinum_walnut": {"dummyMetal": "metalPaintedPlatinum", "dummyWood": "woodWalnut", "dummyPlastic": "plasticGray"},
    },

}


def duplicateObject(obj):
    newMesh = obj.data.copy()
    newObj = bpy.data.objects.new(obj.name, newMesh)

    return newObj


def addObjectToCollection(obj, collection):
    col = bpy.data.collections
    collectionName = collection.name
    collection.objects.link(obj)


def duplicateObjectsInCollectionAssignModify(sourceCollection, targetCollection, variations):
    templateToRemove = f"{prefix}_{sourceCollection.name.removeprefix(f'{templateString}_')}_"
    col = bpy.data.collections
    objects = sourceCollection.objects

    for obj in objects:
        newObj = duplicateObject(obj)
        newObj.location = obj.location
        addObjectToCollection(newObj, targetCollection)

        # replace materials
        for slot in newObj.material_slots:
            pref = targetCollection.name.removeprefix(templateToRemove)
            if (pref in variations and slot.material.name in variations[pref]):
                # if (slot.material.name in variations[pref]):
                mat = variations[pref][slot.material.name]
                slot.material = bpy.data.materials[mat]


def getAllTemplateCollections():
    templates = []
    for collection in bpy.data.collections:
        if ("template" in collection.name):
            templates.append(collection)

    return templates


def generateCollections(collections):
    col = bpy.data.collections
    generatedCollections = []
    for collection in collections:
        for variation in variations:
            # collections
            newCollectionName = f"{prefix}{collection.name.removeprefix(templateString)}_{variation}"
            newCollection = col.new(newCollectionName)
            
            bpy.context.scene.collection.children.link(newCollection)
            generatedCollections.append(newCollection)
            
            bpy.context.view_layer.layer_collection.children[newCollectionName].exclude = True

            # objects
            duplicateObjectsInCollectionAssignModify(
               collection, newCollection, variations)

    return generatedCollections


def generateRendersets(collections):
    generatedRendersets = []
    for collection in collections:
        newContext = bpy.context.scene.renderset_contexts.add()
        bpy.context.scene.renderset_contexts.update()
        newContext.custom_name = collection.name
        generatedRendersets.append(newContext)

    return generatedRendersets


def resetAll():
    contexts = bpy.data.scenes[scene].renderset_contexts
    collections = bpy.data.scenes[scene].id_data.view_layers[viewlayer].layer_collection.children
    templateToSearch = f"{prefix}_{templateString}"

    # for idx in range(len(contexts.values())):
    #     if(idx == 0):
    #         continue
    #     print(templateToSearch)
    #     if(prefix in contexts[idx].custom_name):
    #         print(f"{contexts[idx].custom_name} --- {templateToSearch in contexts[idx].custom_name}")
    #         contexts.remove(idx)
    #         contexts.update()

    for idx in range(len(collections.values())):
        return False
            

def assignCollectionToRenderset():
    contexts = bpy.data.scenes[scene].renderset_contexts
    collections = bpy.data.scenes[scene].id_data.view_layers[viewlayer].layer_collection.children

    for idx in range(len(contexts.values())):
        if(idx == 0):
            continue
        bpy.data.scenes[scene].renderset_context_index = idx
        rcName = contexts[idx].custom_name
        for jdx, collection in enumerate(collections.values()):
            cName = collection.name
            collection.exclude = True
            print(f"************************ {cName} --- {alwaysInclude in cName}")
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