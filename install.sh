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
        sudo mkdir -p /usr/share/vim/vim90/spell &&
        sudo cp .config/spell/* /usr/share/vim/vim90/spell &&
        curl -LO https://github.com/SirVer/ultisnips/archive/master.zip &&
        unzip master.zip &&
        cp -r ultisnips-master $mypath/.config &&

        break
    } || {
        echo "Error. Try again"
    }
done

echo Done 
