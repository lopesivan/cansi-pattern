#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1511303758.537245
__CHEETAH_genTimestamp__ = 'Tue Nov 21 20:35:58 2017'
__CHEETAH_src__ = '../m/StateInternal_h.tmpl'
__CHEETAH_srcLastModified__ = 'Tue Nov 21 20:34:02 2017'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class StateInternal_h(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(StateInternal_h, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''#ifndef ''')
        _v = VFN(VFFSL(SL,"state.name",True),"upper",False)() # u'${state.name.upper()}' on line 1, col 10
        if _v is not None: write(_filter(_v, rawExpr=u'${state.name.upper()}')) # from line 1, col 10.
        write(u'''_STATE_INTERNAL_H
#define ''')
        _v = VFN(VFFSL(SL,"state.name",True),"upper",False)() # u'${state.name.upper()}' on line 2, col 10
        if _v is not None: write(_filter(_v, rawExpr=u'${state.name.upper()}')) # from line 2, col 10.
        write(u'''_STATE_INTERNAL_H

/*
 We need a shared definition of our incomplete type
 exposed in the API. One strategy is to define it
 in an include file like this that we can share
 between the different translation units.
 The advantage is that we keep the definition out
 of the API.
*/

/* Simplify the code by using typedefs for the function pointers. */
typedef void (*EventFunc) (''')
        _v = VFN(VFFSL(SL,"state.name",True),"capitalize",False)() # u'${state.name.capitalize()}' on line 14, col 28
        if _v is not None: write(_filter(_v, rawExpr=u'${state.name.capitalize()}')) # from line 14, col 28.
        write(u'''StatePtr);

struct ''')
        _v = VFN(VFFSL(SL,"state.name",True),"capitalize",False)() # u'${state.name.capitalize()}' on line 16, col 8
        if _v is not None: write(_filter(_v, rawExpr=u'${state.name.capitalize()}')) # from line 16, col 8.
        write(u'''State
{
    /*EventFunc func;*/
    EventFunc ''')
        _v = VFN(VFFSL(SL,"state.start.name",True),"lower",False)() # u'${state.start.name.lower()}' on line 19, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'${state.start.name.lower()}')) # from line 19, col 15.
        write(u''';
    EventFunc ''')
        _v = VFN(VFFSL(SL,"state.stop.name",True),"lower",False)() # u'${state.stop.name.lower()}' on line 20, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'${state.stop.name.lower()}')) # from line 20, col 15.
        write(u''';
''')
        if len(VFFSL(SL,"state.states",True)) > 0: # generated from line 21, col 1
            for i in range(0, len(VFFSL(SL,"state.states",True))): # generated from line 22, col 1
                write(u'''    EventFunc  ''')
                _v = VFN(VFN(VFN(VFFSL(SL,"state",True),"states",True)[i],"name",True),"lower",False)() # u'${state.states[i].name.lower()}' on line 23, col 16
                if _v is not None: write(_filter(_v, rawExpr=u'${state.states[i].name.lower()}')) # from line 23, col 16.
                write(u''';
''')
        write(u'''};

#endif
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_StateInternal_h= 'respond'

## END CLASS DEFINITION

if not hasattr(StateInternal_h, '_initCheetahAttributes'):
    templateAPIClass = getattr(StateInternal_h, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(StateInternal_h)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=StateInternal_h()).run()

