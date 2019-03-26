#!/bin/bash  
cd $1
git init
git remote remove origin
git remote add origin git@github.com:amohangit/$1.git
git fetch git@github.com:amohangit/$1.git
