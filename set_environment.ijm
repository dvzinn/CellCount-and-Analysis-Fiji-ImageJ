// SET ENVIRONMENT
// Daniëlla Zinn <daniellazinn@hotmail.nl>
// April 2023 

// This macro sets the environment that can be used for counting analysis of pictures. 
// The picture, Multipoint Tool, Results and ROI-manager will be opened when running this macro. 
// Then you can select the ROI and place points on the image.
// After activating this macro again, the picture with all points and ROI's will be saved, as well as the data of the points.

// This macro can be activated by installing it as a hotkey for easier use. 
// This can be done by putting the file inside the Fiji.app > plugins folder.
// Then, you can make the shortcut by going to Fiji: Plugins > Shortcuts > Add Shortcut...
// Choose a shortcut (for example F1) and look for the name of this script (set filename) in the list.

// Before starting, change the three folders to the ones you will use. This is the only part that should be personalised.


// change the folders with your own. Make sure to use these "/" instead of "\" in the folder path.
// folder with all pictures that should be analysed:
do_folder = "C:/Users/Danie/Documents/Internship/Counting/ToDo/"
// make sure that the pictures in this folder are not within maps and already stacked if needed.

// folder for saving the analysed images (pictures that are both in this folder and in the do_folder won't be analysed again):
done_folder = "C:/Users/Danie/Documents/Internship/Counting/Done/" 

// folder for saving the multipoint data:
measurements_folder = "C:/Users/Danie/Documents/Internship/Counting/Measurements/"


// first, if there is an image already opened, save the current file in the right place, save the data and close it
if (endsWith(File.name, ".tif")) {
	// clear Results workspace to be certain that only the relevant points are measured
	run("Clear Results");
	
	// measure multipoints (same as ctrl + m)
	run("Measure");

	// save these results to disk appropriately (the name that will be saved is the same as the name from the opened image) 
	saveAs("Tiff", done_folder + File.name); // folder for saving the analysed images
	saveAs("Results", measurements_folder + replace(File.name, ".tif", ".csv")); 
	// folder for saving the multipoint data

	// clear the working space
	run("Clear Results");
	roiManager("Reset");
	
	// close all windows so they van be re-opened for the next run
	run("Close");
}

dofolder = getFileList(do_folder); // folder with all pictures that should be analysed
donefolder = getFileList(done_folder); // folder with pictures that have been analysed (again)

j = 0;
i = 0;
found = true;

// i represents the index of some file in the "do folder"
// j represents the index of some file in the "done folder"
// we go through the do folder to find an occurence of the current file in the "done folder"
// (i.e. donefolder[j] == dofolder[i] at any point)
//
// if we *find* such an occurrence, we stop looking, so j never gets to the end of the list
// (i.e. j < donefolder.length)
// however, if we do not find such an occurrence (so the current file is not in the done folder)
// we have to keep looking all the way to the end, so j gets to be equal to donefolder.length
//
// in short: j < donefolder.length if the current file *is* done, and
//           j = donefolder.length if the current file *is not* done
//
// in this first loop, we loop as long as j != donefolder.length, i.e. we loop until we have
// found a file that is not done
while (found && i < dofolder.length) {
	file = dofolder[i];
	
	j = 0;
	found = false;
	while (!found && j < donefolder.length) {
		if (file == donefolder[j]) {
			found = true;
		}
		
		j++;
	}	
	
	i++;
}

if (!(endsWith(File.name, ".tif") || endsWith(File.name, ".csv"))) {
	doCommand("Point Tool..."); //setTool("multipoint");
}

// at this point, the while loop finished. this means that either j == donefolder.length
// (yay! we found a file that is not done yet!)
// or it means that i >= dofolder.length
// (YAAAY! we didn't find any not-done files, so we are completely finished!)
// in this case, either we will open a new not-yet-done file,
// or the last done file in the list
open(do_folder + file); // folder with all the pictures that should be analysed (again)

// Set environment for selecting area and cell counting
run("ROI Manager..."); // analyze tool ROI Manager
roiManager("Show All");
roiManager("Show All with labels"); // prefered settings
Table.deleteRows(0, 0); // clear the results for next round

