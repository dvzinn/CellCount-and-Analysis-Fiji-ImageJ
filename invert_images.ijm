// INVERT IMAGES
// Daniëlla Zinn <daniellazinn@hotmail.nl>
// April 2023 

// Save pictures in subfolders as stacks and inverted colours in a new map.
// You will have to change four folders: three times the folder in which the original pictures are (they should be in folders, all pictures 
// inside the folders will be stacked together).
// The last folder is the folder in which you want your stacked pictures to be. If you want to use this script before using the set_environment 
// script, this can be the "dofolder".

// Only these two variables have to be altered:
mainfolder = "C:/Users/Danie/Documents/Internship/DG_blackwhite_nonfiltered/" // overarching folder in which the different folders with pictures are
stacks_savingfolder = "C:/Users/Danie/Documents/Internship/Counting/Stacks/" // folder in which all inverted and stacked pictures will be saved

folders = getFileList(mainfolder); // open folder in which all the subfolders reside
for (i = 0; i < folders.length; i++) // starting from 0, go through the amount of existing folders
{
	folder = folders[i];
	files = getFileList(mainfolder + folder); 
	
	for (j = 0; j < files.length; j++) // starting from 0, go through the amount of exsting subfolders inside the folder
	{
		file = files[j];
		File.openSequence(mainfolder + folder + file); 
		run("Invert", "stack"); // the intended alterations, in this case inverting and stacking the images inside the folder
		saveAs("Tiff", stacks_savingfolder + file.substring(0, file.length - 1) + ".tif"); 
		// save images, "file.substring()" is added since the file has a slash because it is technically a folder, you want to delete the slash
		close();
	}
}



