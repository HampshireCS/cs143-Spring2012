from fabric.api import *
import getpass

hosts = [ "%02d" % i for i in range(20) ]
hosts[0] = "sensei"
env.hosts = [ "Administrator@asheclass-"+h for h in hosts ]
env.password = getpass.getpass()

def deploy():
    with cd("/tmp"):
        run("wget http://stout.hampshire.edu/~acg10/pyside.pkg")
        sudo("installer -target / -pkg  pyside.pkg")

def fixqt():
    run("mkdir -p /Applications/Qt")
    sudo("chmod -R 755  /Developer/QtSDK/Desktop")
    run("ln -s /Developer/QtSDK/Desktop/474/gcc/bin/Designer.app /Applications/Qt/Designer.app")
    run("ln -s /Developer/QtSDK/Qt\ Creator.app /Applications/Qt/Qt\ Creator.app")

def qtframeworks():
    run("rm /Applications/Qt/Designer.app")
    run("ln -s /Developer/QtSDK/Desktop/Qt/474/gcc/bin/Designer.app /Applications/Qt/Designer.app")
    run("ln -s /Developer/QtSDK/Desktop/Qt/474/gcc/lib/*.framework /Library/Frameworks")