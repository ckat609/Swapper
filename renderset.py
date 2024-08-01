# context.area: EMPTY
import bpy
import time

filename = bpy.path.basename(
    bpy.context.blend_data.filepath).removesuffix('.blend')
templateString = "template_"
templateStringsToIgnore = ['template_', 'studio_']
prefix = "decorplus"
variations = {
    "white_white": {"dummyMetal": "metalPaintedWhite", "dummyWood": "woodWhite", "dummyPlastic": "plasticWhite"},
    "white_grey": {"dummyMetal": "metalPaintedWhite", "dummyWood": "woodGrey", "dummyPlastic": "plasticWhite"},
    "white_birch": {"dummyMetal": "metalPaintedWhite", "dummyWood": "woodBirch", "dummyPlastic": "plasticWhite"},
    "white_walnut": {"dummyMetal": "metalPaintedWhite", "dummyWood": "woodWalnut", "dummyPlastic": "plasticWhite"},
    "platinum_white": {"dummyMetal": "metalPaintedPlatinum", "dummyWood": "woodWhite", "dummyPlastic": "plasticGray"},
    "platinum_grey": {"dummyMetal": "metalPaintedPlatinum", "dummyWood": "woodGrey", "dummyPlastic": "plasticGray"},
    "platinum_birch": {"dummyMetal": "metalPaintedPlatinum", "dummyWood": "woodBirch", "dummyPlastic": "plasticGray"},
    "platinum_walnut": {"dummyMetal": "metalPaintedPlatinum", "dummyWood": "woodWalnut", "dummyPlastic": "plasticGray"},
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
    templateToRemove = f"{prefix}_{sourceCollection.name.removeprefix(templateString)}_"
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
            newCollectionName = f"{prefix}_{collection.name.removeprefix(templateString)}_{variation}"
            newCollection = col.new(newCollectionName)
            
            bpy.context.scene.collection.children.link(newCollection)
            generatedCollections.append(newCollection)
            bpy.context.view_layer.layer_collection.children[newCollectionName].exclude = True

            # renderset
            newContext = bpy.context.scene.renderset_contexts.add()
            newContext.custom_name = newCollection.name

            # objects
            duplicateObjectsInCollectionAssignModify(
                collection, newCollection, variations)

    return generatedCollections


def generateRendersets(collections):
    for collection in collections:
        newContext = bpy.context.scene.renderset_contexts.add()
        newContext.custom_name = collection.name
        

    return False

def assignCollectionToRenderset():
    # this is where we want to iterate over each context and asssign the collections that we want to render
    # for context in bpy.context.scene.render_set_contexts:
    renderset_contexts = bpy.data.scenes["Scene"].renderset_contexts

    for idx, renderset_context in enumerate(renderset_contexts):
        aName = renderset_context.custom_name
        print(f"****************** {renderset_context.custom_name} --- {aName in renderset_context.id_data.view_layers['View Layer'].layer_collection.children.keys()}")
        
        if(aName in renderset_context.id_data.view_layers['View Layer'].layer_collection.children.keys()):
            renderset_context.id_data.view_layers['View Layer'].layer_collection.children[aName].exclude = False

    return False





templates = getAllTemplateCollections()
generatedCollections = generateCollections(templates)
assignCollectionToRenderset()

