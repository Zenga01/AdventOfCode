clear;clc;close all;

data=readtable("inputDag3_1");
lines=string(data.Var1);
Matrix=split(lines,'');
slope=3;
slopeX=1;
count=0;
multiple=1;
Matrix=Matrix(:,2:32);
slopes=[[1,1],  %[steps right, steps down]
    [3,1],
    [5,1],
    [7,1],
    [1,2]];

for k=1:length(slopes)
    slopeX=slopes(k,1);
    slopeY=slopes(k,2);
    for i=0:slopeY:length(lines)-1
        if (Matrix(i+1,mod(slopeX/slopeY*i,31)+1)=="#")
            count=count+1;
        end
    end
multiple=multiple*count;
count=0;
end
multiple;
disp(num2str(multiple,'%i'));

