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
__CHEETAH_genTime__ = 1511304366.362232
__CHEETAH_genTimestamp__ = 'Tue Nov 21 20:46:06 2017'
__CHEETAH_src__ = '../m/State_c.tmpl'
__CHEETAH_srcLastModified__ = 'Tue Nov 21 20:44:31 2017'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class State_c(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(State_c, self).__init__(*args, **KWs)
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
        
        write(u'''#include "''')
        _v = VFN(VFFSL(SL,"state.name",True),"capitalize",False)() # u'${state.name.capitalize()}' on line 1, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'${state.name.capitalize()}')) # from line 1, col 12.
        write(u'''State.h"
#include "''')
        _v = VFN(VFFSL(SL,"state.name",True),"capitalize",False)() # u'${state.name.capitalize()}' on line 2, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'${state.name.capitalize()}')) # from line 2, col 12.
        write(u'''StateInternal.h"

#include "message.h" // DEBUG

/*
Provide the default implementations:
*/

void ''')
        _v = VFFSL(SL,"state.defaultImplementation.name",True) # u'${state.defaultImplementation.name}' on line 10, col 6
        if _v is not None: write(_filter(_v, rawExpr=u'${state.defaultImplementation.name}')) # from line 10, col 6.
        write(u''' (''')
        _v = VFN(VFFSL(SL,"state.name",True),"capitalize",False)() # u'${state.name.capitalize()}' on line 10, col 43
        if _v is not None: write(_filter(_v, rawExpr=u'${state.name.capitalize()}')) # from line 10, col 43.
        write(u'''StatePtr state)
{
    message("** ''')
        _v = VFFSL(SL,"state.defaultImplementation.name",True) # u'${state.defaultImplementation.name}' on line 12, col 17
        if _v is not None: write(_filter(_v, rawExpr=u'${state.defaultImplementation.name}')) # from line 12, col 17.
        write(u''' **");
}
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

    _mainCheetahMethod_for_State_c= 'respond'

## END CLASS DEFINITION

if not hasattr(State_c, '_initCheetahAttributes'):
    templateAPIClass = getattr(State_c, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(State_c)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=State_c()).run()


