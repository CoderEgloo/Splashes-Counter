import os, getpass

path = "/Applications/Minecraft.app"
os.system(f"open {path}")
username = getpass.getuser()
with open ('/Users/'+username+'/Library/Application Support/minecraft/resourcepacks/Splash/assets/minecraft/log.txt', 'a') as f:
    f.write("lol\n")


    with open ('/Users/'+username+'/Library/Application Support/minecraft/resourcepacks/Splash/assets/minecraft/log.txt', 'r') as f:
        x = len(f.readlines())

    with open ('/Users/'+username+'/Library/Application Support/minecraft/resourcepacks/Splash/assets/minecraft/texts/splashes.txt', 'w') as f:
        f.write("Opened " + str(x) + " times!")