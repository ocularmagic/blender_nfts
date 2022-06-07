#Voxel Dragon NFT Creation

#Created for use with Blender 3.0.0

#Import necessary dependancies
import bpy
import json
import os
import sys


#hornstripes and skinstripes default to false so they will not render on the dragon.
hornstripes = 0
skinstripes = 0


nft_number = 1 #Set the NFT counter to 1

#####################################################################################
#The output_all_files function takes the skin color, horn color, and eye color values. 
#It defines the JSON structure, renders the image, then saves the image and JSON file 
#to the same folder.
#####################################################################################

def output_all_files(skincolor_final, horncolor_final, eyecolor_final):
	global nft_number #We'll be using the global NFT count in this final function to write the image and json files.
	global hornstripes #This is the global true/false holder that lets the script know if it should render horn stripes or not.
	global skinstripes #This is the global true/false holder that lets the script know if it should render skin stripes or not.

	hornstripestf = "" #This is just a string holder for "Yes" or "No" for the horn stripes so we can place it in the JSON structure.
	skinstripestf = "" #This is just a string holder for "Yes" or "No" for the skin stripes so we can place it in the JSON structure.
	item_names = "Voxel Dragon #" #This is the prefix for the name of the specific NFT that will be generated.


	#These if/else statements just set the string values based on the true/false values of the global variable. I'm sure
	#there is a better way to do this.
	if hornstripes == 1:
		hornstripestf = "Yes"
	else:
		hornstripestf = "No"

	if skinstripes == 1:
		skinstripestf = "Yes"
	else:
		skinstripestf = "No"

	#The default JSON Data formatted below can be used to mint on the Elrond blockchain (Elrond.com)
	#through the Frame It marketplace (https://www.frameit.gg) using their smart contracts.
	#Always test mint on a test server beforehand in case something has changed. I am
	#not responsible for your failed mints.

	#You can format this data in any way you want so it works on any other blockchain.
	#I would highly recommend doing a test mint with the JSON you generate to make sure it works.
	json_data = { 
    		"name": f'{item_names}{nft_number}',
    		"description": "Voxel Dragons",
    		"edition": 1,
    		"attributes": [
        		{
        		"trait_type":"Skin Color",
        		"value":skincolor_final
        		},
        		{
        		"trait_type":"Horn Color",
        		"value":horncolor_final
        		},
        		{
        		"trait_type":"Eye Color",
        		"value":eyecolor_final
        		},
        		{
        		"trait_type":"Horn Stripes",
        		"value":hornstripestf
        		},
        		{
        		"trait_type":"Skin Stripes",
        		"value":skinstripestf
        		}
    		]
		}

	#Render the scene

	#Set the output path to wherever you want the files to be created. They will all be in one folder.
	#Example: output_path = "/Users/username/Library"
	output_path = ""

	extension_string = ".png" #Set the image extension.
	extension_string = f'{nft_number}{extension_string}' #This combines the nft_number with the file extension. "1.png"
	scene = bpy.context.scene #I believe this takes all of the current scene values and stores them in "scene".
	scene.render.image_settings.file_format='PNG' #Define the image file format.
	bpy.context.scene.render.filepath = os.path.join(output_path, extension_string) #Store the entire output path and file name.
	bpy.ops.render.render(write_still=1) #Render the scene and save it to the directory

	#Write json data
	json_file_name = ".json" #Set the file extension for the metadata file.
	json_file_name = f'{nft_number}{json_file_name}' #This combines the nft_number with the file extension. "1.json"
	save_json_to = os.path.join(output_path, json_file_name) #Store the output_path and the file name into one variable.
	json_file = open(save_json_to, "w") #Open the JSON file for writing.
	json_data_formatted = json.dumps(json_data) #Format the JSON data to prepare it for writing.
	json.dump(json_data, json_file, indent=4) #Write the data to the file.

	nft_number += 1 #Increment the global NFT number.


#####################################################################################
#The eye_color function takes skin color and horn color values. 
#It changes the eye color in the scene, sets the eyecolor trait value,
#then calls the output_all_files function to render the scene and output the JSON.
#####################################################################################

def eye_color(skin, horncolor):

	eyecolor = "" #Creating an empty string variable to hold the eyecolor trait.

	#Red eyes
	#Change the material in the scene to a red color.
	bpy.data.materials["Eyes"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0, 0, 1)

	eyecolor = "Red" #Update the trait text.

	#Call the output_all_files function to render the image and output the JSON.
	output_all_files(skin, horncolor, eyecolor)

	
	######################Code below is the same as above, just for different colors#########################
	#Blue Eyes
	bpy.data.materials["Eyes"].node_tree.nodes["Emission"].inputs[0].default_value = (0.021219, 0.0241576, 0.610496, 1)
	eyecolor = "Blue"
	output_all_files(skin, horncolor, eyecolor)

	#GreenEyes
	bpy.data.materials["Eyes"].node_tree.nodes["Emission"].inputs[0].default_value = (0, 1, 0.00121415, 1)
	eyecolor = "Green"
	output_all_files(skin, horncolor, eyecolor)
	
	#Yellow Eyes
	bpy.data.materials["Eyes"].node_tree.nodes["Emission"].inputs[0].default_value = (1, 1, 0.0451863, 1)
	eyecolor = "Yellow"
	output_all_files(skin, horncolor, eyecolor)
	


#####################################################################################
#The change_horncolor function takes a skin color value. 
#It changes the horn color in the scene, sets the horncolor trait value,
#then calls the eye_color function to set the eye_color.
#####################################################################################
def change_horncolor(skin):

	horncolor = "" #Creating an empty string variable to hold the horncolor trait.

	horncolor = "LT-Grey"  #Update the trait text.

	#Change the material in the scene to a a light grey color.
	bpy.data.materials["Horns"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.246202, 0.246201, 0.246201, 1)

	#Set the horn stripes to the exact same color as the horns so they appear invisible when rendered.
	bpy.data.materials["Horn Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.246202, 0.246201, 0.246201, 1)

	#If the hornstripes true/false value is set to true, change the horn stripes to a dark grey.
	if hornstripes == 1:
		bpy.data.materials["Horn Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.0466651, 0.0466651, 0.0466651, 1)

	#Call the eye_color function sending the skin trait and the horncolor trait.
	eye_color(skin, horncolor)

	######################Code below is the same as above, just for different colors#########################

	#Set horn color to green
	bpy.data.materials["Horns"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.124772, 0.502886, 0.124772, 1)
	bpy.data.materials["Horn Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.124772, 0.502886, 0.124772, 1)
	if hornstripes == 1:
		bpy.data.materials["Horn Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.0466651, 0.0466651, 0.0466651, 1)

	eye_color(skin, horncolor)

	#Set horn color to orange
	bpy.data.materials["Horns"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 0.278894, 0, 1)
	bpy.data.materials["Horn Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 0.278894, 0, 1)
	if hornstripes == 1:
		bpy.data.materials["Horn Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.0466651, 0.0466651, 0.0466651, 1)

	eye_color(skin, horncolor)

	#Set horn color to lavender
	bpy.data.materials["Horns"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.450786, 0.127438, 0.760525, 1)
	bpy.data.materials["Horn Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.450786, 0.127438, 0.760525, 1)
	if hornstripes == 1:
		bpy.data.materials["Horn Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.0466651, 0.0466651, 0.0466651, 1)

	eye_color(skin, horncolor)


#####################################################################################
#The process_scene function doesn't take any values, this is just the entry point
#for everything else.
#It sets the skin color for the dragon the callse the change_horncolor function,
#passing in the skin color to move onto the next step.
#####################################################################################
def process_scene():

	skin = "" #Creating an empty string variable to hold the skin trait.
	
	skin = "Black" #Update the trait text.

	#Change the skin material in the scene to black.
	bpy.data.materials["Skin"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.0742136, 0.0742136, 0.0742136, 1)

	#Set the skin stripes to the exact same color as the skin so they appear invisible when rendered.
	bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.0742136, 0.0742136, 0.0742136, 1)

	#If the skinstripes true/false value is set to true, change the skin stripes to a different value.
	if skinstripes == 1:
		bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.254152, 0.254152, 0.254152, 1)

	#Call the change_horncolor function sending the skin color trait.
	change_horncolor(skin)

	######################Code below is the same as above, just for different colors#########################

	#set skin to White
	skin = "White"
	bpy.data.materials["Skin"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.564712, 0.564712, 0.564712, 1)
	bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.564712, 0.564712, 0.564712, 1)
	
	if skinstripes == 1:
		bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.254152, 0.254152, 0.254152, 1)

	change_horncolor(skin)

	#set skin to Green
	skin = "Green"
	bpy.data.materials["Skin"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.000910582, 0.109462, 0, 1)
	bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.000910582, 0.109462, 0, 1)
	if skinstripes == 1:
		bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.254152, 0.254152, 0.254152, 1)

	change_horncolor(skin)

	#set skin to Brown
	skin = "Brown"
	bpy.data.materials["Skin"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.119539, 0.0307134, 0, 1)
	bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.119539, 0.0307134, 0, 1)
	if skinstripes == 1:
		bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.254152, 0.254152, 0.254152, 1)

	change_horncolor(skin)

	#set skin to Yellow
	skin = "Yellow"
	bpy.data.materials["Skin"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.332452, 0.215861, 0, 1)
	bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.332452, 0.215861, 0, 1)
	if skinstripes == 1:
		bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.254152, 0.254152, 0.254152, 1)

	change_horncolor(skin)

	#set skin to Blue
	skin = "Blue"
	bpy.data.materials["Skin"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0, 0.00856813, 0.434154, 1)
	bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0, 0.00856813, 0.434154, 1)
	if skinstripes == 1:
		bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.254152, 0.254152, 0.254152, 1)

	change_horncolor(skin)

	#set skin to Red
	skin = "Red"
	bpy.data.materials["Skin"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.376262, 0, 0, 1)
	bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.376262, 0, 0, 1)
	if skinstripes == 1:
		bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.254152, 0.254152, 0.254152, 1)

	change_horncolor(skin)

	#set skin to Pink
	skin = "Pink"
	bpy.data.materials["Skin"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.552012, 0.109462, 0.318547, 1)
	bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.552012, 0.109462, 0.318547, 1)
	if skinstripes == 1:
		bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.254152, 0.254152, 0.254152, 1)

	change_horncolor(skin)

	#set skin to Orange
	skin = "Orange"
	bpy.data.materials["Skin"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.291771, 0.0382043, 0, 1)
	bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.291771, 0.0382043, 0, 1)
	if skinstripes == 1:
		bpy.data.materials["Skin Stripes"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.254152, 0.254152, 0.254152, 1)

	change_horncolor(skin)


#############This is the first function call to start the process###############
process_scene()

################################################################################
#Since the stripes are just on/or off, we don't need a new function change them.
#To keep it simple I just turned them on/off and reran process_scene.
#There is probably a better/cleaner way to do this as well.
################################################################################

skinstripes = 1
hornstripes = 0
process_scene()
skinstripes = 0
hornstripes = 1
process_scene()
skinstripes = 1
hornstripes = 1
process_scene()

