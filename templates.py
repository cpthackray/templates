class Template:
    def __init__(self, source, outpath='', tag='@@'):
        self.source = source
        self.outpath = outpath
        self.tag = tag
        self.read_source()

    def read_source(self):
        with open(self.source, 'r') as f:
            self.contents = f.read()

        # generate tags to be filled
            
    def fill(self, fill_dict):
        # check all tags will fill
        print(fill_dict)
        for key in fill_dict:
            self.contents = self.contents.replace(self.get_tagged(key),
                                                  fill_dict[key])

    def get_tagged(self,key):
        return self.tag+key+self.tag
    
    def write(self, outpath=None):
        if outpath is None:
            outpath = self.outpath
        with open(outpath, 'w') as f:
            f.write(self.contents)


if __name__=='__main__':
    tem = Template('test.template', outpath='test.out')

    fill = {'FILL1': 'filled',
            'FILL2': 'filled twice'}

    tem.fill(fill)

    tem.write()
