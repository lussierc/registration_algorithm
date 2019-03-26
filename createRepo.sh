#!/bin/bash  
git init
git add --all
git commit -m "first commit"
git remote remove origin
git remote add origin git@github.com:amohangit/$1
git push -u origin master