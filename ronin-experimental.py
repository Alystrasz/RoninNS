# RoninNS initialization #
import os
rver = "1.1.0"
def grabninstall(version):
  print("Grabbing latest version detected in varlib...")
  if os.path.exists("~/.ronin/"):
    print("Ronin directory already created.")
  else:
    print("Creating Ronin directory...")
    os.system("mkdir ~/.ronin/")
  os.system("cd ~/.ronin/; curl github.com/Command-Git/RoninNS/varlib/varlib.rnin")
  with open("~/.ronin/varlib.rnin/", 'r') as getLatest:
    version = getLatest.read()
    getLatest.close()
  print(f"Commencing grab of NS v{version} (latest).")
  os.system(f"cd ~/.ronin/; curl github.com/R2Northstar/Northstar/v{version}/Northstar.release.v{version}.zip/")
  os.system(f"cd ~/.ronin/; unzip Northstar.release.v{version}.zip; cp -a ./Northstar.release.v{version}/. ~/.local/share/Steam/steamapps/common/Titanfall2/")
  os.system(f"cd ~/.ronin/; rm -r ./Northstar.release.v{version}.zip/ ./Northstar.release.v{version}/")
  print("Northstar (should) now be successfully installed!")
def grab(version):
  print(f"Grabbing NS v{version} (latest) and saving to Downloads directory.")
  if os.path.exists("~/.ronin/"):
    print("Ronin directory already created.")
  else:
    print("Creating Ronin directory...")
    os.system("mkdir ~/.ronin/")
  netgrab("github.com/Command-Git/RoninNS/varlib/varlib.rnin/")
  with open("~/.ronin/varlib.rnin/", 'r') as getLatest:
    version = getLatest.read()
    getLatest.close()
  os.system(f"cd ~/Downloads; curl github.com/R2Northstar/Northstar/v{version}/Northstar.release.v{version}.zip/")
  print(f"Done! NS v{version} should now be in your Downloads.")
def netgrab(file):
  os.system(f"curl {file}")
# Initialization done #
print(f"RoninNS for RPM v{rver}")
while True:
  print("Choose an option:\n1. Grab 'n Install\n2. Grab\n0. Exit RoninNS")
  option = input("Option: ")
  if option == '1':
    break
    grabninstall("")
  elif option == '2':
    break
    grab("")
  elif option == '0':
    exit()
  else:
    print("Invalid option; try again.")
