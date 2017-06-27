prtg_updater
PRTG Channel Settings updater

Description:
-----------------------------------------------------------------------------------------------
This script logs in the prtg server and change the channel settings according to the values in ini file, that must be a json file, see example file!
Step 1.
For the login you need a hashkey. Open the following page on the firewall with a credential, example:
http://yourprtgserverip/api/getpasshash.htm?username=yourusername&password=yourpassword
In the output is your hashkey.
Step 2.
After that just test it like this example (change the IP and the key for you!):
$ ./sensorupdater.py -host 1.1.1.1 -user root -pass 123 -ini ini.json
Done...

Syntax:
-------
$ ./sensorupdater.py -host <prtg-srv-ip> -user <username> -pass <password> -ini <inifile>

Mandatory arguments:
--------------------
<prtg-srv-ip>			: The IP or hostname of the prtg server.
<username>			: Username for the logon on prtg.
<password>			: The password
<inifile>				: The ini file in json format

Output:
-------
prints the following output:
Done...

Example:
--------
$ ./sensorupdater.py -host 1.1.1.1 -user prtgadmin -pwd admin1234 -file filter.json
Done...

filter.json can be filled up according to the tag description found here from PRTG:
PRTG API (Application Programming Interface) -> Custom Sensors:
https://prtg.paessler.com/api.htm?username=demo&password=demodemo&tabid=7
