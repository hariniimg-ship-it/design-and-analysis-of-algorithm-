
import time
import random

movies = [
    {"id":101,"name":"96","rating":8.5,"year":2018},
    {"id":103,"name":"Vikram","rating":8.3,"year":2022},
    {"id":105,"name":"Leo","rating":7.2,"year":2023},
    {"id":108,"name":"Master","rating":7.4,"year":2021},
    {"id":110,"name":"Kaithi","rating":8.5,"year":2019},
    {"id":115,"name":"Soorarai Pottru","rating":8.7,"year":2020},
    {"id":120,"name":"Thani Oruvan","rating":8.4,"year":2015},
    {"id":125,"name":"Mersal","rating":7.6,"year":2017},
    {"id":130,"name":"Asuran","rating":8.4,"year":2019},
    {"id":135,"name":"Love Today","rating":8.0,"year":2022},
    {"id":140,"name":"Ghilli","rating":8.6,"year":2004},
    {"id":145,"name":"Thuppakki","rating":8.1,"year":2012},
    {"id":150,"name":"Visaranai","rating":8.5,"year":2016},
    {"id":155,"name":"Ratsasan","rating":8.3,"year":2018},
    {"id":160,"name":"Ayan","rating":7.9,"year":2009}
]

ids=[m["id"] for m in movies]

def interpolation_search(arr,target):
    low,high=0,len(arr)-1
    comp=0
    while low<=high and arr[low]<=target<=arr[high]:
        comp+=1
        if arr[low]==arr[high]:
            return (low,comp) if arr[low]==target else (-1,comp)
        pos=low+int(((target-arr[low])*(high-low))/(arr[high]-arr[low]))
        if arr[pos]==target:
            return pos,comp
        elif arr[pos]<target:
            low=pos+1
        else:
            high=pos-1
    return -1,comp

def binary_search(arr,target):
    low,high=0,len(arr)-1
    comp=0
    while low<=high:
        comp+=1
        mid=(low+high)//2
        if arr[mid]==target:
            return mid,comp
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1,comp

def display_movies():
    print("\n{:<6}{:<22}{:<8}{}".format("ID","Movie","Rating","Year"))
    print("-"*50)
    for m in movies:
        print("{:<6}{:<22}{:<8}{}".format(m["id"],m["name"],m["rating"],m["year"]))

def search_movie():
    name=input("Enter Movie Name: ").strip().lower()
    movie=None
    for m in movies:
        if m["name"].lower()==name:
            movie=m
            break
    if not movie:
        print("Movie not found!")
        return
    start=time.perf_counter()
    idx_i,c_i=interpolation_search(ids,movie["id"])
    t_i=(time.perf_counter()-start)*1000
    start=time.perf_counter()
    idx_b,c_b=binary_search(ids,movie["id"])
    t_b=(time.perf_counter()-start)*1000
    print("\nMovie Found")
    print("-"*25)
    print("ID    :",movie["id"])
    print("Name  :",movie["name"])
    print("Rating:",movie["rating"])
    print("Year  :",movie["year"])
    print("\nInterpolation Search")
    print("Comparisons:",c_i)
    print("Time(ms): {:.6f}".format(t_i))
    print("\nBinary Search")
    print("Comparisons:",c_b)
    print("Time(ms): {:.6f}".format(t_b))

def performance_analysis():
    print("\n{:>8} {:>12} {:>12}".format("Size","IS(ms)","BS(ms)"))
    print("-"*36)
    for size in [1000,5000,10000,50000,100000]:
        arr=sorted(random.sample(range(size*10),size))
        target=random.choice(arr)
        s=time.perf_counter()
        for _ in range(100):
            interpolation_search(arr,target)
        is_t=(time.perf_counter()-s)/100*1000
        s=time.perf_counter()
        for _ in range(100):
            binary_search(arr,target)
        bs_t=(time.perf_counter()-s)/100*1000
        print(f"{size:>8} {is_t:>12.6f} {bs_t:>12.6f}")

while True:
    print("\n===== TAMIL MOVIE DATABASE =====")
    print("1. Display Movies")
    print("2. Search Movie")
    print("3. Performance Analysis")
    print("4. Exit")
    ch=input("Enter Choice: ")
    if ch=="1":
        display_movies()
    elif ch=="2":
        search_movie()
    elif ch=="3":
        performance_analysis()
    elif ch=="4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
