export PBASE=/sandbox

export PATH=$PBASE/bin:/bin:/usr/local/bin:/usr/bin:/bin:$PBASE/openresty/luajit/bin:$PBASE/openresty/luarocks/bin:$PBASE/openresty/bin:$PATH
export PYTHONPATH=$PBASE/lib/python:$PBASE/lib/pythonbin:$PBASE/lib/python.zip:$PBASE/lib/jumpscale:$PBASE/lib/pythonbin/lib-dynload:$PBASE/bin
export PYTHONHOME=$PBASE

export LIBRARY_PATH="$PBASE/bin:$PBASE/lib"
export LD_LIBRARY_PATH="$LIBRARY_PATH"

export LDFLAGS="-L$LIBRARY_PATH/"

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

export HOME=$PBASE/root
export HOMEDIR=/root

export PS1="3BOT: "

cd $PBASE

