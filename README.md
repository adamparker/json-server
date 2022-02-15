# json-server

This is a simple HTTP web server written in Python3 that serves local JSON files over HTTP.

I struggled to find anything that perfectly met the requirements, so I made this.  It is purely for development purposes.

You can put this in /usr/local/bin/ and run it from any directory to serve that directory.  Remember to make it executable with 'chmod +x ./jsonserver.py'.  It requires several libraries which are evident from the import lines at the beginning.

## Examples

If you have a file called 'jsonfile' then the following URL will serve it http://localhost:12345/jsonfile

If you want to emulate a REST interface of some sort, putting a file in a subfolder such as /students/1 would serve this under the URL http://localhost:12345/students/1

This means you can develop your frontend and manipulate the backend data trivially.



