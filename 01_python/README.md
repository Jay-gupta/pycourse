# Setting up virtual environment

## Rationale

A single developer will typically work on more than one projects.  Each project has set of external dependencies.  Additionally, the developer account may not have privileges to install packages at the system level.

Creating a virtual environment for each project installs the correct version of the correct dependencies are installed 'locally', or at the project environment level.  The dependencies of one project will not conflict with the dependencies of other projects.

Each project is in its own folder, and the virtual environment is created in that folder.

    |
    |-- trafficam
    |   |-- venv
    |
    |-- dataspy
    |   |-- venv
    |
    |-- autosub
    |   |-- venv


The tree above could be created like this:

>md trafficam
>cd trafficam
>python -m venv venv
>cd ..
>md dataspy
>cd dataspy
>python -m venv venv
>cd ..
>md autosub
>cd autosub
>python -m venv venv

now depending on which project you want to work on you can go into that folder and activate that virtual environment.

>cd dataspy
>venv\Scripts\activate
(venv) >

when you switch to another project, you must activate that projects virtual environment.  to deactivate a virtual environment:

(venv) >deactivate
>

once you have activated a project virtual environment, you can install any external dependencies you need for that project.

(venv) >pip install numpy

