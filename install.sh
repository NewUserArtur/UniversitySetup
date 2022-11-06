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
        read path
        mkdir $path
        mkdir $path/.config
        cp .config/sxhkdrc $path/.config
        cp .config/tint2rc $path/.config
        echo "${$(cat .config/sxhkrdrc)//PATH/"$path}" > $path/.config/sxhkdrc
        cp -r .scripts $path
        cp -r .templates $path
        cp -r .UltiSnips $path
        mkdir -p $HOME/.config/autostart
        echo "${$(cat .config/sxhkd.desktop)./PATH/"$path"}" > $HOME/.config/autostart/sxhkd_uni.desktop
        mkdir -p $HOME/.vim/autoload
        cp .config/plug.vim $HOME/.vim/autoload
        echo "$(cat .config/.vimrc)" >> $HOME/.vimrc

        break
    } || {
        echo "Error; Try again"
    }
done
