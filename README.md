# component-costing

Component costing is a group of programs used to scrape costs of a list of components from websites and output a csv with the 
cost of the components at different quantities. The input is a list of web addresses of each part. The script scrapes the prices
and stores them in a json file, then uses that json file to populate the csv.

Currently, the script only supports Digikey, but will grow to include Mouser and other suppliers, so that prices can be compared
between them.
