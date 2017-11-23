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
__CHEETAH_genTime__ = 1511290422.313828
__CHEETAH_genTimestamp__ = 'Tue Nov 21 16:53:42 2017'
__CHEETAH_src__ = '../m/MemoryPool_ADT_c.tmpl'
__CHEETAH_srcLastModified__ = 'Tue Nov 21 16:53:40 2017'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class MemoryPool_ADT_c(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(MemoryPool_ADT_c, self).__init__(*args, **KWs)
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
        _v = VFFSL(SL,"adt.name",True) # u'${adt.name}' on line 1, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name}')) # from line 1, col 12.
        write(u'''.h"
''')
        if len(VFFSL(SL,"adt.class",True)) > 0: # generated from line 2, col 1
            for i in range(0, len(VFFSL(SL,"adt.class",True))): # generated from line 3, col 1
                write(u'''//#include "''')
                _v = VFN(VFN(VFFSL(SL,"adt",True),"class",True)[i],"name",True) # u'${adt.class[i].name}' on line 4, col 14
                if _v is not None: write(_filter(_v, rawExpr=u'${adt.class[i].name}')) # from line 4, col 14.
                write(u'''.h"
''')
        write(u'''#include <stdlib.h>
#include <stdio.h>

struct ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 10, col 8
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 10, col 8.
        write(u'''
{
''')
        for i in range(0, len(VFFSL(SL,"adt.struct",True))): # generated from line 12, col 1
            write(u'''    ''')
            _v = VFN(VFN(VFFSL(SL,"adt",True),"struct",True)[i],"type",True) # u'${adt.struct[i].type}' on line 13, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.struct[i].type}')) # from line 13, col 5.
            write(u''' ''')
            _v = VFN(VFN(VFFSL(SL,"adt",True),"struct",True)[i],"name",True) # u'${adt.struct[i].name}' on line 13, col 27
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.struct[i].name}')) # from line 13, col 27.
            write(u''';
''')
        write(u'''};

#define MAX_NO_OF_''')
        _v = VFN(VFFSL(SL,"adt.name",True),"upper",False)() # u'${adt.name.upper()}' on line 17, col 20
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.upper()}')) # from line 17, col 20.
        write(u'''S 42

static struct ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 19, col 15
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 19, col 15.
        write(u''' objectPool[MAX_NO_OF_''')
        _v = VFN(VFFSL(SL,"adt.name",True),"upper",False)() # u'${adt.name.upper()}' on line 19, col 61
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.upper()}')) # from line 19, col 61.
        write(u'''S];
static size_t numberOfObjects = 0;

''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 22, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 22, col 1.
        _v = VFFSL(SL,"adt.ptr",True) # u'${adt.ptr}' on line 22, col 25
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.ptr}')) # from line 22, col 25.
        write(u''' create''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 22, col 42
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 22, col 42.
        if len(VFFSL(SL,"adt.ctor",True)) > 1: # generated from line 23, col 1
            write(u'''(''')
            for i in range(0, len(VFFSL(SL,"adt.ctor",True))-1): # generated from line 25, col 1
                _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[i],"type",True) # u'${adt.ctor[i].type}' on line 26, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[i].type}')) # from line 26, col 1.
                write(u''' ''')
                _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[i],"name",True) # u'${adt.ctor[i].name}' on line 26, col 21
                if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[i].name}')) # from line 26, col 21.
                write(u''', ''')
            _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[-1],"type",True) # u'${adt.ctor[-1].type}' on line 28, col 1
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[-1].type}')) # from line 28, col 1.
            write(u''' ''')
            _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[-1],"name",True) # u'${adt.ctor[-1].name}' on line 28, col 22
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[-1].name}')) # from line 28, col 22.
            write(u''')
''')
        else: # generated from line 30, col 1
            if len(VFFSL(SL,"adt.ctor",True)) == 0: # generated from line 31, col 1
                write(u'''()
''')
            else: # generated from line 33, col 1
                write(u'''    (''')
                _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[0],"type",True) # u'${adt.ctor[0].type}' on line 34, col 6
                if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[0].type}')) # from line 34, col 6.
                write(u''' ''')
                _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[0],"name",True) # u'${adt.ctor[0].name}' on line 34, col 26
                if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[0].name}')) # from line 34, col 26.
                write(u''')
''')
        write(u'''{
    ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 38, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 38, col 5.
        _v = VFFSL(SL,"adt.ptr",True) # u'${adt.ptr}' on line 38, col 29
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.ptr}')) # from line 38, col 29.
        write(u''' ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 38, col 40
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 38, col 40.
        write(u''' = NULL;

    if (numberOfObjects < MAX_NO_OF_''')
        _v = VFN(VFFSL(SL,"adt.name",True),"upper",False)() # u'${adt.name.upper()}' on line 40, col 37
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.upper()}')) # from line 40, col 37.
        write(u'''S)
    {
        ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 42, col 9
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 42, col 9.
        write(u''' = &objectPool[numberOfObjects++];
        /* Initialize the object... */
        /* Initialize each field in the ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 44, col 41
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 44, col 41.
        write(u'''... */
        ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 45, col 9
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 45, col 9.
        write(u'''->''')
        _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[0],"name",True) # u'${adt.ctor[0].name}' on line 45, col 30
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[0].name}')) # from line 45, col 30.
        write(u''' = ''')
        _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[0],"name",True) # u'${adt.ctor[0].name}' on line 45, col 52
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[0].name}')) # from line 45, col 52.
        write(u''';
        ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 46, col 9
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 46, col 9.
        write(u'''->''')
        _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[1],"name",True) # u'${adt.ctor[1].name}' on line 46, col 30
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[1].name}')) # from line 46, col 30.
        write(u''' = *''')
        _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[1],"name",True) # u'${adt.ctor[1].name}' on line 46, col 53
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[1].name}')) # from line 46, col 53.
        write(u''';
    }
    return ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 48, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 48, col 12.
        write(u''';
}


''')
        if len(VFFSL(SL,"adt.ctor",True)) > 1: # generated from line 52, col 1
            write(u'''void show''')
            _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 53, col 10
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 53, col 10.
            write(u'''(''')
            _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 54, col 2
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 54, col 2.
            _v = VFFSL(SL,"adt.ptr",True) # u'${adt.ptr}' on line 54, col 26
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.ptr}')) # from line 54, col 26.
            write(u''' ''')
            _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 54, col 37
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 54, col 37.
            write(u''')
{
    printf ("Name:\\t%s\\nCity:\\t%s\\nStreet:\\t%s\\n",
        ''')
            _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 57, col 9
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 57, col 9.
            write(u'''->''')
            _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[0],"name",True) # u'${adt.ctor[0].name}' on line 57, col 30
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[0].name}')) # from line 57, col 30.
            write(u''',
        ''')
            _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 58, col 9
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 58, col 9.
            write(u'''->''')
            _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[1],"name",True) # u'${adt.ctor[1].name}' on line 58, col 30
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[1].name}')) # from line 58, col 30.
            write(u'''.''')
            _v = VFN(VFN(VFN(VFFSL(SL,"adt",True),"class",True)[0],"struct",True)[0],"name",True) # u'${adt.class[0].struct[0].name}' on line 58, col 50
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.class[0].struct[0].name}')) # from line 58, col 50.
            write(u''',
        ''')
            _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 59, col 9
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 59, col 9.
            write(u'''->''')
            _v = VFN(VFN(VFFSL(SL,"adt",True),"ctor",True)[1],"name",True) # u'${adt.ctor[1].name}' on line 59, col 30
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.ctor[1].name}')) # from line 59, col 30.
            write(u'''.''')
            _v = VFN(VFN(VFN(VFFSL(SL,"adt",True),"class",True)[0],"struct",True)[1],"name",True) # u'${adt.class[0].struct[1].name}' on line 59, col 50
            if _v is not None: write(_filter(_v, rawExpr=u'${adt.class[0].struct[1].name}')) # from line 59, col 50.
            write(u''')
    ;
}
''')
        write(u'''
void destroy''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 64, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 64, col 13.
        write(u'''(''')
        _v = VFN(VFFSL(SL,"adt.name",True),"capitalize",False)() # u'${adt.name.capitalize()}' on line 65, col 2
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.capitalize()}')) # from line 65, col 2.
        _v = VFFSL(SL,"adt.ptr",True) # u'${adt.ptr}' on line 65, col 26
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.ptr}')) # from line 65, col 26.
        write(u''' ''')
        _v = VFN(VFFSL(SL,"adt.name",True),"lower",False)() # u'${adt.name.lower()}' on line 65, col 37
        if _v is not None: write(_filter(_v, rawExpr=u'${adt.name.lower()}')) # from line 65, col 37.
        write(u''')
{
    /*
      In case de-allocation is needed, an array will still do, but a more
      sophisticated method for keeping track of "allocated" objects will be
      needed.  However, such an algorithm is outside the scope of this book.
    */
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

    _mainCheetahMethod_for_MemoryPool_ADT_c= 'respond'

## END CLASS DEFINITION

if not hasattr(MemoryPool_ADT_c, '_initCheetahAttributes'):
    templateAPIClass = getattr(MemoryPool_ADT_c, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(MemoryPool_ADT_c)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=MemoryPool_ADT_c()).run()


