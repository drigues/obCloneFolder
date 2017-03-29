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
# App_Themes = os.listdir("ob/App_Themes")
# Images = os.listdir("ob/Images/Custom")
# Stylesheets = os.listdir("ob/Stylesheets")
# App_ThemesFolder = "ob/App_Themes"
# ImagesFolder = "ob/Images/Custom"
# StylesheetsFolder = "ob/Stylesheets"
# tempFolder = "ob/temp"
App_Themes = os.listdir("C:/Thiago/Web/CUOnlineBanking-Prod/CUOnlineBanking/App_Themes")
Images = os.listdir("C:/Thiago/Web/CUOnlineBanking-Prod/CUOnlineBanking/Images/Custom")
Stylesheets = os.listdir("C:/Thiago/Web/CUOnlineBanking-Prod/CUOnlineBanking/Stylesheets")
App_ThemesFolder = "C:/Thiago/Web/CUOnlineBanking-Prod/CUOnlineBanking/App_Themes"
ImagesFolder = "C:/Thiago/Web/CUOnlineBanking-Prod/CUOnlineBanking/Images/Custom"
StylesheetsFolder = "C:/Thiago/Web/CUOnlineBanking-Prod/CUOnlineBanking/Stylesheets"
tempFolder = "C:/Thiago/Web/CUOnlineBanking-Prod/CUOnlineBanking/temp"

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

    # Selecting the folde to copy
    setSkinName.copySkin = raw_input("| Copy SKIN folder from? ")
    if setSkinName.copySkin == "exit":
        return
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
    # copyImages = "ob/Images/Custom/"+setSkinName.copySkin
    # newSkinImages = "ob/Images/Custom/"+setSkinName.newSkin

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
    # copyFolder = "ob/App_Themes"+setSkinName.copySkin
    # newSkinFolder = "ob/App_Themes"+setSkinName.newSkin

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
    sys.exit()
    # setSkinStyle()
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
    print "| --------------------------------------------- |"
    print "| ------- Online Banking CSS STYLE EDIT ------- |"
    print "| --------------------------------------------- |"
    # List all the OB skin
    for obFolder1 in App_Themes:
        print "| - "+obFolder
    print "| --------------------------------------------- |"

    # Selecting the folde to copy
    setSkinStyle.copySkin = raw_input("| Which OB SKIN do you want to EDIT the CSS? ")
    if not setSkinStyle.copySkin in App_Themes:
        print "| SKIN NAME - "+ setSkinStyle.copySkin +" - IS NOT ON THE LIST!"
        print "| Please try again..."
        setSkinStyle()
    print "| --------------------------------------------- |"
    print "| - CSS STYLE FROM: "+setSkinStyle.copySkin
    print "| --------------------------------------------- |"

    # Setting the name of the new OB skin
    setSkinStyle.mainMenuColor = raw_input("| Type the MENU MAIN color (eg. #a1b2b3): ")
    setSkinStyle.mainHoverColor = raw_input("| Type the MENU HOVER color (eg. #a1b2b3): ")
    setSkinStyle.mainSelectColor = raw_input("| Type the MENU SELECT color (eg. #a1b2b3): ")
    print "| --------------------------------------------- |"
    print "| CSS STYLE FROM: "+setSkinStyle.copySkin
    print "| MENU MAIN COLOR: "+setSkinStyle.mainMenuColor
    print "| MENU HOVER: "+setSkinStyle.mainHoverColor
    print "| MENU SELECT: "+setSkinStyle.mainSelectColor
    print "| --------------------------------------------- |"
    print "| "

    # /** NEW STYLE OB SKIN **/
    # body {
    #     border-top:15px solid #69aa2a;
    # }
    # .MenuPanel li {
    #     background: #337dbc;
    # }
    # .MenuPanel li:hover { background-color: #185990; }
    # .MenuPanel a.menuItemSelected { background: #003b71; }
    # .MenuPanel .LogoutButtonPanel a:hover { color: #69aa2a; }
    # /* grid*/
    # .RadGrid_Castlecomer .rgDetailTable.BudgetItemsBalance .rgHeader { background:#69aa2a; }
    # /*
    # .MenuPanel .logoutButton:hover { border: 2px solid #69aa2a !important;}
    # .MenuPanel .logoutButton:hover {background: url(../Images/Custom/Castlecomer/logout_btnB.jpg) no-repeat scroll right top rgba(0, 0, 0, 0); border: 2px solid #69aa2a !important; height: 34px; margin-top: 10px; padding: 0; width: 243px;}
    # .MenuPanel .LogoutButtonPanel a {background: none; color: #2e3c56; display: block; font-weight: bold; padding-bottom: 3px; padding-left: 10px; padding-top: 3px; text-shadow: 1px 1px 1px #FFFFFF; text-align: left; line-height: 28px;}
    # */
    # .footerPanel {
    #     background: #f1f1f1;
    #     border-bottom: 15px solid #003b71;
    # }
    # .footerMenuPanel li a {
    #     color:#333;
    # }
    # .footerMenuPanel li a:hover {
    #     color:#000;
    #     text-decoration:underline;
    # }

    print "| NEW OB BANKING SKIN IS ALL DONE!"
    print "| Now you must to change the logo.svg on the images folder."
    print "| "
    sys.exit()
    return

# SOFTWARE ROOT - Main Function
setSkinName()
