import os, urllib.request#, requests, io
##package for working with tar.gz
import tarfile

class realecHelper:
    def __init__(self,path_to_data=None,encoding='utf-8'):
        if path_to_data is not None:
            self.path = path_to_data
        self.get_file_path = 'http://realec.org/ajax.cgi?action=downloadFile&protocol=1&collection={}&document={}&extension={}'
        self.get_folder_path = 'http://realec.org/ajax.cgi?action=downloadCollection&protocol=1&collection={}'
        self.escape_slashes = lambda x: x.replace('/','%2F')
        self.encoding = encoding
        self.cut_site_name = lambda x: x[18:].lstrip('/') if x.startswith('http://realec.org/') else x

    def search_text(self,text_to_search,folder='',encoding='ansi'):
        if self.path is not None:
            no_neg_numb = lambda x: x*int(x>0)
            results = []
            if folder:
                path_to_search = self.path
            else:
                path_to_search = os.path.join(self.path,folder)
            for root,dirs,files in os.walk(path_to_search):
                for f in files:
                    if f.endswith('.txt'):
                        filename = os.path.join(root,f)
                        try:
                            t = open(filename,'r',encoding=encoding).read()
                        except:
                            print(filename)
                            continue
                        match_index = t.find(text_to_search)
                        if match_index!=-1:
                            result_start_position = no_neg_numb(match_index-30)
                            result_fin_position = match_index+len(text_to_search)+30
                            result = (filename,t[result_start_position:result_fin_position])
                            print(result)
                            results.append(result)
        else:
            print('Cannot search - must download data or specify the path to it first')

    def download_folder(self, path_to_folder='/exam/', path_to_saved_folder='.',make_current=True):
        '''путь к папке с данными realec, которые будут скачаны, нужно задавать именно здесь'''
        ##нужно что-то делать с повторяющимися именами
        folder_request, folder_name =  self.form_folder_request(path_to_folder, return_folder_name = True)
        t = tarfile.open(fileobj=urllib.request.urlopen(folder_request), mode='r:gz')
        t.extractall(path=path_to_saved_folder)
        t.close()
        print('folder {} from realec.org succesfully saved to {}'.format(folder_name, path_to_saved_folder))
        if make_current:
            self.path = os.path.join(path_to_saved_folder, folder_name)

    def form_folder_request(self, path, return_folder_name = False):
        path = self.cut_site_name(path)
        if return_folder_name:
            folder_name = path.strip('/').split('/')[-1]
            path = self.escape_slashes(path)
            return (self.get_folder_path.format(path), folder_name)
        else:
            path = self.escape_slashes(path)
            return self.get_folder_path.format(path)

    def download_document(self, path_to_document, path_to_saved_document='.', save=False):
        '''file name must contain extension'''
        document_name = self.escape_slashes(path_to_document)
        path_to_document = self.form_document_request(path_to_document)
        with urllib.request.urlopen(path_to_document) as f:
            self.current_document = f.read().decode(self.encoding)
        if save:
            with open(os.path.join(path_to_saved_document,document_name),'w',encoding=self.encoding) as t:
                t.write(self.current_document)

    def form_document_request(self, path):
        path = self.cut_site_name(path)
        last_slash = path.rfind('/')
        collection = path[:last_slash]
        file = path[last_slash:]
        file, extension = file.rsplit('.')
        file = file.strip('/')
        collection = self.escape_slashes(collection)
##        print(self.get_file_path.format(collection,file,extension))
##        raise Exception
        return self.get_file_path.format(collection,file,extension)
    
    def download_essay(self, path_to_essay, path_to_saved_essay='.', include_ann=True, include_json=True, save=False):
        path_to_essay = path_to_essay.rsplit('.')[0]
        essay_name = self.escape_slashes(path_to_essay)
        path_to_text = self.form_document_request(path_to_essay+'.txt')
        with urllib.request.urlopen(path_to_text) as f:
            self.current_text = f.read().decode(self.encoding)
            if save:
                with open(os.path.join(path_to_saved_essay,essay_name)+'.txt','w',encoding=self.encoding) as t:
                    t.write(self.current_text)
        if include_ann:
            path_to_ann = self.form_document_request(path_to_essay+'.ann')
            with urllib.request.urlopen(path_to_ann) as f:
                self.current_ann = f.read().decode(self.encoding)
                if save:
                    with open(os.path.join(path_to_saved_essay,essay_name)+'.ann','w',encoding=self.encoding) as t:
                        t.write(self.current_ann)
        if include_json:
            path_to_json = self.form_document_request(path_to_essay+'.json')
            with urllib.request.urlopen(path_to_json) as f:
                self.current_json = f.read().decode(self.encoding)
                if save:
                    with open(os.path.join(path_to_saved_essay,essay_name)+'.json','w',encoding=self.encoding) as t:
                        t.write(self.current_json)
        
def simple_search1(text):
    path = r'P:\realec_dumps\realec_dump_26_02_2018\data\exam'
    r = realecHelper(path)
    r.search_text(text)

def module_test():
    corpus = realecHelper()
    corpus.download_folder(path_to_saved_folder = r'P:\trash')
    corpus.search_text("percentage of UK residents")

def get_essay():
    r = realecHelper()
    while True:
        r.download_essay(input())
        print(r.current_text)
        print(r.current_ann)
        print(r.current_json)

