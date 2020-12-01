# L-Cloud
L-Cloud is private cloud for linux environment for services of Storage(StaaS) and Software(StaaS)


# Steps to configure and install in your system
There are two sides of this project:

SERVER SIDE
1. Since this server is designed on RHEL7- distribution of linux , it requires RHEL as
a backend
2. Backend is designed with Python3, therefore python3 is required in your system
3. Install openssh-server and make sure ssh server with X-window system running
4. Install nfs-util for nfs server
5. Off the selinux and flush the firewall rules
6. Change the IP adress in file with yours
7. Install Docker in your system
8. Download and configure all the software with is included for giving services 
9. Create a VG(volume group)of your any partition and rename it as /dev/cloud
10. Run the Start.py...and your server will start for client


CLIENT SIDE
1. Client have to ensure that python3 with Tkinter module is installed
2. Run the App.py file with python3.
