import tkinter as tk
from tkinter import ttk, messagebox
import heapq

class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n)); self.rank=[0]*n
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        rx,ry=self.find(x),self.find(y)
        if rx==ry: return False
        if self.rank[rx]<self.rank[ry]:
            rx,ry=ry,rx
        self.parent[ry]=rx
        if self.rank[rx]==self.rank[ry]:
            self.rank[rx]+=1
        return True

def kruskal(n,edges):
    e=sorted(edges)
    uf=UnionFind(n)
    mst=[]; cost=0
    for w,u,v in e:
        if uf.union(u,v):
            mst.append((u,v,w)); cost+=w
    return mst,cost

def prim(n,adj,start=0):
    key=[float("inf")]*n
    parent=[-1]*n
    vis=[False]*n
    key[start]=0
    pq=[(0,start)]
    mst=[]; cost=0
    while pq:
        w,u=heapq.heappop(pq)
        if vis[u]: continue
        vis[u]=True
        if parent[u]!=-1:
            mst.append((parent[u],u,w)); cost+=w
        for v,wt in adj.get(u,[]):
            if not vis[v] and wt<key[v]:
                key[v]=wt; parent[v]=u
                heapq.heappush(pq,(wt,v))
    return mst,cost

n=7
edges=[
(7,0,1),(5,0,3),(8,1,2),(9,1,3),
(7,1,4),(5,2,4),(15,3,4),(6,3,5),
(8,4,5),(9,4,6),(11,5,6)
]
adj={}
for w,u,v in edges:
    adj.setdefault(u,[]).append((v,w))
    adj.setdefault(v,[]).append((u,w))

def run():
    out.delete("1.0",tk.END)
    km,kc=kruskal(n,edges)
    pm,pc=prim(n,adj)
    out.insert(tk.END,"KRUSKAL MST\n")
    out.insert(tk.END,"-"*35+"\n")
    for u,v,w in km:
        out.insert(tk.END,f"{u} -- {v}   Weight={w}\n")
    out.insert(tk.END,f"\nTotal Cost = {kc}\n\n")
    out.insert(tk.END,"PRIM MST\n")
    out.insert(tk.END,"-"*35+"\n")
    for u,v,w in pm:
        out.insert(tk.END,f"{u} -- {v}   Weight={w}\n")
    out.insert(tk.END,f"\nTotal Cost = {pc}\n")
    messagebox.showinfo("Success","Algorithms executed successfully!")

root=tk.Tk()
root.title("MST Mini Project - Prim & Kruskal")
root.geometry("700x550")

tk.Label(root,text="Minimum Spanning Tree Visualizer",
font=("Arial",18,"bold")).pack(pady=10)

ttk.Button(root,text="Run Algorithms",command=run).pack(pady=5)

out=tk.Text(root,font=("Consolas",11),width=80,height=22)
out.pack(padx=10,pady=10)

root.mainloop()