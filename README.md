# sandbox_osx
hosts the sandbox for python jumpscale

## how to update for python

```
js_shell 'j.tools.sandboxer.python.do(build=True)'
```

- will build python
- the result is in j.dirs.BUILDDIR + "/sandbox/tfbot/"
- this will be copied to base in this directory

don't forget to push

## how to update for openresty & lua

```
js_shell 'j.tools.prefab.local.runtimes.lua.build()'
#to cleanup
js_shell 'j.tools.prefab.local.runtimes.lua.cleanup()'
```


