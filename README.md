# LogRoast

LogRoast runs through the firewall log file looking for all outbound connections. Once gathered, the destination IP addresses are aggregated and a Whois api call is performed on each unique IP address. The result is a table showcasing all the outbound destination addresses, how many times each unique address was connected to by the localhost and which organisation owns the destination IP address. This tool works for Debian based Linux and Windows.

![Screenshot 2022-03-09 at 11 36 54](https://user-images.githubusercontent.com/53338724/157515382-bfe2db14-d582-49a6-9c4a-c2399b632bce.png)

This screenshot show cases the functionality of LogRoast in Ubuntu. The tool requires UFW to work so it searchs for ufw.log files. If it cannot find them, it will install UFW and enable logging. Therefore when run with Python, the tool must be run with sudo privileges or as root.


![Screenshot 2022-03-09 at 11 51 14](https://user-images.githubusercontent.com/53338724/180252338-cdee4d91-f64e-4dda-83cb-07eea4ad5f14.png)

This screenshot showcase the functionality of LogRoast in Windows. The tool automatically searchs to see if the Windows firewall log is populated. If not, it will enable logging through the use of powershell. Therefore the executable of this tool must be run with administrator privileges or with Python via a command prompt with administrator privileges.
