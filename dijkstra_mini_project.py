import tkinter as tk
from tkinter import ttk
import heapq

graph={
0:[(1,4),(2,1)],
1:[(3,1)],
2:[(1,2),(3,5)],
3:[(4,3)],
4:[(5,2)],
5:[]
}

def dijkstra(graph,source):
    n=len(graph)
    dist=[float('inf')]*n
    prev=[None]*n
    dist[source]=0
    pq=[(0,source)]
    vis=set()
    while pq:
        d,u=heapq.heappop(pq)
        if u in vis: continue
        vis.add(u)
        for v,w in graph[u]:
            if dist[u]+w<dist[v]:
                dist[v]=dist[u]+w
                prev[v]=u
                heapq.heappush(pq,(dist[v],v))
    return dist,prev

def path(prev,s,t):
    p=[]
    while t is not None:
        p.append(t)
        t=prev[t]
    p.reverse()
    return p if p and p[0]==s else []

def run():
    for i in tree.get_children():
        tree.delete(i)
    src=int(source.get())
    dist,prev=dijkstra(graph,src)
    for v in range(len(graph)):
        p=" -> ".join(map(str,path(prev,src,v)))
        d="INF" if dist[v]==float("inf") else dist[v]
        tree.insert("",tk.END,values=(v,d,p))

root=tk.Tk()
root.title("Dijkstra Shortest Path Visualizer")
root.geometry("700x450")

tk.Label(root,text="Dijkstra's Algorithm Mini Project",font=("Arial",18,"bold")).pack(pady=10)
top=tk.Frame(root); top.pack()
tk.Label(top,text="Source Vertex:").pack(side=tk.LEFT)
source=ttk.Combobox(top,values=[0,1,2,3,4,5],width=5)
source.current(0)
source.pack(side=tk.LEFT,padx=5)
ttk.Button(top,text="Run",command=run).pack(side=tk.LEFT,padx=5)

cols=("Vertex","Distance","Shortest Path")
tree=ttk.Treeview(root,columns=cols,show="headings")
for c in cols:
    tree.heading(c,text=c)
tree.column("Vertex",width=80)
tree.column("Distance",width=100)
tree.column("Shortest Path",width=450)
tree.pack(fill="both",expand=True,padx=10,pady=10)

run()
root.mainloop()