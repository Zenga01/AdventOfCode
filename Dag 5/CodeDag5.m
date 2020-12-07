clear;clc;close all;
totalRows=128;
maxSeatID=0;
seatIDs=[];
boardingPasses=readFile("BoardingPasses.txt");
% boardingPasses=readFile("testCase.txt");
tic
for passNumber=1:length(boardingPasses)
    boardingPass=split(boardingPasses(passNumber),'');
    boardingPass=boardingPass(2:11);
    seatID=getSeatID(boardingPass);
    seatIDs(end+1)=seatID;
    if (seatID>maxSeatID)
        maxSeatID=seatID;
    end
end
for i=1:maxSeatID
    if(~any(seatIDs(:) == i))
        if(any(seatIDs(:)==i-1)&&any(seatIDs(:)==i+1))
            mySeat=i;
            break;
        end
    end
end
toc

function seatID=getSeatID(boardingPass)
    row=0;
    col=0;
    binarySet=[64,32,16,8,4,2,1,4,2,1];
    for i=1:length(boardingPass)
        if(boardingPass(i)=="B")
            row=row+binarySet(i);
        elseif(boardingPass(i)=="R")
            col=col+binarySet(i);
        end 
    end
    seatID=(row)*8+(col);
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