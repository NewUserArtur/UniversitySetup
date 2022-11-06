#set runtimepath+=~/.vim/bundle/ultisnips-master
set rtp+=MYPATH
set rtp+=MYPATH/current_course

setlocal spell
set spelllang=la,uk,en_us
inoremap <C-l> <c-g>u<Esc>[s1z=`]a<c-g>u

syntax on
set hlsearch
set incsearch
set number
set noswapfile

set tabstop=4
set shiftwidth=4
set expandtab

call plug#begin()

Plug 'lervag/vimtex'
let g:tex_flavor='latex'
let g:vimtex_view_method='zathura'
let g:vimtex_quickfix_mode=0
set conceallevel=1
let g:tex_conceal='abdmg'

Plug 'sirver/ultisnips'
let g:UltiSnipsExpandTrigger = '<tab>'
let g:UltiSnipsJumpForwardTrigger = '<tab>'
let g:UltiSnipsJumpBackwardTrigger = '<S-tab>'
let g:UltiSnipsSnippetDirectories=['.UltiSnips']

call plug#end()

autocmd FileType tex :VimtexCompile
