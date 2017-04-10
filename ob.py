# To work with diretories
import os
import shutil
# To get command from keyboard
import fileinput
# To overwrite the file content
import re
# To stop the flow
import sys
# To list files and folder from the root
from os import listdir, walk
from os.path import isfile, join

## DIRECTORY Root of all the ONLINE BANKING SKIN
App_Themes = os.listdir("ob/App_Themes")
Images = os.listdir("ob/Images/Custom")
Stylesheets = os.listdir("ob/Stylesheets")
App_ThemesFolder = "ob/App_Themes"
ImagesFolder = "ob/Images/Custom"
StylesheetsFolder = "ob/Stylesheets"
tempFolder = "ob/temp"


# LIST / SELECT / SETUP the new OB Skin
def setSkinName():
    print ""
    print "| ------------------------------------- |"
    print "| ---- LIST OF ONLINE BANKING SKIN ---- |"
    print "| ------------------------------------- |"
    # List all the OB skin
    for obFolder in App_Themes:
        print "| - "+obFolder
    print "| ------------------------------------- |"

    # Selecting the folder to copy
    setSkinName.copySkin = raw_input("| Copy SKIN folder from? ")
    if setSkinName.copySkin == "exit":
        sys.exit()
    if not setSkinName.copySkin in App_Themes:
        print "| SKIN NAME - "+ setSkinName.copySkin +" - IS NOT ON THE LIST!"
        print "| Please try again..."
        setSkinName()
    print "| ------------------------------------- |"
    print "| - SKIN BASE: "+setSkinName.copySkin
    print "| ------------------------------------- |"

    # Setting the name of the new OB skin
    setSkinName.newSkin = raw_input("| Name of the NEW OB SKIN? ")
    print "| ------------------------------------- |"
    print "| - NEW SKIN: "+setSkinName.newSkin
    print "| ------------------------------------- |"
    confimCopySkin(setSkinName.copySkin, setSkinName.newSkin)
    return

# CONFIMATION to COPY the skin
def confimCopySkin(copySkin, newSkin):
    print "| Do you confirm to copy the SKIN folder from "+setSkinName.copySkin+" to "+setSkinName.newSkin+"?"
    confCopy = input("| 1 - YES / 0 - NO? " )
    print ""
    if confCopy == 1:
        createNewSkin(setSkinName.copySkin, setSkinName.newSkin)
    else:
        #setSkinName()
        print "bye.."
    return

# COPY foldes and files to the NEW SKIN
def createNewSkin(copySkin, newSkin):
    print "| ------------------------------------- |"
    print "| - Copying from "+setSkinName.copySkin+" to "+setSkinName.newSkin
    print "| ------------------------------------- |"

    ### STYLESHEETS
    cssFolder = StylesheetsFolder+"/"
    #cssFolder = "ob/Stylesheets/"
    print "| + Stylesheets"
    # Changing SKIN NAME APP THEMES in the FOLDER
    changeCSSFile(cssFolder, setSkinName.copySkin, setSkinName.newSkin)

    ### CUSTOM IMG
    copyImages = ImagesFolder+"/"+setSkinName.copySkin
    newSkinImages = ImagesFolder+"/"+setSkinName.newSkin

    print "| + Images/Custom"
    # Creating the NEW IMAGES SKIN FOLDER
    if not os.path.exists(newSkinImages):
        os.makedirs(newSkinImages)
        print "  | + "+newSkinImages

    # list and copy IMAGES files
    listIMGS = os.walk(copyImages).next()[2]
    for obImg in listIMGS:
        newCopyImg = copyImages+"/"+obImg
        shutil.copy2(newCopyImg, newSkinImages)
        print "    | - "+obImg

    ### APP THEMES
    copyFolder = App_ThemesFolder+"/"+setSkinName.copySkin
    newSkinFolder = App_ThemesFolder+"/"+setSkinName.newSkin

    # Creating the NEW MAIN SKIN FOLDER
    if not os.path.exists(newSkinFolder):
        os.makedirs(newSkinFolder)

    # List FOLDERS in the root
    listFolders = os.walk(copyFolder).next()[1]
    print "| + App_Themes/"
    for obFolder in listFolders:
        newFolderTree = newSkinFolder+"/"+obFolder
        print "  | + "+newFolderTree

        # Creating the NEW SKIN FOLDER TREE
        if not os.path.exists(newFolderTree):
            os.makedirs(newFolderTree)

        obFolderTree = copyFolder+"/"+obFolder
        copyAllFiles = os.walk(obFolderTree).next()[2]
        for copyFile2NewFolder in copyAllFiles:
            copyFile2Foler = newFolderTree+"/"+copyFile2NewFolder
            fileFolderTree = obFolderTree+"/"+copyFile2NewFolder
            shutil.copy2(fileFolderTree, copyFile2Foler)
            print "    | - "+copyFile2NewFolder

    # list and copy files
    listFiles = os.walk(copyFolder).next()[2]
    for obFile in listFiles:
        newCopyFile = copyFolder+"/"+obFile
        shutil.copy2(newCopyFile, newSkinFolder)

    # Changing SKIN NAME APP THEMES in the FOLDER
    changeSkinName(newSkinFolder, setSkinName.copySkin, setSkinName.newSkin)

    print "| --------------------------------------------------------- |"
    print "| - NEW Online Banking skin: "+setSkinName.newSkin+" created successfully!!"
    print "| --------------------------------------------------------- |"
    # sys.exit()
    setSkinStyle()
    return

# OPEN file and RENAME the SKIN
def changeSkinName(newSkinFolder, copySkin, newSkin):
    newListFiles = os.walk(newSkinFolder).next()[2]
    # Renaming the SKIN FILE
    for obFile in newListFiles:
        newObFile = obFile.replace(setSkinName.copySkin,setSkinName.newSkin,1)
        for filename in os.listdir(newSkinFolder):
            oldNameFile = newSkinFolder+"/"+obFile
            newNameFile = newSkinFolder+"/"+newObFile
        os.rename(oldNameFile, newNameFile)
        # Replacing into the file the SKIN NAME
        repSkinNameFile(newNameFile, newSkinFolder, copySkin, newSkin)
        print "| - "+newObFile
    return

# COPY AND RENAME a CSS file on the SAME FOLDER
def changeCSSFile(cssFolder, copySkin, newSkin):
    listCSS = os.walk(cssFolder).next()[2]
    temp = tempFolder
    for obCSS in listCSS:
        copyOldCSS = cssFolder+"/"+obCSS
        if setSkinName.copySkin in obCSS:
            shutil.copy2(copyOldCSS, temp)

    listTemp = os.walk(temp).next()[2]
    for obTemp in os.listdir(temp):
        if setSkinName.copySkin in obTemp:
            oldCSSFile = temp+"/"+obTemp
            newObTemp = obTemp.replace(setSkinName.copySkin,setSkinName.newSkin,1)
            newCSSFile = temp+"/"+newObTemp
        print "  | - "+newObTemp

    os.rename(oldCSSFile, newCSSFile)
    shutil.move(newCSSFile, cssFolder)
    newCSSPlaced = cssFolder+"/"+newObTemp

    # Replacing into the file the SKIN NAME
    repSkinNameFile(newCSSPlaced, cssFolder, copySkin, newSkin)
    return

# REPLACE INTO the file the SKIN NAME
def repSkinNameFile(newNameFile, newSkinFolder, copySkin, newSkin):
    newListFiles = os.walk(newSkinFolder).next()[2]
    for obFile in newListFiles:
        newObFile = obFile.replace(setSkinName.copySkin,setSkinName.newSkin,1)
        f = open(newNameFile, 'r+')
        text = f.read()
        text = re.sub(setSkinName.copySkin, setSkinName.newSkin, text)
        f.seek(0)
        f.write(text)
        f.truncate()
        f.close()
    return

# SELECT an OB SKIN to EDIT CSS STYLE
def setSkinStyle():
    # listing the folder again to refresh the new skin created
    App_Themes = os.listdir("ob/App_Themes")
    print ""
    print "| ------------------------------------------------------- |"
    print "| ------------ Online Banking CSS STYLE EDIT ------------ |"
    print "| ------------------------------------------------------- |"
    # List all the OB skin
    for obFolder1 in App_Themes:
        print "| - "+obFolder1
    print "| ------------------------------------------------------- |"

    # Selecting the folder to EDIT the style
    setSkinStyle.copySkin = raw_input("| Which OB SKIN do you want to EDIT the CSS? ")
    if setSkinStyle.copySkin == "exit":
        sys.exit()
    if not setSkinStyle.copySkin in App_Themes:
        print "| SKIN NAME - "+ setSkinStyle.copySkin +" - IS NOT ON THE LIST!"
        print "| Please try again..."
        setSkinStyle()
    print "| ------------------------------------------------------- |"
    print "| - CSS STYLE FROM: "+setSkinStyle.copySkin
    print "| ------------------------------------------------------- |"

    # Setting the COLORS of the new OB skin
    setSkinStyle.mainMenuColor = raw_input("| Type the MENU MAIN color (eg. #a1b2b3): ")
    setSkinStyle.mainHoverColor = raw_input("| Type the MENU HOVER color (eg. #a1b2b3): ")
    setSkinStyle.mainSelectColor = raw_input("| Type the MENU SELECT color (eg. #a1b2b3): ")

    cssBlock1 = "\n/* STYLE DONE BY PYTHON to update MENU, BACKGROUND and BORDERS COLORS */ \n/*1*/ \nbody { border-top:15px solid "+setSkinStyle.mainMenuColor+"; } \n.MenuPanel li { background: "+setSkinStyle.mainMenuColor+"; } \n.RadGrid_INTO .rgDetailTable .rgHeader { background: "+setSkinStyle.mainMenuColor+" !important; } /*transaction grid*/"
    cssBlock2 = "\n/*2*/ \n.MenuPanel li:hover { background-color: "+setSkinStyle.mainHoverColor+"; } \n.footerPanel a:hover { color: "+setSkinStyle.mainHoverColor+";} \n.RadGrid_INTO .rgHeader, .RadGrid_INTO th.rgResizeCol { background: "+setSkinStyle.mainHoverColor+" !important; } /*main grid*/ \n.MenuPanel .LogoutButtonPanel a { background-color: "+setSkinStyle.mainHoverColor+"; border: 3px solid "+setSkinStyle.mainHoverColor+" !important;}"
    cssBlock3 = "\n/*3*/ \n.MenuPanel a.menuItemSelected { background: "+setSkinStyle.mainSelectColor+"; } \n.MenuPanel .LogoutButtonPanel a:hover { background-color: "+setSkinStyle.mainSelectColor+"; border: 3px solid "+setSkinStyle.mainSelectColor+" !important; } \n.sectionHeader { background: "+setSkinStyle.mainSelectColor+";} \n.sectionContent { border-top: 2px solid "+setSkinStyle.mainSelectColor+"; }"

    listCssFiles = os.walk(StylesheetsFolder).next()[2]
    for editCssFile in listCssFiles:
        if setSkinStyle.copySkin in editCssFile:
            fileCss = StylesheetsFolder+"/"+editCssFile
            with open(fileCss, "r+") as myfile:
                text = myfile.read()
                myfile.seek(0)
                myfile.write(text)
                myfile.write(cssBlock1)
                myfile.write(cssBlock2)
                myfile.write(cssBlock3)
                myfile.truncate()
                myfile.close()

    print "| ------------------------------------------------------- |"
    print "| "
    print "| The stylesheet has been updated on "+fileCss
    print "| "
    print "| MENU MAIN COLOR: "+setSkinStyle.mainMenuColor
    print "| MENU HOVER: "+setSkinStyle.mainHoverColor
    print "| MENU SELECT: "+setSkinStyle.mainSelectColor
    print "| "
    print "| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |"
    print "| "
    print "| NEW OB BANKING SKIN IS ALL DONE!"
    print "| Now, you must to change the LOGO.SGV at Images/Custom/"+setSkinStyle.copySkin
    print "| "
    print "| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |"
    sys.exit()
    return

# SOFTWARE ROOT - Main Function
setSkinName()
#setSkinStyle()
