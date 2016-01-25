# core-serval
Various configs and script for testing serval in core-network.

More information about adding serval to core-network can be found in the following blog article: http://otg-living.blogspot.de/2016/01/running-serval-in-core-network-simulator.html

## Installation
Copy/merge the conf files from dotcore to your ~/.core directory. Copy over the serval.py file into your myservices folder, modify the init file to load the serval file or copy the version from this repo if you haven't got any other custom services installed. Edit /etc/core/core.conf to add the local plugin directory.

Change the installation path of servald in the widgets.conf and serval.py depending on where your servald is installed and the runtime directory. No support for instancepath at the moment. Servald was compiled with --prefix=/home/meshadmin/serval-conf

For some widgets external scripts are used. These can be found here: https://github.com/gh0st42/serval-tests

## Usage
There are 2 new node types: one a basic pc only with servald running and one with standard olsr for mesh support.

Several widgets are available to quickly inspect the running nodes.
