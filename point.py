class point:
    def __init__(p1,dim, data):
        p1.dim=dim
        p1.data=[]
        for i in range(dim):
            p1.data.append(float(data[i]))
    def __repr__(p1):
        output=""
        for i in p1.data:
            output+=str(i)+" "
        return output
    def scale(p1, x):
        for i in range(p1.dim):
            p1.data[i]*=x
    def dot(p1, p2):
        sum=0
        for i in range(p1.dim):
            sum+=p1.data[i]*p2.data[i]
        return sum

    def dist(p1, p2):
        return math.sqrt((self.data[0]-p2.data[0])**2+(self.data[1]-p2.data[1])**2+(self.data[2]-p2.data[2])**2)
        print(p1.dist(p2))
        
  
