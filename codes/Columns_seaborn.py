class Columns_seaborn:

    def __init__(self,col_1,col_2,col_3):
        self.col1 = col_1
        self.col2 = col_2
        self.col3 = col_3

    def __str__(self):
        return str(self.col1)+","+str(self.col2)+","+str(self.col3)+",\n"
