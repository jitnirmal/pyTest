'''cProfile and line_profiler.
cProfile : default with python 2
 -- It exclusively measures CPU time and pays no attention to memory consumption
 -- ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    -- ncalls reports the number of calls to the function. 
 	-- tottime is the total time spent inside the function 
 	-- percall is simply the quotient of tottime divided by ncalls.
 	-- cumtime is the cumulative time spent inside the function including the time spent in subfunctions
 	-- filename:lineno(function) provides the file name, line number, and function name of the analyzed function.


line_profiler (https://github.com/rkern/line_profiler), a well-known profiler out there.


'''

import cProfile
import re
cProfile.run([1,2,3])