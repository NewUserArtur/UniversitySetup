ath/.config 
                                                                                                                   
┌──(arthur㉿arthur)-[~/university]
└─$ echo "${$(cat .config/sxhkdrc)//MYPATH/"$mypath"}" > $mypath/.config/sxhkdrc
                                                                                                                   
┌──(arthur㉿arthur)-[~/university]
# general packages
{
    sudo apt install $(cat .config/requirements)
} || {
    brew install $(cat .config/requirements)
} || {
    sudo dnf install $(cat .config/requirements)
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
        read mypath
        mkdir $mypath
        mkdir $mypath/.config
        cp .config/sxhkdrc $mypath/.config
        cp .config/tint2rc $mypath/.config
        mydata=$(cat .config/sxhkdrc)
        echo "${mydata//MYPATH/"$mypath"}" > $mypath/.config/sxhkdrc
        cp -r .scripts $mypath
        cp -r .templates $mypath
        cp -r .UltiSnips $mypath
        mkdir -p $HOME/.config/autostart
        mydata=$(cat .config/sxhkd.desktop)
        echo "${data//MYPATH/"$mypath"}" > $HOME/.config/autostart/sxhkd_uni.desktop
        mkdir -p $HOME/.vim/autoload
        cp .config/plug.vim $HOME/.vim/autoload
        echo "$(cat .config/.vimrc)" >> $HOME/.vimrc

        break
    } || {
        echo "Error. Try again"
    }
done
