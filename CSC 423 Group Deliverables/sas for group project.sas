libname perm 'C:\Users\Admin\Desktop\sasdata';

symbol1 font=marker value=U height=1.1 color=depk;

title "Scatter-plot of Brain Size vs FSIQ";
proc gplot data=work.brain;
plot MRI_count * FSIQ;
run;
title;

title "Scatter-plot of Brain Size vs VIQ";
proc gplot data=work.brain;
plot MRI_count * VIQ;
run;
title;

title "Scatter-plot of Brain Size vs PIQ";
proc gplot data=work.brain;
plot MRI_count * PIQ;
run;
title;

title "Scatter-plot of Brain Size vs Weight";
proc gplot data=work.brain;
plot MRI_count * Weight;
run;
title;

title "Scatter-plot of Brain Size vs Height";
proc gplot data=work.brain;
plot MRI_count * HEIGHT;
run;
title;

title "Scatter-plot of Brain Size vs Gender";
proc gplot data=work.brain;
plot MRI_count * Gender;
run;
title;

data work.transformed;
set work.brain;
x1 = (gender = "Male");
run;

title "Least-squares 2 Regression";
proc reg data=work.transformed plots=none;
model MRI_count = x1 FSIQ VIQ PIQ weight HEIGHT;
run;
title; 

title "Stepwise Regression";
proc reg data=work.transformed plots=none;
model MRI_count = x1 FSIQ VIQ PIQ weight HEIGHT / selection=stepwise;
run;
title;

title "Using FORWARD Regression";
proc reg data=work.transformed plots=none;
model MRI_count = x1 FSIQ VIQ PIQ WEIGHT HEIGHT / selection=FORWARD;
run;
title;

title "Using BACKWARD Regression";
proc reg data=work.transformed plots=none;
model MRI_count = x1 FSIQ VIQ PIQ WEIGHT HEIGHT / selection=BACKWARD;
run;
title;

title "Correlations among indpendent variables";
PROC CORR DATA = work.transformed ;
VAR x1 FSIQ VIQ PIQ WEIGHT HEIGHT ;
RUN ;

title "Correlations among indpendent variables new model";
PROC CORR DATA = work.transformed ;
VAR x1 PIQ HEIGHT ;
RUN ;

title "Least-squares for new model";
proc reg data=work.transformed plots=none;
model MRI_count = x1 PIQ HEIGHT / p;
run;
title;

title "Partial residuals for new model";
proc reg data=work.transformed plots=none;
model MRI_count = x1 PIQ HEIGHT / partial;
plot residual.*x1;
plot residual.*PIQ;
plot residual.*HEIGHT;
run;
title;


data work.transformed2;
set work.transformed;
MRI_count_ln = log(MRI_Count);
run;

title "transformation on the dependent variable to reduce hetero";
proc reg data=work.transformed2 plots=none;
model MRI_count_ln = x1 PIQ HEIGHT;
plot residual.*PIQ;
plot nqq.*residual.; 
run;

title "Regression with studenstize residuals";
proc reg data=work.TRANSFORMED2 plots=none;
model MRI_count= x1 PIQ HEIGHT / R INFLUENCE ;
plot student.*x1;
plot student.*PIQ;
run;
title;

title "Regression with DW";
proc reg data=work.TRANSFORMED2 plots=none;
model MRI_count= x1 PIQ HEIGHT / dw;
run;
title;
