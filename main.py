import csv
import cherrypy
# import pdb; pdb.set_trace()

class SearhCSV(object):

  @cherrypy.expose
  def index(self):
    html_body = \
    """
    <h3>Search in CSV file</h3>

    <div>Select search field:</div>
    <form method="post" action=searchFile>
      <select name="search_field"
        <option value="ITEM SKU">Item SKU</option>
        <option value="PRODUCT NAME">Product name</option>
        <option value="BRAND NAME">Brand name</option>
        <option value="EAN">EAN</option>
        <option value="REQUIRED PRICE TO AMAZONE">Required price to amazon</option>
      </select>
      <p></p>
      <p>Input search field value:</p>
        <form method="post" action="searchFile">
          <input type="text" name="search_value"/>
          <button type="submit">Search</button>
    </form>
    """
    return html_body


  @cherrypy.expose
  def searchFile(self, search_field, search_value):
    with open("DataFile\\test.mod.csv", mode='r', encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        dict_list = list(reader)
    for item in dict_list:
      for key, value in item.items():
        if key != search_field:
          continue
        else:
          if value == search_value:
            return f"Search key: {key}\tValue: {value}\n{item}"

if __name__ == '__main__':
    cherrypy.quickstart(SearhCSV())