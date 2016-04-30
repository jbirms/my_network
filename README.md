This python script generates a web page with a d3.js visualization of the relationships between people specified in an input csv table.

[example link](http://jbirms.github.io/my_network/)

Input CSV file must be in this format:

Input, Output, Category <br />
Pam,Tom,wife <br />
Tom,John,friends <br />
Sidney,Morgan,friends <br />
Casey,Justin,brother <br />


Friendships (Category = friends) are displayed with green links, while all other relationships (Category != friends) are assumed to be family and are displayed with red links

The python script launches a server instance in the current directory and launches a browser tab with the generated visualization index.html file

d3 force layout is based on http://bl.ocks.org/mbostock/1153292
