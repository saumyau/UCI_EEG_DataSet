class Columns:

    def __init__(self,col_1,col_2):
        self.col1 = col_1
        self.col2 = col_2

    def __str__(self):
        return str(self.col1)+","+str(self.col2)+"\n"
