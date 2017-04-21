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

## Steps

### Choose Project Environment
For this project I will use Python to perform the convertion of Java to UML:
* Using PyCharm IDE
* Python 3.6
* Anaconda 3
* JavaParser from javaparser.org
* UMLGraph

### Test Java Parser
- Installed JavaParser and Java Symbol Solver using Gradle and Maven
- Read the documentation trying to understand how it's usage apply to the project

### Test UML Parser
- Downloaded and installed UMLGraph.  The location in the project definition had an error; the correct link is [UMLGraph](https://www.spinellis.gr/umlgraph/)
### Integrate Java Parser and UML Parser

### Research
* yuml: is a tool written in python to create UML following a simple format.  Code can be found at the github
repo at [yUML](https://github.com/wandernauta/yuml)
* UMLGraph: is a tool written in JAVA for creating UML out of java files.  The java files need to be decorated with
"javadoc" tags to provide additional information for correct drawing of diagrams.
**[UMLGraph](https://www.spinellis.gr/umlgraph/)
**[Github Repo for UMLGraph](https://github.com/dspinellis/UMLGraph)

### Updates
* Decided on UMLGraph and JavaParser
* Installing and Updating system to support these two programs

### Template System
* Research on templates systems to help in structuring code that is going to be passed to the UMLGraph.
  * [pystache](https://github.com/defunkt/pystache): is Mustache library adapted python.  It can help
    create a file with the structure of the java code in the right format.  Code Example:
    ```
    print pystache.render('Hi {{person}}!', {'person': 'Mom'})
    Hi Mom!
    ```
### Python Parsers
Experimenting with a simpler python parser.  The java parser used are too complex for what we are trying to achieve.  I tried the plyj parser
which takes a file and returns a java tree.  Initial test showed to be simple to use for class diagrams.

* Added os.walk to get all files in directory and perform the parsing.
* Once the files are parsed the function return an array of parsed trees
* Next:  Set relations in the format of the UML generator.

### Running the Class Diagram Generator from Command Line
 * Need to be in the directory where the plantuml.jar file is located and execute the following command:
```
java -jar plantuml.jar class.txt
```
 * Alternatively the python script will execute the java jar file using a subprocess call:
 ```
 subprocess.call(['java', '-jar', 'plantuml.jar', 'Output.txt'])
 ```



