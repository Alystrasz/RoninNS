import os
with open("verlib.rnin", 'r') as detect: # Get latest version in version library
  latest = detect.read()
  detect.close()
def grabInstall():
  print(f"What version do you want to download? The latest (in your local list) is {latest}. Type 'L' to get latest, or another version. (syntax: vX.X.X, where X is a number.)")
  version = input("Enter the version, or L for latest: ")
  if version == 'L':
    print("Grabbing latest...")
    os.system("cd ~; mkdir .ronintemp; cd .ronintemp; curl https://www.github.com/R2Northstar/Northstar/v{latest}/Northstar.release.v{latest}.zip; unzip Northstar.release.v{latest}.zip; cp -a Northstar.release.v{latest}. ~/.local/share/Steam/steamapps/common/Titanfall2; cd ~; rm -r .ronintemp")
    print("Installed Northstar!")
  else:
    print(f"Grabbing NS v{version}...")
    os.system("cd ~; mkdir .ronintemp; cd .ronintemp; curl https://www.github.com/R2Northstar/Northstar/v{version}/Northstar.release.v{version}.zip; unzip Northstar.release.v{version}.zip; cp -a Northstar.release.v{version}. ~/.local/share/Steam/steamapps/common/Titanfall2; cd ~; rm -r .ronintemp")
    print("Installed Northstar!")
def grab():
  print("Grab Tool - Select a version (L for latest)")
  version = input("Version: ")
  if version == 'L':
    print("Grabbing latest. It will be saved to Downloads.")
    os.system(f"cd ~/Downloads; curl https://www.github.com/R2Northstar/Northstar/v{latest}/Northstar.release.v{latest}.zip")
    print("Grab successful!")
  else:
    print("Grabbing NS v{latest}...")
    os.system(f"cd ~/Downloads; curl https://www.github.com/R2Northstar/Northstar/v{version}/Northstar.release.v{version}.zip")
    print("Grab successful!")
print("Ronin - The CLI for Northstar - v1.2.0")
print("What would you like to do?")
print("1. Grab and Install\n2. Grab\n0. Exit")
