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
prefix = ""
variations = {
    "template_classic_ventilated": {
        "white": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyPlastic": "plasticWhite"},
        "platinum": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyPlastic": "plasticGray"},
        "graphite": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyPlastic": "plasticGraphite"},
    },
    "template_classic_trim": {
        "white_white": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyWood": "woodWhite", "dummyPlastic": "plasticWhite", },
        "white_grey": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyWood": "woodGrey", "dummyPlastic": "plasticWhite", },
        "white_birch": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyWood": "woodBirch", "dummyPlastic": "plasticWhite", },
        "white_walnut": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyWood": "woodWalnut", "dummyPlastic": "plasticWhite", },
        "platinum_white": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyWood": "woodWhite", "dummyPlastic": "plasticGray", },
        "platinum_grey": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyWood": "woodGrey", "dummyPlastic": "plasticGray", },
        "platinum_birch": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyWood": "woodBirch", "dummyPlastic": "plasticGray", },
        "platinum_walnut": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyWood": "woodWalnut", "dummyPlastic": "plasticGray", },
        "graphite_white": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyWood": "woodWhite", "dummyPlastic": "plasticGraphite", },
        "graphite_grey": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyWood": "woodGrey", "dummyPlastic": "plasticGraphite", },
        "graphite_birch": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyWood": "woodBirch", "dummyPlastic": "plasticGraphite", },
        "graphite_walnut": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyWood": "woodWalnut", "dummyPlastic": "plasticGraphite", },
    },
    "template_classic_decor": {
        "white_white": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyWood":"woodWhite", "dummyPlastic": "plasticWhite"},
        "white_grey": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyWood":"woodGrey", "dummyPlastic": "plasticWhite"},
        "white_birch": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyWood":"woodBirch", "dummyPlastic": "plasticWhite"},
        "white_walnut": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyWood":"woodWalnut", "dummyPlastic": "plasticWhite"},
        "platinum_white": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyWood":"woodWhite", "dummyPlastic": "plasticGray"},
        "platinum_grey": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyWood":"woodGrey", "dummyPlastic": "plasticGray"},
        "platinum_birch": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyWood":"woodBirch", "dummyPlastic": "plasticGray"},
        "platinum_walnut": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyWood":"woodWalnut", "dummyPlastic": "plasticGray"},
        "graphite_white": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyWood":"woodWhite", "dummyPlastic": "plasticGraphite"},
        "graphite_grey": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyWood":"woodGrey", "dummyPlastic": "plasticGraphite"},
        "graphite_birch": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyWood":"woodBirch", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyWood":"woodWalnut", "dummyPlastic": "plasticGraphite"},
    },
    "template_classic_trim_fronts_classic": {
        "white_white_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyWood":"woodWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_grey_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyWood":"woodGrey", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_birch_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyWood":"woodBirch", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_walnut_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyWood":"woodWalnut", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "platinum_white_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyWood":"woodWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_grey_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyWood":"woodGrey", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_birch_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyWood":"woodBirch", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_walnut_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyWood":"woodWalnut", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "graphite_whit_nickele": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyWood":"woodWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyWood":"woodGrey", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyWood":"woodBirch", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyWood":"woodWalnut", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        
        "white_white_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_grey_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_birch_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_walnut_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "platinum_white_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_grey_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_birch_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_walnut_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "graphite_white_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        
        "white_white_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_grey_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_birch_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_walnut_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "platinum_white_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_grey_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_birch_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_walnut_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "graphite_white_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
    },
    "template_classic_trim_fronts_flat": {
        "white_white_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_grey_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_birch_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_walnut_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "platinum_white_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_grey_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_birch_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_walnut_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "graphite_white_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        
        "white_white_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_grey_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_birch_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_walnut_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "platinum_white_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_grey_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_birch_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_walnut_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "graphite_white_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        
        "white_white_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_grey_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_birch_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_walnut_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "platinum_white_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_grey_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_birch_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_walnut_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "graphite_white_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
    },
    "template_classic_trim_fronts_modern": {
        "white_white_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_grey_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_birch_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_walnut_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "platinum_white_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_grey_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_birch_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_walnut_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "graphite_white_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        
        "white_white_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_grey_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_birch_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_walnut_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "platinum_white_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_grey_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_birch_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_walnut_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "graphite_white_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        
        "white_white_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_grey_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_birch_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_walnut_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "platinum_white_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_grey_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_birch_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_walnut_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "graphite_white_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
    },
    "template_classic_decor_fronts_classic": {
        "white_white_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_grey_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_birch_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_walnut_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "platinum_white_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_grey_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_birch_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_walnut_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "graphite_white_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        
        "white_white_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_grey_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_birch_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_walnut_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "platinum_white_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_grey_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_birch_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_walnut_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "graphite_white_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        
        "white_white_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_grey_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_birch_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_walnut_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "platinum_white_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_grey_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_birch_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_walnut_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "graphite_white_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
    },
    "template_classic_decor_fronts_flat": {
        "white_white_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_grey_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_birch_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_walnut_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "platinum_white_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_grey_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_birch_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_walnut_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "graphite_white_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        
        "white_white_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_grey_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_birch_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_walnut_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "platinum_white_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_grey_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_birch_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_walnut_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "graphite_white_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        
        "white_white_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_grey_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_birch_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_walnut_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "platinum_white_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_grey_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_birch_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_walnut_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "graphite_white_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
    },
    "template_classic_decor_fronts_modern": {
        "white_white_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_grey_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_birch_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "white_walnut_nickel": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticWhite"},
        "platinum_white_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_grey_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_birch_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "platinum_walnut_nickel": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGray"},
        "graphite_white_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_nickel": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalDoorknobBrushed", "dummyPlastic": "plasticGraphite"},
        
        "white_white_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_grey_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_birch_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "white_walnut_chrome": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticWhite"},
        "platinum_white_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_grey_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_birch_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "platinum_walnut_chrome": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGray"},
        "graphite_white_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_chrome": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"metalChrome", "dummyPlastic": "plasticGraphite"},
        
        "white_white_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_grey_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_birch_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "white_walnut_bronze": {"dummyMetal": "metalPaintedWhite", "dummyMesh": "metalMeshWhite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticWhite"},
        "platinum_white_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_grey_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_birch_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "platinum_walnut_bronze": {"dummyMetal": "metalPaintedPlatinum", "dummyMesh": "metalMeshPlatinum", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGray"},
        "graphite_white_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_grey_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_birch_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
        "graphite_walnut_bronze": {"dummyMetal": "metalPaintedGraphite", "dummyMesh": "metalMeshGraphite", "dummyMetalKnob":"bronzeOilRubbed", "dummyPlastic": "plasticGraphite"},
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
    prefixStr = f"{prefix}_" if len(prefix) > 0 else""
    templateToRemove = f"{prefixStr}{sourceCollection.name.removeprefix(f'{templateString}_')}"
    col = bpy.data.collections
    objects = sourceCollection.objects

    for obj in objects:
        newObj = duplicateObject(obj)
        newObj.location = obj.location
        addObjectToCollection(newObj, targetCollection)

        # replace materials
        for slot in newObj.material_slots:
            pref = targetCollection.name.removeprefix(f"{templateToRemove}_")
            if (pref in variations[sourceCollection.name] and slot.material.name in variations[sourceCollection.name][pref]):
                mat = variations[sourceCollection.name][pref][slot.material.name]
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
        for idx, template in enumerate(variations):
            for variation in variations[template]:
                #collections
                prefixStr = f"{prefix}_" if len(prefix) > 0 else""
                newCollectionName = f"{prefixStr}{collection.name.removeprefix(f'{templateString}_')}_{variation}"
                if(collection.name == list(variations.keys())[idx]):
                    newCollection = col.new(newCollectionName)
                    
                    bpy.context.scene.collection.children.link(newCollection)
                    generatedCollections.append(newCollection)
                    
                    bpy.context.view_layer.layer_collection.children[newCollectionName].exclude = True

                    # objects
                    duplicateObjectsInCollectionAssignModify(
                    collection, newCollection, variations)
                    

    return generatedCollections

# def generateCollections(collections):
#     col = bpy.data.collections
#     generatedCollections = []
#     for collection in collections:
#         for variation in variations:
#             # collections
#             newCollectionName = f"{prefix}{collection.name.removeprefix(templateString)}_{variation}"
#             newCollection = col.new(newCollectionName)
            
#             bpy.context.scene.collection.children.link(newCollection)
#             generatedCollections.append(newCollection)
            
#             bpy.context.view_layer.layer_collection.children[newCollectionName].exclude = True

#             # objects
#             duplicateObjectsInCollectionAssignModify(
#                collection, newCollection, variations)

#     return generatedCollections


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