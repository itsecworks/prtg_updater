prtg_updater
PRTG Channel Settings updater

Description:
-----------------------------------------------------------------------------------------------
This script logs in the prtg server and change the channel settings according to the values in filter file, that must be a json file, see example file!
Step 1.
For the login you need a hashkey. Open the following page on the firewall with a credential, example:
<pre><code>http://yourprtgserverip/api/getpasshash.htm?username=yourusername&password=yourpassword</code></pre>
In the output is your hashkey.
Step 2.
After that just test it like this example (change the IP and the key for you!):
<pre><code>$ ./sensorupdater.py 1.1.1.1 root 123 filter.json</code></pre>
Done...

Syntax:
-------
<pre>$ ./sensorupdater.py <code>&lt;prtg-srv-ip&gt; &lt;username&gt; &lt;password&gt; &lt;inifile&gt;</code></pre>

Mandatory arguments:
--------------------
<pre>
<code>&lt;prtg-srv-ip&gt;</code>	: The IP or hostname of the prtg server.
<code>&lt;username&gt;</code>		: Username for the logon on prtg.
<code>&lt;password&gt;</code>		: The password
<code>&lt;inifile&gt;</code>		: The filter file in json format
</pre>
	
Output:
-------
prints the following output:
Done...

Example:
--------
<pre><code>$ ./sensorupdater.py 1.1.1.1 prtgadmin admin1234 filter.json</code></pre>
Done...

filter.json can be filled up according to the tag description found here from PRTG:
PRTG API (Application Programming Interface) -> Custom Sensors:
https://prtg.paessler.com/api.htm?username=demo&password=demodemo&tabid=7
