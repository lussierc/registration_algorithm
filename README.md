# cs202-s2019-project

## Group Members: Christian Lussier, Ben Watto, Mikey Spurr
"All work is our own unless otherwise cited."

### Brief Project Description
This project takes Allegheny College's current method of determining registration
letter groups and improves upon in a way many students seem to thing would be more
fair. This is done by the creation of a new algorithm. Please read the document
in the `Final Report` folder and related folders for more information.

### Running The Program
To run the Letter Group Organizer Algorithm and it's associated program, first
ensure you have Python3 installed.

Then navigate to the `SourceCode` folder of the project.

You can then run the following command to run the entire program:
```
python3 interface.py
```

### File Organization
This project contains a variety of folders. Their purposes are detailed below:
- `data` folder: Contains the sample input data in the folder called `input` and
a folder called `output` where users can choose to output their sorted students (by letter group)
results.
- `FINALReport` folder: Contains the Final Report Document for the project.
- `PresentationSlides` folder: Contains the associated Presentation Slides for the project.
- `ProgressReport` folder: Contains the Progress Report Document for the Project.
- `Proposal` folder: Contains the Project Proposal Document.
- `SourceCode` folder: Contains all of the SourceCode for the project.
  - `fileReader.py`: Reads in input files.
  - `interface.py`: The interface and "driver"/main file for the program.
    This is the file that should be used to run the program..
  - `organizer.py`: The Letter Group Organizer algorithm.
