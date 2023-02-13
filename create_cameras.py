import bpy

# Read the text file with camera information
with open("camera_info.txt", "r") as file:
    lines = file.readlines()

# Loop through each line in the text file
for line in lines:
    # Split the line into name and focal length
    name, focal_length = line.strip().split(":")
    # Create a new camera object
    camera = bpy.data.cameras.new(name)
    camera_object = bpy.data.objects.new(name, camera)
    # Set the camera's focal length
    camera.lens = float(focal_length)
    # Link the camera object to the scene
    bpy.context.scene.collection.objects.link(camera_object)
