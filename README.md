# obCloneFolder

A Python software to support the Online Baking development at Progress Systems.
During that development is required to copy a list of folders and files to be used as a template for a new Online Banking Skin.
Using this software, we reduce the manual job and turns much faster and consistent the production.

## Tasks

#### List and Select

Listing the folders on the root, selecting the a skin that will copied to create a new skin.

    setSkinName()

#### Coping folders and files

After the confirmation, copying all the listed folders and files from App_Themes, Images and Stylesheets folders.

    createNewSkin()

#### Renaming and Opening files

Listing the files that must to be renamed, opening, finding and replacing to the new online banking skin.

    changeSkinName()

#### Duplicate and Renaming file

Using a temp folder to duplicate and rename a file based on the new OB skin.

    changeCSSFile()

#### Searching and Replacing

Open a file, searching for the word to be replaced and saving with the new name.

    repSkinNameFile()

#### Inserting data to the file

Updating the style file with an editable CSS to speed up the production of the new skin.

    setSkinStyle()


##

More about me at [drigues.com][drigues-com-url]


[drigues-com-url]: http://drigues.com
