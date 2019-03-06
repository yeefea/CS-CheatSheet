class Memento:
    def __init__(self, txt):
        self.data = txt


class Editor:
    def __init__(self, txt):
        self.txt = txt
    
    def set_txt(self, txt):
        self.txt = txt

    def save_to_memento(self):
        return Memento(self.txt)
    
    def load_from_memento(self, memento):
        self.txt = memento.data

    def __str__(self):
        return self.txt

if __name__ == '__main__':

    vim = Editor('hello vim')
    print(vim)
    memo = vim.save_to_memento()
    vim.set_txt('import math')
    print(vim)
    vim.set_txt('print(\'Hello world!\')')
    print(vim)
    vim.set_txt('raise exception')
    print(vim)
    vim.load_from_memento(memo)
    print(vim)

    




    