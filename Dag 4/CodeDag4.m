clear;clc;close all;
fieldSet={'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'};
valueSet={'','','','','','','',''};
currentPassport=containers.Map(fieldSet,valueSet);
valid=0;
% validation{'byr'}=0;
data=readFile("Dag5input.txt");
tic
for i=1:length(data)
    if (string(data(i))=="")
        valid=valid+passportValidation(currentPassport);
        
        for m=1:length(fieldSet)
%             disp(fieldSet(m)+":"+validate(char(fieldSet(m))));
        end
        currentPassport=containers.Map(fieldSet,valueSet);
%         disp("New Passport");
    else
        fields=split(data(i),' ');
        for j=1:length(fields)
            keyPair=split(fields,':');
            if(numel(keyPair)>2)
                for k=1:length(keyPair)
                    if(any(strcmp(keyPair(k,1),fieldSet),'all'))
                        currentPassport(char(keyPair(k,1)))=char(keyPair(k,2));
                    end
                end
            else
                if(any(strcmp(fieldSet,keyPair(1))))
                    currentPassport(char(keyPair(1)))=char(keyPair(2));
                    
                end
            end
        end
    end
    
end
toc;
function valid=passportValidation(passport)
    checkSet={'byr','iyr','eyr','hcl','hgt','ecl','pid'};
    regexps=["^19[2-9][0-9]|200[0-2]$","^2020|201[0-9]$","^2030|202[0-9]$",...
        "^#([a-f]|[0-9]){6}$","^(1[5-8][0-9]|19[0-3])cm|((59|6[0-9]|7[0-6])in)$",...
        "^(amb|blu|brn|gry|grn|hzl|oth)$","^\d{9}$"]; 
    valid=1;
    for ii=1:length(checkSet)
        if(isempty(passport(char(checkSet(ii)))))
            valid=0;
            return
        end
        if(isempty(regexp( passport(char(checkSet(ii))), regexps(ii), 'once') ))
%             disp (checkSet(ii))
%             disp(passport(char(checkSet(ii))));
            valid=0;
            return;
        end
    end
end

function data=readFile(fileName)
fid=fopen(fileName,'r');
data = cell(0,1);
inputLine = fgetl(fid);
while(ischar(inputLine))
    data{end+1,1}=inputLine;
    inputLine=fgetl(fid);
end
data=split(data,"\n\n");
fclose(fid);
end

function valid=regexpbyr(value)
expression="(1[5-8][0-9]|19[0-3])cm|((59|6[0-9]|7[0-6])in)";
if(regexp(value,expression))
    valid=true;
end
end

