#!/bin/bash

# create blog direcotry
blog_dir=$1
if [ -z $blog_dir ]
then
    blog_dir=blog_tmp
fi

# install hexo-cli
npm install -g hexo-cli

# init blog
hexo init $blog_dir
cp -r _config.yml "source" $blog_dir
cp -r themes/pacmanBlue $blog_dir/themes
cd $blog_dir
npm install hexo-deployer-git --save
npm install
hexo generate

hexo server

hexo deploy
