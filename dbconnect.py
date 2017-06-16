import clipy as clipy

@clipy.clipy(name=__name__)
def dbconnect(
    name,
    func_usage="""
    Connect to your mongodb database
    """,
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
