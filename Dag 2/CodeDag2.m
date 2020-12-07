clear;clc;close all;

data=readtable("Dag2input.txt");
valid=0;
for i=1:length(data.Var1)

    letter=string(data.Var3(i));
    word=split(string(char(data.Var4(i))),'');
    if(xor((word(data.Var1(i)+1)==letter),(word(data.Var2(i)+1)==letter)))
        valid=valid+1;
    end
    
    
end