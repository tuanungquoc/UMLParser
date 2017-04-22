[![Stories in Ready](https://badge.waffle.io/carlo379/UMLParser.png?label=ready&title=Ready)](http://waffle.io/carlo379/UMLParser)
# UML Parser
#### By Carlos Martinez

## Description
In this project we will create a Parser to convert Java to UML (Class Diagram).  We will use Agile (Kanban board) to manage all
User Stories or Task and produce weekly reports.

## Requirements
* The parser must be a command line application following this format:
```
umlparser <source folder> <output file name>
```

## Project Tracking
* Waffle IO
* Github / Github Issues

## Dependencies
 * First you need to install the following dependencies:
   1. Python 3.5 +: [https://www.python.org/downloads/source/](https://www.python.org/downloads/source/)
     Will depend on operating system. Check link
   2. Javalang
   ```
    pip install javalang
   ```
   3. Argparse
   ```
   pip install argparse
   ```
   4. Java 1.8+:  Follow these [Instructions: https://www.java.com/en/download/help/download_options.xml](https://www.java.com/en/download/help/download_options.xml)

   5. GraphViz: Download installer from [GraphVix website: http://www.graphviz.org/Download..php](http://www.graphviz.org/Download..php) and run file to install.  Test Installation with:
   ```
   java -jar plantuml.jar -testdot
   ```
 * To Run the application use the following commands on the terminal:
   1. usage: 'python3 umlparser.py <source folder>'
   ```
   python3 /Relative/Path/To/UMLParser/umlparser.py /Relative/Path/To/TestCase/SourceFiles/Directory
   ```
     i. Example:
     ```
     python3 Projects/cmpe202/UMLParser/umlparser.py -s Projects/cmpe202/UMLParser/SourceFiles/uml-parser-test-1
     ```
   The output image file ('Output.png') will be rendered in the directory of the project.




