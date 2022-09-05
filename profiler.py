import cProfile, pstats, io
import karatsuba.python.karatsuba as k
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()
cProfile.run("k.karatsuba('1234123412341234','567856785678')")
pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())