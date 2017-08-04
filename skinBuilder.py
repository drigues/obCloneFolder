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
# To list the User Temp Folder
import tempfile

# SETTING THE ROOT DIRECTORIES
pathFileFolder = os.path.abspath("..")

App_ThemesFolder = os.path.join(pathFileFolder, "App_Themes")
ImagesFolder = os.path.join(pathFileFolder, "Images\Custom")
StylesheetsFolder = os.path.join(pathFileFolder, "Stylesheets")
tempFolder = tempfile.gettempdir()

App_Themes = os.listdir(App_ThemesFolder)
Images = os.listdir(ImagesFolder)
Stylesheets = os.listdir(StylesheetsFolder)

print "| ------------------------------------- |"
print "| ---- ONLINE BANKING SKIN BUILDER ---- |"
print "| ------------------------------------- |"
print "| - " + App_ThemesFolder
print "| - " + ImagesFolder
print "| - " + StylesheetsFolder
print "| - " + tempFolder


# # # # # # # # # # # # # # # # # # # # # # # # #
# # # #    LIST / SET NEW OB SKIN NAME    # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #
def setSkinName():
    # Selecting the TEMPLATE SKIN to copy
    setSkinName.copySkin = "BaseSkinTemplate"
    print "| ------------------------------------- |"
    print "| - SKIN BASE: " + setSkinName.copySkin
    print "| ------------------------------------- |"

    # Setting the name of the new OB skin
    setSkinName.newSkin = raw_input("| - Name of the NEW OB SKIN? ")

    if setSkinName.newSkin == "exit":
        print "/// exit"
        sys.exit()

    if setSkinName.copySkin == "" or setSkinName.copySkin == " ":
        print "| INVALID OB SKIN NAME"
        print "| Please try again..."
        print "| ------------------------------------- |"
        setSkinName()

    if setSkinName.newSkin in App_Themes:
        print "|"
        print "| " + setSkinName.newSkin + " - ALREADY EXIST ON THE LIST!"
        print "| Do you wish to OVERWRITE all the current files of " + setSkinName.newSkin + "?"
        confCopy = input("| 1 - YES / 0 - NO? " )
        print "|"
        if confCopy == 1:
            deleteOldSkin(setSkinName.copySkin, setSkinName.newSkin)
        else:
            print "/// exit"
            sys.exit()
        return

    print "| ------------------------------------- |"
    print "| - NEW SKIN: " + setSkinName.newSkin
    print "| ------------------------------------- |"
    print "| Do you confirm to copy the SKIN folder from " + setSkinName.copySkin + " to " + setSkinName.newSkin + "?"
    confCopy = input("| 1 - YES / 0 - NO? ")
    print "|"
    if confCopy == 1:
        createNewSkin(setSkinName.copySkin, setSkinName.newSkin)
    else:
        print "/// exit"
        sys.exit()
    return


# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # #    DELETE OLD OB SKIN   # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #
def deleteOldSkin(copySkin, newSkin):
    print "| ------------------------------------- |"
    print "| - DELETING the old skin: " + setSkinName.newSkin
    print "| ------------------------------------- |"

    # CSS File
    cssFolder = StylesheetsFolder+"/"
    listCSS = os.walk(cssFolder).next()[2]
    for obCSS in listCSS:
        if setSkinName.newSkin in obCSS:
            oldObCss = cssFolder+obCSS
            print "| - " + oldObCss
            os.remove(oldObCss)

    # IMG Folder
    newSkinImages = ImagesFolder+"/"+setSkinName.newSkin
    print "| - " + newSkinImages
    shutil.rmtree(newSkinImages)

    #APP_THEMES Folder
    newSkinFolder = App_ThemesFolder+"/"+setSkinName.newSkin
    print "| - " + newSkinFolder
    shutil.rmtree(newSkinFolder)

    print "|"
    createNewSkin(setSkinName.copySkin, setSkinName.newSkin)


# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # #    CREATE NEW OB SKIN   # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #
def createNewSkin(copySkin, newSkin):
    print "| ------------------------------------- |"
    print "| - Copying from " + setSkinName.copySkin + " to " + setSkinName.newSkin
    print "| ------------------------------------- |"

    # # # STYLESHEETS FOLDER
    cssFolder = StylesheetsFolder + "\\"
    print "| + Stylesheets"
    # Changing SKIN NAME APP THEMES in the FOLDER
    changeCSSFile(cssFolder, setSkinName.copySkin, setSkinName.newSkin)

    # # # CUSTOM IMG FOLDER
    copyImages = ImagesFolder + "\\" + setSkinName.copySkin
    newSkinImages = ImagesFolder + "\\" + setSkinName.newSkin

    print "| + Images/Custom"
    # Creating the NEW IMAGES SKIN FOLDER
    if not os.path.exists(newSkinImages):
        os.makedirs(newSkinImages)
        print "  | + " + newSkinImages

    # list and copy IMAGES files
    listIMGS = os.walk(copyImages).next()[2]
    for obImg in listIMGS:
        newCopyImg = copyImages + "\\" + obImg
        shutil.copy2(newCopyImg, newSkinImages)
        print "    | - " + obImg

    # # # APP THEMES FOLDER
    copyFolder = App_ThemesFolder + "\\" + setSkinName.copySkin
    newSkinFolder = App_ThemesFolder + "\\" + setSkinName.newSkin

    # Creating the NEW MAIN SKIN FOLDER
    if not os.path.exists(newSkinFolder):
        os.makedirs(newSkinFolder)

    # List FOLDERS in the root
    listFolders = os.walk(copyFolder).next()[1]
    print "| + App_Themes/"
    for obFolder in listFolders:
        newFolderTree = newSkinFolder + "\\" + obFolder
        print "  | + " + newFolderTree

        # Creating the NEW SKIN FOLDER TREE
        if not os.path.exists(newFolderTree):
            os.makedirs(newFolderTree)

        obFolderTree = copyFolder + "\\" + obFolder
        copyAllFiles = os.walk(obFolderTree).next()[2]
        for copyFile2NewFolder in copyAllFiles:
            copyFile2Foler = newFolderTree + "\\" + copyFile2NewFolder
            fileFolderTree = obFolderTree + "\\" + copyFile2NewFolder
            shutil.copy2(fileFolderTree, copyFile2Foler)
            print "    | - " + copyFile2NewFolder

    # list and copy files
    listFiles = os.walk(copyFolder).next()[2]
    for obFile in listFiles:
        newCopyFile = copyFolder + "\\" + obFile
        shutil.copy2(newCopyFile, newSkinFolder)

    # Changing SKIN NAME APP THEMES in the FOLDER
    changeSkinName(newSkinFolder, setSkinName.copySkin, setSkinName.newSkin)

    print "| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |"
    print "| "
    print "| NEW OB SKIN: " + setSkinName.newSkin + " has been created"
    print "| "
    print "| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |"
    # sys.exit()
    setSkinStyle()
    return


# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # #    OPEN AND RENAME THE FILE     # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #
def changeSkinName(newSkinFolder, copySkin, newSkin):
    newListFiles = os.walk(newSkinFolder).next()[2]
    # Renaming the SKIN FILE
    for obFile in newListFiles:
        newObFile = obFile.replace(setSkinName.copySkin, setSkinName.newSkin, 1)
        for filename in os.listdir(newSkinFolder):
            oldNameFile = newSkinFolder + "\\" + obFile
            newNameFile = newSkinFolder + "\\" + newObFile
        os.rename(oldNameFile, newNameFile)
        # Replacing into the file the SKIN NAME
        repSkinNameFile(newNameFile, newSkinFolder, copySkin, newSkin)
        print "| - " + newObFile
    return


# # # # # # # # # # # # # # # # # # # # # # # # #
# # # #   COPY AND RENAME THE CSS FILE    # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #
def changeCSSFile(cssFolder, copySkin, newSkin):
    listCSS = os.walk(cssFolder).next()[2]
    temp = tempFolder
    for obCSS in listCSS:
        copyOldCSS = cssFolder + "\\" + obCSS
        if setSkinName.copySkin in obCSS:
            try:
                shutil.copy2(copyOldCSS, temp)
            except IOError, e:
                print "Unable to copy file. %s" % e

    listTemp = os.walk(temp).next()[2]
    for obTemp in os.listdir(temp):
        if setSkinName.copySkin in obTemp:
            oldCSSFile = temp + "\\" + obTemp
            newObTemp = obTemp.replace(setSkinName.copySkin, setSkinName.newSkin, 1)
            newCSSFile = temp + "\\" + newObTemp
            print "  | - " + newObTemp

    os.rename(oldCSSFile, newCSSFile)
    shutil.move(newCSSFile, cssFolder)
    newCSSPlaced = cssFolder + "\\" + newObTemp

    # Replacing into the file the SKIN NAME
    repSkinNameFile(newCSSPlaced, cssFolder, copySkin, newSkin)
    return


# # # # # # # # # # # # # # # # # # # # # # # # #
# #     REPLACE THE OB SKIN INTO THE FILE     # #
# # # # # # # # # # # # # # # # # # # # # # # # #
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


# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # #    OB SKIN CSS EDITOR     # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # #
def setSkinStyle():
    # listing the folder again to refresh the new skin created
    App_Themes = os.listdir(App_ThemesFolder)
    print "|"
    print "| -------------------------------------------------- |"
    print "| ------------ OB SKIN CSS STYLE EDITOR ------------ |"
    print "| -------------------------------------------------- |"
    # List all the OB skin
    for obFolderStyle in App_Themes:
        print "| - " + obFolderStyle
    print "| -------------------------------------------------- |"

    # Selecting the folder to EDIT the style
    setSkinStyle.copySkin = raw_input("| Choose the OB SKIN to EDIT the CSS? ")

    if setSkinStyle.copySkin == "exit":
        print "/// exit"
        sys.exit()

    if setSkinStyle.copySkin == "" or setSkinStyle.copySkin == " ":
        print "| INVALID OB SKIN NAME"
        print "| Please try again..."
        print "| -------------------------------------------------- |"
        setSkinStyle()

    if not setSkinStyle.copySkin in App_Themes:
        print "| THE OB SKIN: " + setSkinStyle.copySkin + " - IS NOT ON THE LIST!"
        print "| Please try again..."
        print "| -------------------------------------------------- |"
        setSkinStyle()

    print "| -------------------------------------------------- |"
    print "| - CSS STYLE FROM: " + setSkinStyle.copySkin
    print "| -------------------------------------------------- |"

    # Setting the COLORS of the new OB skin
    setSkinStyle.mainMenuColor = raw_input("| Type the MENU MAIN color (eg. a1b2b3): ")
    setSkinStyle.mainHoverColor = raw_input("| Type the MENU HOVER color (eg. a1b2b3): ")
    setSkinStyle.mainSelectColor = raw_input("| Type the MENU SELECT color (eg. a1b2b3): ")

    cssBlock = '''

/* -------------- STANDARD STYLE DONE BY PYTHON --------------- */

/* MENU, BACKGROUND and BORDERS COLORS */
/*Main - 1*/
body { border-top:15px solid #''' + setSkinStyle.mainMenuColor + '''; }
.MenuPanel li { background: #''' + setSkinStyle.mainMenuColor + '''; }
/*Hover - 2*/
.MenuPanel li:hover { background-color: #''' + setSkinStyle.mainHoverColor + '''; }
.RadGrid_''' + setSkinStyle.copySkin + ''' .rgHeader, .RadGrid_''' + setSkinStyle.copySkin + ''' th.rgResizeCol, .fixedTableHeader { background: #''' + setSkinStyle.mainHoverColor + ''' !important; } /*main grid*/
.MenuPanel .LogoutButtonPanel a { background-color: #''' + setSkinStyle.mainHoverColor + ''' !important; border: 2px solid #''' + setSkinStyle.mainHoverColor +''' !important;}
/*Select - 3*/
.MenuPanel a.menuItemSelected { background: #''' + setSkinStyle.mainSelectColor + '''; }
.MenuPanel .LogoutButtonPanel a:hover { background-color: #''' + setSkinStyle.mainSelectColor + ''' !important; border: 2px solid #''' + setSkinStyle.mainSelectColor + ''' !important; }
.footerPanel a:hover { color: #''' + setSkinStyle.mainSelectColor + ''';}
.sectionHeader { background: #''' + setSkinStyle.mainSelectColor + ''';} /*header subscription services*/
.sectionContent { border-top: 2px solid #''' + setSkinStyle.mainSelectColor + '''; }'''

    listCssFiles = os.walk(StylesheetsFolder).next()[2]
    for editCssFile in listCssFiles:
        if setSkinStyle.copySkin in editCssFile:
            fileCss = StylesheetsFolder + "\\" + editCssFile
            with open(fileCss, "r+") as myfile:
                text = myfile.read()
                myfile.seek(0)
                myfile.write(text)
                myfile.write(cssBlock)
                myfile.truncate()
                myfile.close()

    print "| ------------------------------------------------------- |"
    print "| "
    print "| The stylesheet has been updated on " + fileCss
    print "| "
    print "| MENU MAIN COLOR: " + setSkinStyle.mainMenuColor
    print "| MENU HOVER: " + setSkinStyle.mainHoverColor
    print "| MENU SELECT: " + setSkinStyle.mainSelectColor
    print "| "
    print "| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |"
    print "| "
    print "| NEW OB BANKING SKIN IS ALL DONE!"
    print "| Now, you must to change the LOGO.SGV at Images/Custom/" + setSkinStyle.copySkin
    print "| "
    print "| ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |"

    sys.exit()
    return

# SOFTWARE ROOT - Main Function
setSkinName()
