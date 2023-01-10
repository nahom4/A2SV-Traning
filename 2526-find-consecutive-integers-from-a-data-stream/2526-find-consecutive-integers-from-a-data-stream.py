class DataStream:

    def __init__(self, value: int, k: int):
        self.data_stream = [[value,k]]
        self.count = 0
        
    
    def consec(self, num: int) -> bool:
       
        self.data_stream.append(num)
        if len(self.data_stream) - 1 < self.data_stream[0][1]:
            
         
            
            if self.data_stream[0][0]==num:
                self.count += 1
            else:
                self.count = 0
         
            return False
        else:
           
            if self.data_stream[0][0]==num:
                    self.count += 1
            else:
                    self.count = 0

            if self.count >= self.data_stream[0][1]:
                return True
            else:
                return False

        

