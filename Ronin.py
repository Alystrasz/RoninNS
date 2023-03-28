import os
print("Ronin - The CLI to update Northstar on Linux")
print("Latest version: unknown. Manual required.")
print("Version syntax: vx.xx.x, where x is a number. Without the v.")
while True:
    version = input("Enter the version to download: ")
    prompt = input("Update NS? (y/n) ")
    if prompt == 'y':
        print("Now updating/installing...")
        os.system("sudo yum install curl")
        try:
            os.system(f"sudo mkdir ~/.ronintemp; cd ~/.ronintemp; curl https://github.com/R2Northstar/Northstar/releases/download/v{version}/Northstar.release.v{version}.zip; unzip Northstar.release.v{version}.zip; cp -a ./Northstar.release.v{version}/. ~/.local/share/Steam/steamapps/common/Titanfall2; cd ~; rm -r ./.ronintemp")
            print("Successfully installed Northstar!")
        except:
            print("Download failed: you may have entered an invalid version.")
    elif version == 'n':
        print("Aborted.")
        exit()
    else:
        print("Invalid option; try again.")