import timeit

def time(bench='pyth', size=10):
    number = 1
    count = 10000000
    t = timeit.timeit(bench + '.run(' + str(count) + ')', setup='import ' + bench + '; ' + bench + '.setup(' + str(size) + ')',number=number)
    print bench + ' ' + str(size) + ' ' + str(t)
    
def run(benches='cyth', sizes=10):
    if isinstance(benches, str):
        benches = [benches]
    if isinstance(sizes, int):
        sizes = [sizes]
    for b in benches:
        for s in sizes:
            time(bench=b, size=s)
