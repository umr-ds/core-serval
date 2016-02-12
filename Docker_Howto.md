# Docker Howto

## Linux

Simply run:

```
# Install Docker
sudo apt-get install docker.io
# Allow the container by hostname to access X11
xhost +local:`sudo docker inspect --format='{{ ).Config.Hostname  }}' nachtmaar/nicer_core_emu:latest`
# Start the container
sudo docker run -it --rm --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix nachtmaar/nicer_core_emu:latest
````

This installs Docker and allows the Docker container to access the X11 server.

Note: The host name of the Docker container is allowed to access the X11 server. This might not be the safest way, but is way better to disable X11 Access Control List at all.
Check http://wiki.ros.org/docker/Tutorials/GUI for a better way if you really care.

## OS X

### Install XQuartz:


#### Via brew cask:

```
$ brew install cask
$ brew cask install xquartz
```

#### Manually

Download and install it from: http://www.xquartz.org

### Run the container

#### Install Docker

```
brew install socat
brew cask install Caskroom/cask/dockertoolbox
```

#### Prepare X11
Figure out the IP address of your VirtualBox network device.
For me it was `192.168.99.1`. Note that this is the IP address of Mac OS X, not the virtual machine where docker is running.

```
$ ifconfig
...
vboxnet1: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	ether 0a:00:27:00:00:01
	inet 192.168.99.1 netmask 0xffffff00 broadcast 192.168.99.255
```
Forward X11 connections from port 6000 to the X11 Unix Domain Socket. Bind only to the supplied IP address.

```
$ socat TCP-LISTEN:6000,reuseaddr,fork,bind=192.168.99.1,range=192.168.99.0/24 UNIX-CLIENT:\"$DISPLAY\"
```


Start Xquartz

```
open -a Xquartz
```

Check before that the display is set like this:

```
$ echo $DISPLAY
/private/tmp/com.apple.launchd.LLKyMpK06C/org.macosforge.xquartz:0
```

Otherwise relogin.

Afterwards run the container:

```
docker run -it --privileged --rm -e DISPLAY=192.168.99.1:0 nachtmaar/nicer_core_emu:latest
```

Note: If you want to right-click on the nodes in the canvas, you have to click with two fingers (real click, no touch).

## (Re)building

Use the command below to build the docker image by yourself. For example if you modified the `Dockerfile` or do not trust the hosted image.

```
cd docker
docker build -t nachtmaar/nicer_core_emu:latest .
```
