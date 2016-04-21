import sys
import SimpleHTTPServer
import SocketServer
import webbrowser
import numpy as np
import pandas as pd
import os

fam = str(sys.argv[1])
if fam.endswith('.csv'):
    pd.set_option('display.max_colwidth', -1)
    base=os.path.basename(fam)
# reads relationships from csv file and only keeps relevant columns
    df = pd.read_csv(fam)
# concatenates each input, output, and category into javascript link format
    outlist = []
    for inp, outp, category in zip(df['Input'], df['Output'], df['Category']):
        if category == 'friends':
            outlist.append('{source: "'+inp+'", target: "'+outp+'", type: "friend"},')
        else:
            outlist.append('{source: "'+inp+'", target: "'+outp+'", type: "family"},')
    ostring = []
    filename = os.path.splitext(base)[0]+"out.txt"
    with open(filename, "w") as outfile:
        for item in outlist:
            # pick only unique values
            if item not in ostring:
                ostring.append(item)
                outfile.write("%s\n" % item)
    # remove trailing comma from the end of file
    with open(filename, 'rb+') as filehandle:
        filehandle.seek(-2, os.SEEK_END)
        filehandle.truncate()

    # concatenate html templates and outfile into final html file for js visualization
    filenames = ['template1.html', filename, 'template2.html']
    with open('index.html', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read())
os.chmod(outfile.name, 0777)

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
new = 2 # open in a new tab, if possible

# open this visualization index.html hosted in current directory
url = "localhost:"+str(PORT)

webbrowser.open(url)

httpd.serve_forever()
