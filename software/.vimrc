set nu
syntax on
set ruler
set encoding=utf-8
set autoindent
set tabstop=4
set softtabstop=4
set shiftwidth=4
set backspace=2
set smarttab
set history=1000
set nobackup
set ignorecase
set nohlsearch
set incsearch
set formatoptions=tcrqn
set showmatch
set matchtime=5

call plug#begin('~/.vim/plugged')
Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
Plug 'altercation/vim-colors-solarized'
Plug 'aperezdc/vim-template'
Plug 'boydos/emmet-vim'
call plug#end()
map <F2>  :NERDTreeToggle<CR>
