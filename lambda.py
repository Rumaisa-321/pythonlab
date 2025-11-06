sq = lambda a:a*a; rect = lambda l,b:l*b;
tri = lambda b,h:0.5*b*h
a = float(input("square side:"));
l = float(input("rect length:"))
b = float(input("rect braedth:"));
bt = float(input("tri base:"));
h = float(input("tri height:"))
print("square:",sq(a),"rectangle:",rect(l,b),"triangle",tri(bt,h))
