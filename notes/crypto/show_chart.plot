file='/tmp/eth100'; size=10000; plot file using ($1*size):10, file using ($1*size):4 with lines, file using ($1*size):8 with lines, file using ($1*size):9 with lines;
file='/tmp/eth40'; size=1; plot file using ($1*size):($5):($5*0.0002) with points pt 7 ps var;             
set grid xtics ytics mxtics mytics; file='/tmp/eth40'; size=1; plot file using ($1*size):($5>10?$5:10):(0.5) with points pt 7 ps var;
set grid xtics ytics mxtics mytics; set logscale y; set xtics 0.001;  file='/tmp/eth40'; size=1; plot file using ($1*size):($5>10?$5:10):(0.5) with points pt 7 ps var;
file='/tmp/eth40'; size=1; plot file using ($1*size):10, file using ($1*size):4 with lines, file using ($1*size):8 with lines, file using ($1*size):9 with lines;
