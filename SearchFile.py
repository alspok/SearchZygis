import cherrypy

class SearchFile(object):
    
    @cherrypy.expose
    def searchFile(self, search_key = 'EAN'):
        with open("DataFile\\MergeFile.mod.csv", mode='r', encoding='utf-8') as fh:
            reader = csv.DictReader(fh)
            dict_list = list(reader)
        
        for item in dict_list:
            for key, value in item.items():
                if key == search_key:
                    print(key, value)
                    print(item)
                    break
        return item

if __name__ == '__main__':
    SearchFile().searchFile()