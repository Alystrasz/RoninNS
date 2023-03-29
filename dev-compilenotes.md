# Developer Compile Notes
## 1 - Prepare directories
- Create a directory named `RoninNS`.
- Inside the directory, create two subdirectories: `DEBIAN` and `bin`.
- Inside `DEBIAN`, make a file called `control`. Configure it with the package settings.
- Inside `bin`, make a final subdirectory called `ronin`. Inside it, paste all the code.
## 2 - Prepare terminal
- Open Terminal.
- Run `cd ~/Desktop/; sudo dpkg --build ./RoninNS ./RoninNS-v1.10.deb`.
- Make sure that the Debian package is in the Desktop.
## 3 - Upload to GitHub
## 4 - Add GitHub repo to system package cache
