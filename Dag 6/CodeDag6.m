clear;clc;close all;
groupAnswers=readlines('Answers.txt');
input=fileread('Answers.txt');
groupsAnswers=regexp(input,'\n\n','split');
questions=["a","b","c","x","y","z"];
totalCount=0;
count1=0;
givenAnswers=[""];
lastLine=0;
tic;
for lineNumber=1:length(groupAnswers)
    if (groupAnswers(lineNumber)=="")
        groupLength=lineNumber-lastLine-1;
        for i=1:length(givenAnswers)
            if (givenAnswers(i)=="")
                continue;
            end
            if(sum(givenAnswers==givenAnswers(i))==groupLength)
                count1=count1+1;
            end
            givenAnswers(givenAnswers==givenAnswers(i))="";
        end
        totalCount=totalCount+count1;
        count1=0;
        givenAnswers=[""];
        lastLine=lineNumber;
        continue;
    end
    personAnswers=split(groupAnswers(lineNumber),'');
    
    for questionNumber=1:length(personAnswers)
%         if (any(questions(:)==personAnswers(questionNumber)))
%             if(any(givenAnswers(:)==personAnswers(questionNumber)))
%                 count1=count1+1;
                givenAnswers(end+1)=personAnswers(questionNumber);
%             end
%         end
    end 
end 
toc