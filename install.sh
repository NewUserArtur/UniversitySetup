#!/bin/bash

# general packages
{
    sudo apt update && sudo apt install $(cat .config/requirements)
} || {
    sudo dnf update && sudo dnf install $(cat .config/requirements)
} || {
    echo "Could not install required packages"
    exit 1
}

# python packages
{
    python3 -m pip install $(cat .config/requirements_python)
} || {
    echo "Could not install required python packages"
    exit 2
}

# all the files
while true; do
    echo "Enter path where to install"
    {
        read mypath &&
        eval mypath=$mypath &&
        mkdir -p $mypath &&
        mkdir -p $mypath/.config &&
        cp .config/sxhkdrc $mypath/.config &&
        cp .config/tint2rc $mypath/.config &&
        mydata=$(cat .config/sxhkdrc) &&
        echo "${mydata//MYPATH/"$mypath"}" > $mypath/.config/sxhkdrc &&
        cp -r .scripts $mypath &&
        cp -r .templates $mypath &&
        cp -r .UltiSnips $mypath &&
        mkdir -p $HOME/.config/autostart &&
        mydata=$(cat .config/sxhkd.desktop) &&
        echo "${mydata//MYPATH/"$mypath"}" > $HOME/.config/autostart/sxhkd_uni.desktop &&
        mkdir -p $HOME/.vim/autoload &&
        cp .config/plug.vim $HOME/.vim/autoload &&
        mydata=$(cat .config/.vimrc) &&
        echo "${mydata//MYPATH/"$mypath"}" >> $HOME/.vimrc &&
        curl -LO https://github.com/SirVer/ultisnips/archive/master.zip &&
        rm -r ultisnips-master &&
        unzip master.zip &&
        cp -r ultisnips-master $mypath/.config &&
        tmp=$(find /usr/share/vim/ -maxdepth 1 -regextype sed -regex '/usr/share/vim/vim[0-9]\+') &&
        tmp=(${tmp//\n/ }) &&
        tmp=("${tmp[@]#/usr/share/vim/vim}") &&
        tmp=$(printf '%d\n' "${tmp[@]}" | sort -nr | head -n1) &&
        sudo mkdir -p /usr/share/vim/vim$tmp/spell &&
        sudo cp .config/spell/* /usr/share/vim/vim$tmp/spell &&

        break
    } || {
        echo "Error. Try again"
    }
done

echo Done 
