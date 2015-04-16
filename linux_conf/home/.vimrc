set background=dark
colorscheme desert

set cindent
set smartindent
set autoindent

set expandtab
""set textwidth=79
set tabstop=8
set softtabstop=4
set shiftwidth=4

set nocompatible
set showmatch
syntax on
filetype on
au BufNewFile,BufRead *.mak set filetype=html
set hlsearch
highlight Search term=reverse ctermbg=4 ctermfg=7
"highlight Normal ctermbg=black ctermfg=white
"
"""""set color 1""""
"hi Comment ctermfg=Green
""hi Comment ctermfg=darkcyan
"hi Comment ctermfg=blue
"
"""""set color 2""""
"highlight Comment ctermfg=Green
""highlight Comment ctermfg=darkcyan
"highlight Comment ctermfg=blue
"""""""""""""""""""""""""""""""""""""""""""""
colorscheme dawn

"setting cscope
set cscopequickfix=s-,c-,d-,i-,t-,e-

""setting taglist
let Tlist_Show_One_File=1
let Tlist_Exit_OnlyWindow=1
let Tlist_Use_Right_Window = 1
let Tlist_Inc_Winwidth=0

"setting winManager
let g:winManagerWindowLayout='FileExplorer|TagList'
nmap <C-W><C-F> :FirstExplorerWindow<cr>
nmap <C-W><C-B> :BottomExplorerWindow<cr>
nmap <silent> <leader>wm :WMToggle<cr>

"setting minibuffer to enable tab, navigater, and arrows
let g:miniBufExplMapCTabSwitchBufs = 1
let g:miniBufExplMapWindowNavVim = 1
let g:miniBufExplMapWindowNavArrows = 1
let g:miniBufExplModSelTarget = 1

"new-omni-completion
filetype plugin indent on
"set completeopt=longest,menu
autocmd FileType python set omnifunc=pythoncomplete#Complete                                                                                                                                      
let g:ragtag_global_maps = 1

" HTML Tidy, http://tidy.sourceforge.net/
" "  " select xml text to format and hit ,x
vmap ,x :!tidy -q -i -xml<CR>
map <C-n> :bnext<Return>
map <C-p> :bprevious<Return>

" jquery syntax support
au BufRead,BufNewFile jquery.*.js set ft=javascript syntax=jquery
