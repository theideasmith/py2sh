import py2sh as py2sh

@py2sh.shify(
       name=__name__,
       usage="Connect to your mongodb database")                         
def dbconnect(
    name,
    pids=[],
    port=8080,
    nodename="",
    autoconnect=False,
    *args,
    **kwargs
    ):
  print "Name: "+ name
  print "Port: "+ str(port)
  print "Nodename: " + nodename
  print "Autoconnect: " + str(autoconnect)
  print pids
