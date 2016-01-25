# core-serval
Various configs and script for testing serval in core-network

## Installation
Copy/merge the conf files from dotcore to your ~/.core directory. Copy over the serval.py file into your myservices folder, modify the init file to load the serval file or copy the version from this repo if you haven't got any other custom services installed. Edit /etc/core/core.conf to add the local plugin directory.

Change the installation path of servald in the widgets.conf and serval.py depending on where your servald is installed and the runtime directory. No support for instancepath at the moment. Servald was compiled with --prefix=/home/meshadmin/servald-conf

## Usage
There are 2 new node types: one a basic pc only with servald running and one with standard olsr for mesh support.

Several widgets are available to quickly inspect the running nodes.
