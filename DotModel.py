import Dot
class DotModel:
     def __int__(self):
         self.dots=[]
         # This is to be uncommented when i figure out
         # how to implement an interface in pyhton
         # self.listener=[]
         self.nextZ=0

     def addDot(self,x,y):
         self.dots.append(Dot(x,y,2,self.nextZ+1 ))


     #This function is to be woked on later because it might
     # be modified to meet the problem
     def contains(self, x, y):
         for dot in self.dots:
              if dot.contains(x,y):
                  return True
              else:
                  return False