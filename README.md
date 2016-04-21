# my_network
This python script generates a web page with a d3.js visualization of the relationships between people specified in an input csv table.

Input CSV file must be in this format:

Input, Output, Category

Pam,Tom,wife

Tom,John,friends

Sidney,Morgan,friends

Casey,Justin,brother


Friendships (Category = friends) are displayed with green links, while all other relationships (Category != friends) are assumed to be family and are displayed with red links

The python script launches a server instance in the current directory and launches a browser tab with the generated visualization index.html file

d3 force layout is based on http://bl.ocks.org/mbostock/1153292
