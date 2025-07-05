import zipfile as z
import json as j
import os
import shutil
import time
import app.settings.settings as s
from app.logics.id_creator import id_creator

# Here for debug purposes, something may crash if not
# here (some kind of coconut.jpg function idk)
def clique():
    print("cliqué!")

def convert_date(date):
    if not type(date)=="str":
        date=str(date)
    return time.strptime(date, "%Y%m%d%H%M%S")

def format_date(date_converted,date_format):
    return time.strftime(date_format, date_converted)

class Item:
    def __init__(self,properties):
        self.properties=properties

    def read_properties(self):
        print("Item properties: ",self.properties)

    def get_properties(self,info_file):
        with z.ZipFile(self.path,'r') as archive:
            with archive.open(info_file) as infos:
                self.properties=j.load(infos)
        self.read_properties()
    

class Inventory:
    def __init__(self,folder_name,path):
        self.folder_name=folder_name
        self.path=path
        self.properties={}
        self.items=[]

    def read_properties(self):
        print("IVT Properties: ",self.properties)

    def get_properties(self,info_file):
        with z.ZipFile(self.path,'r') as archive:
            with archive.open(info_file) as infos:
                self.properties=j.load(infos)
        self.read_properties()

    def get_item(self,item_file):
        with z.ZipFile(self.path,'r') as archive:
            with archive.open(item_file) as item:
                self.items.append(Item(j.load(item)))
                print("Item added: ", self.items[-1].properties['id'])
        self.read_properties()

class Database:

    def __init__(self,path):
        self.path=path
        self.root_of_db=None
        self.properties={}
        self.files_in_db=[]
        self.inventories={}
        
        self.get_properties()
        self.build_inventories()

    def read_properties(self):
        print("DB Properties: ", self.properties)

    def get_properties(self):
        with z.ZipFile(self.path,'r') as archive:
            self.files_in_db=archive.namelist()
            for file in self.files_in_db:
                if "db.info" in file:
                    info_file=file
                    self.root_of_db=file[:-7]
                    break
            with archive.open(info_file,'r') as infos:
                self.properties=j.load(infos)
        self.read_properties()

    def current_inventories(self):
        print("Current IVTs :",self.inventories.keys())
        
    def build_inventories(self):
        print("Files in DB: ",self.files_in_db)
        for f in self.files_in_db:
            if f=='db.info':
                continue
            parts = f.split('/')
            if len(parts) >= 2 and parts[0] == "Inventories":
                key = parts[1]
                print("Key: ",key)
            else:
                print("Ignored file: ",f)
                continue
            if (not key in self.inventories):
                print("New key: ", key, self.path)
                self.inventories[key]=Inventory(key,self.path)
            if f.endswith(".itm"):
                print("Add an itm")
                self.inventories[key].get_item(f)
            if f.endswith("ivt.info"):
                print("Read infos")
                self.inventories[key].get_properties(f)

# May move to settings.py
def select_format(db_format):
    if db_format=="ivtdb":
        return "inventore It! Database (v1)"

def compress(path,db_format):
    with z.ZipFile(path+"."+db_format, "w", z.ZIP_DEFLATED) as archive:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                archive.write(file_path,
                              os.path.relpath(file_path, start=path))

def create_database(name,path,db_format,inventories):
    for loop in range(0,1):
        if path=="":
            path=os.getcwd()
        elif not os.path.isabs(path):
            path=os.path.abspath(path)
        path=path+"/"+name
        try:
            os.mkdir(path)
        except FileExistsError as e:
            print("Folder already exist")
            return e
        except Exception as e:
            print(e)
            break
        now_str=time.strftime("%Y%m%d%H%M%S", time.localtime())
        now=int(now_str)
        
#### ADD A LOGIC FOR MULTIPLE FORMATS
  # Maybe create outer files for each db formats, or one big that
  # contain every function to create any type of db
#### CREATION FOR IVTDB (v1)
## Add a log.state creation for inventories and db
        db_id=str(id_creator(now))
        e_str=["{\"id\":\"",db_id,
               "\",\n\"name\":\"",name,
               "\",\n\"created\":",now_str,
               ",\n\"updated\":",now_str,
               ",\n\"owner\":\"",os.getlogin(),
               "\",\n\"format\": \"",select_format(db_format),"\"\n}"]
        string=""
        for i in range(len(e_str)):
            string+=e_str[i]
        with open(path+"/db.info","w",encoding='utf-8') as f:
            f.write(string)
            f.close()
        logst=open(path+'/log.state',"w",encoding='utf-8')
        logst.close()
        os.mkdir(path+f"/Inventories")
        for inventory in inventories:
            ivt_id=str(id_creator(now))
            ivt_path=path+f"/Inventories/{ivt_id}"
            os.mkdir(ivt_path)
            os.mkdir(ivt_path+f"/logs")
            logst=open(ivt_path+'/log.state',"w",encoding='utf-8')
            logst.close()
            fields="["
            for fld in (inventories[inventory]):
                fields+="\""+fld+"\""
                if not fld==inventories[inventory][-1]:
                    fields+=","
            fields+="]"
            e_str=["{\"id\":\"",ivt_id,
                   "\",\n\"name\":\"",inventory,
                   "\",\n\"created\":",now_str,
                   ",\n\"updated\":",now_str,
                   ",\n\"fields\":",fields,"\n}"]
            string=""
            for i in range(len(e_str)):
                string+=e_str[i]
            with open(ivt_path+"/ivt.info","w",encoding='utf-8') as f:
                f.write(string)
                f.close()
#### END
        compress(path, db_format)
        shutil.rmtree(path)

def open_database(path):
    close_database()
    time.sleep(1)
    s.db=Database(path)
    s.db_instance=True

def close_database():
    s.db=None
    s.db_instance=False

    